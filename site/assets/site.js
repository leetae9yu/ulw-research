(() => {
  "use strict";

  const html = document.documentElement;
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const largeScreen = matchMedia("(min-width: 60em)");
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
  const SEARCH_DEBOUNCE_MS = 150;
  const SHEET_CLOSE_FALLBACK_MS = 300;

  const sections = $$(".sec");
  const blocks = $$(".blk");
  const header = $(".hdr");
  const toggleAllBtn = $("#toggle-all");
  const tocOpenBtn = $("#toc-open");
  const tocCloseBtn = $("#toc-close");
  const sheet = $("#toc-sheet");
  const searchToggle = $("#search-toggle");
  const searchForm = $("#search-form");
  const searchInput = $("#q");
  const searchClear = $("#q-clear");
  const status = $("#search-status");
  const toTop = $("#totop");
  const hero = $(".hero");

  const openState = new Map();

  const isOpen = (sec) => openState.get(sec.id) !== false;

  function setOpen(sec, open, animate = true) {
    const btn = $(".sec__btn", sec);
    const body = $(".sec__body", sec);
    btn.setAttribute("aria-expanded", String(open));
    if (open) {
      body.removeAttribute("hidden");
      body.classList.remove("is-entering");
      if (animate && !reducedMotion.matches) {
        void body.offsetWidth;
        body.classList.add("is-entering");
      }
    } else {
      body.setAttribute("hidden", "until-found");
    }
    openState.set(sec.id, open);
    updateToggleAll();
  }

  const mainSections = sections.filter((sec) => !sec.classList.contains("sec--aux"));

  function updateToggleAll() {
    if (!toggleAllBtn) return;
    const anyClosed = mainSections.some((sec) => !isOpen(sec));
    const label = anyClosed ? "모두 펼치기" : "모두 접기";
    toggleAllBtn.dataset.action = anyClosed ? "open" : "close";
    $(".btn__label", toggleAllBtn).textContent = label;
    toggleAllBtn.setAttribute("aria-label", label);
    toggleAllBtn.title = label;
  }

  function applyDefaultState() {
    sections.forEach((sec, index) => {
      const open = sec.dataset.default === "closed" ? false : largeScreen.matches || index === 0;
      setOpen(sec, open, false);
    });
    html.classList.add("is-ready");
  }

  sections.forEach((sec) => {
    $(".sec__btn", sec).addEventListener("click", () => setOpen(sec, !isOpen(sec)));
    $(".sec__body", sec).addEventListener("beforematch", () => setOpen(sec, true, false));
  });

  toggleAllBtn?.addEventListener("click", () => {
    const open = toggleAllBtn.dataset.action === "open";
    sections.forEach((sec) => setOpen(sec, open, false));
  });

  function revealTarget(id) {
    const target = id && document.getElementById(id);
    if (!target) return null;
    const sec = target.closest(".sec");
    if (sec && !isOpen(sec)) setOpen(sec, true, false);
    return target;
  }

  window.addEventListener("hashchange", () => {
    const target = revealTarget(decodeURIComponent(location.hash.slice(1)));
    if (target) target.scrollIntoView({ block: "start" });
  });

  document.addEventListener("click", (event) => {
    const link = event.target.closest('a[href^="#"]');
    if (!link) return;
    const id = decodeURIComponent(link.getAttribute("href").slice(1));
    if (searchInput?.value) clearSearch({ focus: false });
    revealTarget(id);
    if (sheet?.open) closeSheet();
  });

  function openSheet() {
    if (!sheet || sheet.open) return;
    sheet.showModal();
    html.classList.add("sheet-open");
  }

  function finishClose() {
    sheet.classList.remove("is-closing");
    html.classList.remove("sheet-open");
    if (sheet.open) sheet.close();
  }

  function closeSheet() {
    if (!sheet || !sheet.open) return;
    if (reducedMotion.matches) {
      finishClose();
      return;
    }
    sheet.classList.add("is-closing");
    let done = false;
    const once = () => {
      if (done) return;
      done = true;
      sheet.removeEventListener("animationend", once);
      finishClose();
    };
    sheet.addEventListener("animationend", once);
    setTimeout(once, SHEET_CLOSE_FALLBACK_MS);
  }

  tocOpenBtn?.addEventListener("click", openSheet);
  tocCloseBtn?.addEventListener("click", closeSheet);
  sheet?.addEventListener("cancel", (event) => {
    event.preventDefault();
    closeSheet();
  });
  sheet?.addEventListener("click", (event) => {
    if (event.target === sheet) closeSheet();
  });
  sheet?.addEventListener("close", () => html.classList.remove("sheet-open"));

  const tocLinks = $$(".toc a");
  const headingFor = new Map();
  $$(".sec__h, .blk__h").forEach((heading) => {
    const owner = heading.closest(".blk[id], .sec[id]");
    if (owner) headingFor.set(heading, owner.id);
  });

  let currentId = null;
  function setCurrent(id) {
    if (currentId === id) return;
    currentId = id;
    tocLinks.forEach((link) => {
      if (decodeURIComponent(link.hash.slice(1)) === id) link.setAttribute("aria-current", "true");
      else link.removeAttribute("aria-current");
    });
  }

  if ("IntersectionObserver" in window && headingFor.size) {
    const headerPx = header ? header.getBoundingClientRect().height : 56;
    const spy = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting);
      if (visible.length) setCurrent(headingFor.get(visible[0].target));
    }, { rootMargin: `-${Math.round(headerPx)}px 0px -55% 0px`, threshold: 0 });
    headingFor.forEach((_, heading) => spy.observe(heading));
  }

  const normalize = (text) => text.normalize("NFC").toLowerCase();
  const tokensOf = (query) => normalize(query).trim().split(/\s+/).filter(Boolean);
  const matchesAll = (text, tokens) => tokens.every((token) => text.includes(token));
  const escapeRegExp = (text) => text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

  let savedOpenState = null;
  let marks = [];
  let debounceTimer = 0;

  function highlight(root, tokens) {
    const pattern = new RegExp(tokens.map(escapeRegExp).join("|"), "giu");
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        if (!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        const parent = node.parentElement;
        if (!parent || parent.closest("script, style, mark, .sec__h, .blk__h")) return NodeFilter.FILTER_REJECT;
        if (parent.closest("tr[hidden], [hidden]")) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      },
    });
    const targets = [];
    while (walker.nextNode()) targets.push(walker.currentNode);
    targets.forEach((textNode) => {
      const text = textNode.nodeValue;
      pattern.lastIndex = 0;
      if (!pattern.test(text)) return;
      pattern.lastIndex = 0;
      const fragment = document.createDocumentFragment();
      let last = 0;
      let match;
      while ((match = pattern.exec(text)) !== null) {
        if (match.index > last) fragment.appendChild(document.createTextNode(text.slice(last, match.index)));
        const mark = document.createElement("mark");
        mark.textContent = match[0];
        fragment.appendChild(mark);
        marks.push(mark);
        last = match.index + match[0].length;
        if (match[0].length === 0) pattern.lastIndex++;
      }
      if (last < text.length) fragment.appendChild(document.createTextNode(text.slice(last)));
      textNode.parentNode.replaceChild(fragment, textNode);
    });
  }

  function clearHighlights() {
    const parents = new Set();
    marks.forEach((mark) => {
      const parent = mark.parentNode;
      if (!parent) return;
      parent.replaceChild(document.createTextNode(mark.textContent), mark);
      parents.add(parent);
    });
    parents.forEach((parent) => parent.normalize());
    marks = [];
  }

  function showStatus(nodes) {
    status.replaceChildren(...nodes);
    status.hidden = false;
  }

  function makeClearButton() {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "btn";
    btn.textContent = "검색 지우기";
    btn.addEventListener("click", () => clearSearch({ focus: true }));
    return btn;
  }

  function strong(text) {
    const el = document.createElement("strong");
    el.textContent = text;
    return el;
  }

  function runSearch(query) {
    const tokens = tokensOf(query);
    clearHighlights();
    if (!tokens.length) {
      restoreAll();
      return;
    }
    if (!savedOpenState) savedOpenState = new Map(openState);
    searchClear.hidden = false;

    let visibleBlocks = 0;
    blocks.forEach((block) => {
      const blockMatches = matchesAll(normalize(block.textContent), tokens);
      $$("tbody tr", block).forEach((row) => {
        row.hidden = !matchesAll(normalize(row.textContent), tokens);
      });
      $$(".tbl", block).forEach((table) => {
        table.hidden = !$$("tbody tr", table).some((row) => !row.hidden);
      });
      block.hidden = !blockMatches;
      if (blockMatches) {
        visibleBlocks++;
        highlight(block, tokens);
      }
    });
    sections.forEach((sec) => {
      const anyBlock = $$(".blk", sec).some((block) => !block.hidden);
      sec.hidden = !anyBlock;
      if (anyBlock && !isOpen(sec)) setOpen(sec, true, false);
    });

    if (!visibleBlocks) {
      showStatus([
        strong(`"${query.trim()}"`),
        document.createTextNode(" 일치하는 내용이 없습니다. 다른 검색어를 입력하거나 검색을 지우세요."),
        makeClearButton(),
      ]);
      return;
    }
    showStatus([
      strong(`"${query.trim()}"`),
      document.createTextNode(` 일치 ${marks.length}곳 · ${visibleBlocks}개 절 표시 중`),
      makeClearButton(),
    ]);
  }

  function restoreAll() {
    blocks.forEach((block) => {
      block.hidden = false;
      $$("tbody tr, .tbl", block).forEach((el) => { el.hidden = false; });
    });
    sections.forEach((sec) => { sec.hidden = false; });
    if (savedOpenState) {
      sections.forEach((sec) => setOpen(sec, savedOpenState.get(sec.id) !== false, false));
      savedOpenState = null;
    }
    status.hidden = true;
    status.replaceChildren();
    searchClear.hidden = true;
  }

  function clearSearch({ focus }) {
    clearTimeout(debounceTimer);
    searchInput.value = "";
    runSearch("");
    if (focus) searchInput.focus();
  }

  if (searchForm && searchInput) {
    searchForm.addEventListener("submit", (event) => {
      event.preventDefault();
      clearTimeout(debounceTimer);
      runSearch(searchInput.value);
    });
    searchInput.addEventListener("input", () => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => runSearch(searchInput.value), SEARCH_DEBOUNCE_MS);
    });
    searchInput.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && searchInput.value) {
        event.preventDefault();
        clearSearch({ focus: true });
      }
    });
    searchClear.addEventListener("click", () => clearSearch({ focus: true }));
  }

  searchToggle?.addEventListener("click", () => {
    const open = !header.classList.contains("search-open");
    header.classList.toggle("search-open", open);
    searchToggle.setAttribute("aria-expanded", String(open));
    searchToggle.setAttribute("aria-label", open ? "검색 닫기" : "검색 열기");
    if (open) searchInput.focus();
    else if (searchInput.value) clearSearch({ focus: false });
  });

  if (toTop && hero && "IntersectionObserver" in window) {
    new IntersectionObserver(([entry]) => {
      toTop.hidden = entry.isIntersecting;
    }, { threshold: 0 }).observe(hero);
  }

  applyDefaultState();
  const initial = revealTarget(decodeURIComponent(location.hash.slice(1)));
  if (initial) initial.scrollIntoView({ block: "start" });
})();
