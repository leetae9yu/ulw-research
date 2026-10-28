# ulw-research

공개 자료로 조사한 보고서를 날짜별로 모아 두는 저장소입니다. 보고서 원문은 Markdown으로 쓰고, 같은 디자인의 정적 웹 페이지로 만들어 GitHub Pages로 배포합니다.

- 웹 페이지: https://leetae9yu.github.io/ulw-research/
- 이전 주소(https://leetae9yu.github.io/pleos-sdk-research/)는 저장소 이름이 바뀌어 더 이상 열리지 않습니다. 위 새 주소를 쓰세요.

## 주제 목록

| 날짜 | 주제 | 페이지 | 원문 |
|---|---|---|---|
| 2026-10-28 | 서울 AI 해커톤 2026 조사(작성 중) | [열기](https://leetae9yu.github.io/ulw-research/2026-10-28-seoul-ai-hackathon/) | [report.md](topics/2026-10-28-seoul-ai-hackathon/report.md) |
| 2026-10-23 | Pleos SDK 제공 정보 범위 조사 | [열기](https://leetae9yu.github.io/ulw-research/2026-10-23-pleos-sdk/) | [report.md](topics/2026-10-23-pleos-sdk/report.md) |

## 구성

- topics/YYYY-MM-DD-주제/report.md: 주제별 보고서 원문입니다. 폴더 이름의 날짜가 조사 기준일이고, 첫 화면 목록의 날짜 묶음이 됩니다.
- topics/_template/: 새 주제를 만들 때 복사하는 틀입니다. 밑줄(_)로 시작하는 폴더는 빌드에서 빠집니다.
- site/: 생성기(build.py), 템플릿(page.html은 보고서 페이지, index.html은 첫 화면 목록), 스타일과 스크립트입니다.
- docs/: GitHub Pages가 배포하는 생성 결과입니다(main 브랜치의 /docs).

## 주제 추가 방법

1. topics/_template/ 를 topics/YYYY-MM-DD-주제/ 로 복사합니다. 날짜는 조사 기준일이고, 주제 부분은 영문 소문자, 숫자, 하이픈만 씁니다. 예: topics/2026-11-02-ev-charging/
2. report.md 맨 위의 front matter를 채웁니다.
   - title: 페이지 제목
   - subtitle: 제목 위에 붙는 짧은 말(대회나 프로젝트 이름)
   - summary: 첫 화면 목록에 나오는 한 줄 설명
   - status: 작성 중이면 draft를 적습니다. 완성되면 이 줄을 지웁니다.
3. 본문을 Markdown으로 씁니다. "## 1. 제목"은 접고 펼 수 있는 절이 되고, "### 1.1 제목"은 목차의 하위 항목이 됩니다. 표 안의 URL은 출처 번호 링크로 바뀌고 페이지 끝의 출처 목록에 모입니다.
4. 페이지를 만듭니다.

   ```
   python3 site/build.py
   ```

   docs/YYYY-MM-DD-주제/index.html이 만들어지고, docs/index.html 목록에 날짜 최신순으로 추가됩니다. topics/에서 지운 주제의 페이지는 docs/에서도 지워집니다.
5. topics/와 docs/의 변경을 함께 커밋하고 main에 푸시합니다. 1~2분 뒤 Pages에 반영됩니다.

생성기는 Python 3과 markdown, beautifulsoup4 패키지가 필요합니다. 생성 결과에 메일 주소, 전화번호, 로컬 경로, 내부 호스트 이름이 보이면 생성기가 파일을 쓰지 않고 멈춥니다.

## docs/를 커밋하는 이유

GitHub Pages는 main 브랜치의 docs/ 폴더를 그대로 배포합니다. 그래서 생성 결과인 docs/도 저장소에 커밋합니다. 별도의 배포 작업 없이 푸시만으로 페이지가 바뀌고, 생성기를 실행할 수 없는 환경에서도 커밋된 페이지를 그대로 볼 수 있습니다. docs/는 직접 고치지 말고 topics/를 고친 뒤 다시 생성합니다.

## 출처와 이용

각 보고서의 모든 주장 옆에 출처 URL이 있습니다. 인용한 문서의 내용은 요약과 이름 인용 수준으로만 담았으며, 원문은 각 링크에서 확인할 수 있습니다. 확인하지 못한 항목은 "확인 못 함"으로 표시했습니다.
