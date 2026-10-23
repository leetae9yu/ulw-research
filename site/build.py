#!/usr/bin/env python3
"""Build the report site: Markdown -> dist/index.html (single file, no runtime network).

Usage:
    python3 build.py                 # report.md if present, else sec/*.md in filename order
    python3 build.py --src FILE.md   # explicit source
    python3 build.py --out DIR       # output directory (default: site/dist)

Design contract: site/DESIGN.md (Section 9 lists every content transform done here).
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

import markdown
from bs4 import BeautifulSoup, Comment, NavigableString, Tag
from bs4.element import PageElement

NodeList = list["PageElement | str"]

SITE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SITE_DIR.parent
TEMPLATE_PATH = SITE_DIR / "templates" / "page.html"
CSS_PATH = SITE_DIR / "assets" / "site.css"
JS_PATH = SITE_DIR / "assets" / "site.js"

TITLE_SUP = "현대차그룹 차량용 앱 공모전"
TITLE_MAIN = "Pleos SDK 제공 정보 범위 조사"
PAGE_TITLE = f"{TITLE_SUP} · {TITLE_MAIN}"
BASE_DATE = "2026-10-23"
SOURCES_TITLE = "출처 목록"
SOURCES_INTRO = "표 안의 출처 번호가 가리키는 주소입니다. 번호는 문서 전체에서 같은 주소에 같은 번호를 씁니다."
DESCRIPTION_MAX = 155

PILL_STATUS_HEADERS = {"판정", "서드파티 사용", "Playground 상태", "공모전 상태", "상태", "사용 가능 상태"}
PILL_MAX_CHARS = 24
CARD_LAYOUT_MIN_COLS = 4
CARD_LAYOUT_MAX_CELL = 60
CHEVRON_PATH = "m6 9 6 6 6-6"

URL_RE = re.compile(r"https?://[^\s<>\"'()\[\]]+")
URL_TRAILING = ",.;:!?"
XREF_RE = re.compile(r"(\d+\.\d+)절")
NUM_HEADING_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)\.?\s+(.+?)\s*$")
PILL_NOTE_RE = re.compile(r"^(.+?)\s*(\(.+\))$")
# `signature|privileged` inside a table row: a pipe with word characters on both sides is literal text.
LITERAL_PIPE_RE = re.compile(r"(?<=[A-Za-z0-9_])\|(?=[A-Za-z0-9_])")
# `CAR_*`, `register*`: a star glued to an identifier is a wildcard, not emphasis.
WILDCARD_STAR_RE = re.compile(r"(?<=[A-Za-z0-9_])\*")
# `*text*`: a star opening real emphasis sits after a space or line start and before a non-space.
EMPHASIS_OPEN_RE = re.compile(r"(?:^|\s)\*(?=\S)")
IDENT_RE = re.compile(
    r"\b[a-z]{2,}(?:\.[A-Za-z0-9_]+){2,}\b"                  # pleos.car.permission.NAVI_ROUTE, ai.pleos.playground.tts
    r"|\b[A-Z][A-Z0-9]*(?:_(?:[A-Z0-9]+|\*))+"                # CAR_DRIVE, PERF_VEHICLE_SPEED, CONTROL_CAR_*
    r"|\b[a-z][a-z0-9]*(?:[A-Z][A-Za-z0-9]*)+(?:\(\)|\*)?"    # getBrake(), onComplete, moveSeat*
    r"|\b[a-z][a-z0-9]*(?:\(\)|\*)"                           # initialize(), register*
)
TEXT_SKIP_TAGS = {"a", "code", "pre", "script", "style", "h1", "h2", "h3", "h4", "button", "svg"}
IDENT_PARENT_TAGS = {"p", "li", "td"}

PRIVACY_PATTERNS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "phone": re.compile(r"\b0\d{1,2}-\d{3,4}-\d{4}\b"),
    "home path": re.compile(r"/home/|/Users/|[A-Z]:\\\\"),
    "local host": re.compile(r"localhost|127\.0\.0\.1|\.local\b|\.internal\b"),
}


@dataclass
class TocEntry:
    id: str
    num: str | None
    title: str
    children: list["TocEntry"] = field(default_factory=list)


def load_source(explicit: Path | None) -> tuple[str, str]:
    if explicit is not None:
        return explicit.read_text(encoding="utf-8"), str(explicit)
    report = PROJECT_DIR / "report.md"
    if report.exists():
        return report.read_text(encoding="utf-8"), "report.md"
    parts = sorted((PROJECT_DIR / "sec").glob("*.md"))
    if not parts:
        sys.exit("build.py: no report.md and no sec/*.md found")
    texts = [p.read_text(encoding="utf-8").strip("\n") for p in parts]
    return "\n\n".join(texts) + "\n", "sec/*.md (" + ", ".join(p.name for p in parts) + ")"


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:]
    return text


def protect_literal_markup(text: str) -> str:
    out: list[str] = []
    in_fence = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
        elif not in_fence:
            if stripped.startswith("|"):
                line = LITERAL_PIPE_RE.sub(r"\\|", line)
            if "*" in line and not EMPHASIS_OPEN_RE.search(line):
                line = WILDCARD_STAR_RE.sub(r"\\*", line)
        out.append(line)
    return "\n".join(out)


def new(soup: BeautifulSoup, name: str, attrs: dict[str, str] | None = None, text: str | None = None) -> Tag:
    tag = soup.new_tag(name)
    for key, value in (attrs or {}).items():
        tag[key] = value
    if text is not None:
        tag.string = text
    return tag


def svg_icon(soup: BeautifulSoup, path_d: str, cls: str) -> Tag:
    svg = new(soup, "svg", {
        "class": cls, "viewBox": "0 0 24 24", "width": "20", "height": "20", "fill": "none",
        "stroke": "currentColor", "stroke-width": "2", "stroke-linecap": "round",
        "stroke-linejoin": "round", "aria-hidden": "true", "focusable": "false",
    })
    svg.append(new(soup, "path", {"d": path_d}))
    return svg


def split_heading(text: str) -> tuple[str | None, str]:
    match = NUM_HEADING_RE.match(text)
    if match:
        return match.group(1), match.group(2)
    return None, text.strip()


def is_blank(node: object) -> bool:
    return isinstance(node, NavigableString) and not str(node).strip()


def has_ancestor(node: NavigableString, names: set[str]) -> bool:
    return any(isinstance(p, Tag) and p.name in names for p in node.parents)


def inside_pill(node: NavigableString) -> bool:
    return any(isinstance(p, Tag) and "pill" in (p.get("class") or []) for p in node.parents)


def text_nodes(root: Tag, skip: set[str]) -> Iterator[NavigableString]:
    for node in list(root.find_all(string=True)):
        if isinstance(node, Comment) or not isinstance(node, NavigableString):
            continue
        if has_ancestor(node, skip) or inside_pill(node):
            continue
        yield node


def replace_text_node(node: NavigableString, parts: NodeList) -> None:
    node.replace_with(*[p for p in parts if p != ""])


class Doc:
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup
        self.ids: set[str] = set()
        self.toc: list[TocEntry] = []
        self.sources: dict[str, int] = {}
        self.table_count = 0

    def unique_id(self, base: str) -> str:
        candidate, n = base, 2
        while candidate in self.ids:
            candidate = f"{base}-{n}"
            n += 1
        self.ids.add(candidate)
        return candidate

    def heading_id(self, num: str | None, index: int) -> str:
        return self.unique_id(f"s-{num.replace('.', '-')}" if num else f"s-x{index}")

    def build(self) -> Tag:
        soup = self.soup
        self.drop_title_h1_and_demote_others()
        top = [n for n in list(soup.contents) if not is_blank(n)]
        article = new(soup, "div", {"class": "doc-body"})

        lead: NodeList = []
        sections: list[tuple[Tag, NodeList]] = []
        for node in top:
            if isinstance(node, Tag) and node.name == "h2":
                sections.append((node, []))
            elif sections:
                sections[-1][1].append(node)
            else:
                lead.append(node)

        if lead:
            lead_block = new(soup, "div", {"class": "blk blk--lead", "id": self.unique_id("s-lead"), "data-block": ""})
            for node in lead:
                lead_block.append(node)
            article.append(lead_block)

        for index, (h2, nodes) in enumerate(sections, 1):
            article.append(self.make_section(h2, nodes, index))
        return article

    def drop_title_h1_and_demote_others(self) -> None:
        first_heading = self.soup.find(["h1", "h2", "h3"])
        for h1 in self.soup.find_all("h1"):
            if h1 is first_heading:
                h1.decompose()
            else:
                h1.name = "h2"

    def section_shell(self, sid: str, num: str | None, title: str, extra_class: str = "") -> tuple[Tag, Tag]:
        soup = self.soup
        section = new(soup, "section", {"class": f"sec {extra_class}".strip(), "id": sid, "aria-labelledby": f"h-{sid}"})
        heading = new(soup, "h2", {"class": "sec__h", "id": f"h-{sid}"})
        button = new(soup, "button", {
            "class": "sec__btn", "type": "button", "aria-expanded": "true", "aria-controls": f"b-{sid}",
        })
        if num:
            button.append(new(soup, "span", {"class": "num"}, num))
        button.append(new(soup, "span", {"class": "ttl"}, title))
        button.append(svg_icon(soup, CHEVRON_PATH, "chev"))
        heading.append(button)
        section.append(heading)
        body = new(soup, "div", {"class": "sec__body", "id": f"b-{sid}"})
        section.append(body)
        return section, body

    def make_section(self, h2: Tag, nodes: NodeList, index: int) -> Tag:
        soup = self.soup
        num, title = split_heading(h2.get_text(" ", strip=True))
        sid = self.heading_id(num, index)
        section, body = self.section_shell(sid, num, title)
        h2.decompose()

        entry = TocEntry(sid, num, title)
        self.toc.append(entry)

        current_block: Tag | None = None
        block_index = 0
        for node in nodes:
            if isinstance(node, Tag) and node.name == "h3":
                block_index += 1
                sub_num, sub_title = split_heading(node.get_text(" ", strip=True))
                bid = self.heading_id(sub_num, index * 100 + block_index)
                current_block = new(soup, "div", {"class": "blk", "id": bid, "data-block": ""})
                h3 = new(soup, "h3", {"class": "blk__h", "id": f"h-{bid}"})
                if sub_num:
                    h3.append(new(soup, "span", {"class": "num"}, sub_num))
                h3.append(new(soup, "span", {"class": "ttl"}, sub_title))
                current_block.append(h3)
                body.append(current_block)
                node.decompose()
                entry.children.append(TocEntry(bid, sub_num, sub_title))
                continue
            if current_block is None:
                current_block = new(soup, "div", {"class": "blk blk--lead", "data-block": ""})
                body.append(current_block)
            current_block.append(node)
        return section

    def process_tables(self, root: Tag) -> None:
        soup = self.soup
        for table in root.find_all("table"):
            self.table_count += 1
            headers = [th.get_text(" ", strip=True) for th in table.select("thead th")]
            ncols = len(headers)
            max_cell = max((len(td.get_text(" ", strip=True)) for td in table.select("tbody td")), default=0)
            layout = "cards" if (ncols >= CARD_LAYOUT_MIN_COLS or max_cell > CARD_LAYOUT_MAX_CELL) else "scroll"
            first_cells = [tr.find("td") for tr in table.select("tbody tr")]
            numbered = bool(first_cells) and all(td is not None and td.get_text(strip=True).isdigit() for td in first_cells)

            for th in table.select("thead th"):
                th["scope"] = "col"
            status_cols = {i for i, h in enumerate(headers) if h in PILL_STATUS_HEADERS}
            for tr in table.select("tbody tr"):
                cells = tr.find_all("td", recursive=False)
                row_is_status = bool(cells) and cells[0].get_text(" ", strip=True) in PILL_STATUS_HEADERS
                for j, td in enumerate(cells):
                    if j < ncols:
                        td["data-label"] = headers[j]
                    if (j in status_cols or (row_is_status and j > 0)) and not td.find_all():
                        self.pillify(td)
                    if layout == "cards":
                        wrapper = new(soup, "span", {"class": "cell"})
                        for child in list(td.contents):
                            wrapper.append(child)
                        td.append(wrapper)

            label = f"표 {self.table_count}: " + ", ".join(headers)
            if len(label) > 120:
                label = label[:117] + "..."
            scroll = new(soup, "div", {"class": "tbl__scroll", "role": "region", "tabindex": "0", "aria-label": label})
            classes = f"tbl tbl--{layout}" + (" tbl--numbered" if numbered else "")
            figure = new(soup, "figure", {"class": classes, "data-cols": str(ncols)})
            table.wrap(scroll)
            scroll.wrap(figure)

    def pillify(self, td: Tag) -> None:
        text = td.get_text(" ", strip=True)
        tone = pill_tone(text)
        if tone is None:
            return
        note_match = PILL_NOTE_RE.match(text)
        label, note = (note_match.group(1), note_match.group(2)) if note_match else (text, None)
        td.clear()
        td.append(new(self.soup, "span", {"class": f"pill pill--{tone}"}, label))
        if note:
            td.append(" ")
            td.append(new(self.soup, "span", {"class": "pill__note"}, note))

    def linkify(self, root: Tag) -> None:
        for node in text_nodes(root, TEXT_SKIP_TAGS):
            text = str(node)
            if "http://" not in text and "https://" not in text:
                continue
            in_table = has_ancestor(node, {"td", "th"})
            parts: NodeList = []
            pos = 0
            for match in URL_RE.finditer(text):
                url, end = match.group(0), match.end()
                while url and url[-1] in URL_TRAILING:
                    url, end = url[:-1], end - 1
                parts.append(text[pos:match.start()])
                parts.append(self.source_link(url) if in_table else self.inline_link(url))
                pos = end
            parts.append(text[pos:])
            replace_text_node(node, parts)

    def inline_link(self, url: str) -> Tag:
        soup = self.soup
        a = new(soup, "a", {"class": "url", "href": url})
        display = re.sub(r"^https?://", "", url)
        for i, segment in enumerate(display.split("/")):
            if i:
                a.append("/")
                a.append(new(soup, "wbr"))
            if segment:
                a.append(segment)
        return a

    def source_link(self, url: str) -> Tag:
        number = self.sources.setdefault(url, len(self.sources) + 1)
        return new(self.soup, "a", {"class": "src", "href": url, "title": url}, f"출처{number}")

    def crossref(self, root: Tag) -> None:
        for node in text_nodes(root, TEXT_SKIP_TAGS):
            text = str(node)
            if "절" not in text:
                continue
            parts: NodeList = []
            pos = 0
            for match in XREF_RE.finditer(text):
                target = f"s-{match.group(1).replace('.', '-')}"
                if target not in self.ids:
                    continue
                parts.append(text[pos:match.start()])
                parts.append(new(self.soup, "a", {"class": "xref", "href": f"#{target}"}, match.group(0)))
                pos = match.end()
            if not parts:
                continue
            parts.append(text[pos:])
            replace_text_node(node, parts)

    def mark_identifiers(self, root: Tag) -> None:
        for node in text_nodes(root, TEXT_SKIP_TAGS | {"th"}):
            if not has_ancestor(node, IDENT_PARENT_TAGS):
                continue
            in_cell = has_ancestor(node, {"td"})
            text = str(node)
            parts: NodeList = []
            pos = 0
            for match in IDENT_RE.finditer(text):
                parts.append(text[pos:match.start()])
                parts.append(new(self.soup, "code", None, match.group(0)))
                if in_cell:
                    parts.append(new(self.soup, "wbr"))
                pos = match.end()
            if not parts:
                continue
            parts.append(text[pos:])
            replace_text_node(node, parts)

    def sources_section(self) -> str:
        if not self.sources:
            return ""
        soup = self.soup
        sid = self.unique_id("s-sources")
        section, body = self.section_shell(sid, None, SOURCES_TITLE, "sec--aux")
        section["data-default"] = "closed"
        block = new(soup, "div", {"class": "blk blk--lead", "data-block": ""})
        block.append(new(soup, "p", None, SOURCES_INTRO))
        ol = new(soup, "ol", {"class": "srcs"})
        for url, number in sorted(self.sources.items(), key=lambda kv: kv[1]):
            li = new(soup, "li", {"id": f"src-{number}"})
            li.append(self.inline_link(url))
            ol.append(li)
        block.append(ol)
        body.append(block)
        self.toc.append(TocEntry(sid, None, SOURCES_TITLE))
        return str(section)

    def toc_html(self) -> str:
        def item(entry: TocEntry) -> str:
            num = f'<span class="toc__num">{esc(entry.num)}</span>' if entry.num else ""
            return f'<a href="#{entry.id}">{num}<span class="toc__ttl">{esc(entry.title)}</span></a>'

        items = []
        for entry in self.toc:
            children = "".join(f"<li>{item(c)}</li>" for c in entry.children)
            sub = f'<ol class="toc__sub">{children}</ol>' if children else ""
            items.append(f"<li>{item(entry)}{sub}</li>")
        return f'<ol class="toc">{"".join(items)}</ol>'


def pill_tone(text: str) -> str | None:
    t = text.strip()
    if not t or len(t) > PILL_MAX_CHARS:
        return None
    if t.startswith("준비 중"):
        return "part"
    if "불가" in t or "없음" in t:
        return "no"
    if "가능" in t:
        return "ok"
    if "부분" in t:
        return "part"
    if "확인 못 함" in t:
        return "unk"
    return None


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def description_from(root: Tag) -> str:
    first = root.find(["p", "li"])
    text = first.get_text(" ", strip=True) if first else PAGE_TITLE
    text = re.sub(r"\s+", " ", text)
    if len(text) > DESCRIPTION_MAX:
        cut = text[:DESCRIPTION_MAX].rsplit(" ", 1)[0]
        text = cut.rstrip(" ,.;") + "…"
    return text


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_DIR))
    except ValueError:
        return str(path)


def privacy_scan(html: str) -> list[str]:
    hits = []
    for name, pattern in PRIVACY_PATTERNS.items():
        for match in pattern.finditer(html):
            hits.append(f"{name}: {match.group(0)}")
    return hits


def compact_css(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};:,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()


def compact_js(js: str) -> str:
    lines = [line.strip() for line in js.splitlines()]
    return "\n".join(line for line in lines if line)


def render_page(doc: Doc, content_html: str, sources_html: str, description: str) -> str:
    page = TEMPLATE_PATH.read_text(encoding="utf-8")
    values = {
        "TITLE": esc(PAGE_TITLE),
        "TITLE_SUP": esc(TITLE_SUP),
        "TITLE_MAIN": esc(TITLE_MAIN),
        "BASE_DATE": BASE_DATE,
        "DESCRIPTION": esc(description),
        "CSS": compact_css(CSS_PATH.read_text(encoding="utf-8")),
        "JS": compact_js(JS_PATH.read_text(encoding="utf-8")),
        "TOC": doc.toc_html(),
        "CONTENT": content_html,
        "SOURCES": sources_html,
    }
    for key, value in values.items():
        page = page.replace("{{" + key + "}}", value)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", page)
    if leftover:
        sys.exit(f"build.py: unresolved template placeholders: {leftover}")
    return page


def build(src: Path | None, out_dir: Path) -> Path:
    text, source_label = load_source(src)
    text = protect_literal_markup(strip_front_matter(text))

    converter = markdown.Markdown(extensions=["tables", "sane_lists", "fenced_code"], output_format="html")
    soup = BeautifulSoup(converter.convert(text), "html.parser")

    doc = Doc(soup)
    article = doc.build()
    doc.process_tables(article)
    doc.linkify(article)
    doc.crossref(article)
    doc.mark_identifiers(article)
    content_html = "".join(str(child) for child in article.contents)
    sources_html = doc.sources_section()
    page = render_page(doc, content_html, sources_html, description_from(article))

    hits = privacy_scan(page)
    if hits:
        sys.exit("build.py: refusing to write output, sensitive patterns found:\n  " + "\n  ".join(hits))

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "index.html"
    out_file.write_text(page, encoding="utf-8")
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")

    print(f"source   : {source_label}")
    print(f"sections : {len(doc.toc)} (h2) / {sum(len(e.children) for e in doc.toc)} (h3)")
    print(f"tables   : {doc.table_count}, sources: {len(doc.sources)}")
    print(f"output   : {display_path(out_file)} ({out_file.stat().st_size // 1024} KB)")
    return out_file


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--src", type=Path, default=None, help="Markdown source (default: report.md or sec/*.md)")
    parser.add_argument("--out", type=Path, default=SITE_DIR / "dist", help="output directory (default: site/dist)")
    args = parser.parse_args()
    build(args.src, args.out)


if __name__ == "__main__":
    main()
