---
title: 2026 서울 AI 디지털 배움터 청년 해커톤 트랙별 조사
subtitle: 서울 AI 해커톤 2026
summary: 대회 규칙과 심사 기준, 트랙 A~D의 서울 문제 수치·기존 사업·공개 데이터·아이디어를 조사하고, 추천 트랙과 팀 역할, 6시간 일정, 사전 준비 목록을 정리했습니다.
created: 2026-10-28
updated: 2026-10-28
aliases: 2026-10-28-seoul-ai-hackathon
---

# 2026 서울 AI 디지털 배움터 청년 해커톤 트랙별 조사

조사 기준일: 2026년 10월 28일. 공개 자료만 사용했고, 모든 수치는 원 페이지와 다시 대조했습니다. 추정은 추정이라고 표시했습니다.

## 1. 요약

- 심사는 현장 작동 실용성, 정보 약자용 디지털 포용 UX, 시민 체감 효과를 봅니다. 제출물은 작동 프로토타입, 기획·기대효과서 PDF, GitHub 저장소, 접근성 시연 발표자료 4종입니다(2절).
- 핵심 기능 코드를 미리 작성하면 실격입니다. 주최 측은 commit 기록으로 사전 개발 여부를 확인합니다. 기획, 디자인, 개발 환경, 빈 프로젝트 구조는 미리 준비해도 됩니다(2.1절).
- 추천 1순위는 트랙 B(소상공인)입니다. 서울 상권 데이터가 가장 풍부하고, 큰 버튼·음성으로 쓰는 가게 건강검진과 지원금 길잡이를 6시간 안에 만들 수 있습니다. 2순위는 트랙 A(복지·돌봄)입니다(5절).
- 공지의 문제 근거 수치 일부는 서울이 아닌 전국·수도권 값입니다. 서울 가동사업자 1.2만 명 순감은 서울 원표를 찾지 못했습니다. 발표에는 4절 표의 값과 범위를 씁니다.
- 대회 전에 할 일은 신청(11/8 마감), 공공데이터 인증키와 무료 LLM 키 발급, 화면 설계, 배포 환경 연결입니다(8절).

## 2. 대회 규칙과 심사 기준

주요 평가 요소는 현장에서 실제 작동하는 실용성, 정보 약자도 쉽게 쓰는 디지털 포용 UX, 시민이 체감하는 효과입니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

공식 안내의 핵심 가치는 실용성(Utility), 디지털 포용(Inclusion), 시민 체감(Impact)입니다. 대상 예시로 고령자, 1인가구, 장애인, 소상공인을 들고, 만든 MVP를 서울시 행정 서비스와 디지털배움터 교육·복지 현장에 연계한다고 밝혔습니다. [출처: https://goorm.notion.site/2026-AI-3ec4e6997fb0806ca882d12e501f97c9]

| 항목 | 내용 | 출처 |
|---|---|---|
| 자격 | 만 19~39세, 직업 제한 없음, 5~6인 팀 | FAQ, 링커리어 |
| 모집 | 10/12(월)~11/8(일), 신청 https://forms.gle/HNx9CiyYZS3sXuwj9 | 링커리어 본문 |
| 사전 세미나 | 11/14(토) 13:00~18:00, 구름스퀘어 강남, 온·오프라인 병행, 바이브코딩 | 링커리어 본문 |
| 본선 | 11/21(토) 09:00~19:00, 아키스케치 성수, 6시간 개발·발표·심사 | 링커리어 본문 |
| 제출물 | 작동하는 프로토타입(웹/앱/챗봇 등), 서비스 기획 및 기대효과서 PDF, GitHub 저장소, 정보 약자 접근성을 반영한 시연 발표자료 | FAQ |
| 데이터 | 서울시 데이터 권장, 저작권 문제가 없는 타 공공데이터와 직접 구축한 데이터도 가능 | FAQ |
| 시상 | 총 300만 원 상당, 세부는 추후 공지. 당일 상위 4팀 발표, 12/8(화) 용산아이파크몰 7층 CGV 시상식(대표 1인 참석) | FAQ, 링커리어 |
| 지적재산권 | 원칙적으로 참가팀 귀속 | FAQ |
| 기타 | 점심 제공, 주차 지원 없음 | FAQ |

링커리어 상단의 접수 시작일은 2026.10.16으로 표기되어 본문의 10/12와 다릅니다. 마감일 11/8은 두 곳이 같습니다. [출처: https://linkareer.com/activity/357358]

### 2.1 사전 준비 허용 범위

핵심 기능 코딩은 본선 당일 현장에서 해야 합니다. 주최 측은 commit 기록을 확인하고, 사전 개발이 적발되면 실격 처리합니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

| 구분 | 미리 해도 되는 것 |
|---|---|
| 기획 | 문제 정의, 기능 기획, 사용자 시나리오, 발표 자료 구성 |
| 디자인 | 와이어프레임, UI·화면 설계, 로고 |
| 개발 환경 | 계정 생성, GitHub 저장소, 배포 환경 구성, 프레임워크·라이브러리 설치, ERD·파이프라인 등 개발 계획 문서 |
| 기본 템플릿 | 빈 프로젝트 구조와 스캐폴딩, 공개 오픈소스·공개 API 활용 |

본선 당일에는 사전에 제출한 작업물의 피드백을 참고해 진행하라는 안내가 있습니다. 사전 제출 절차와 마감은 공지에서 확인하지 못했습니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

트랙 1~3의 문제 근거는 참고용이며, 팀이 페인포인트를 더 구체화하거나 다르게 해석해도 됩니다. 자유주제는 시민 체감형 공익 가치와 디지털배움터의 포용적 AI 방향을 반영해야 합니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

## 3. 지난 대회와 심사 경향

같은 이름으로 열린 지난 회차와 수상작은 찾지 못했습니다. 서울시와 구름이 연 비슷한 대회의 결과는 다음과 같습니다.

| 대회 | 규모와 형식 | 대상 또는 상위 수상작 | 출처 |
|---|---|---|---|
| 2024 서울 프롬프톤 | 67개 팀(190명), 10팀 시상 | 디지털 소외 계층용 음성 버스 예매 AI(대상) | https://mas.smc.seoul.kr/attach/record/SEOUL/appendix/a11/A0068626.pdf , https://www.seoul.co.kr/news/society/2024/07/12/20240712500037 |
| 2025 서울 AI 해커톤 | 8.12~10.2, 2~3인 팀, 122팀 331명 | 관광객용 VR·AI 도슨트 서울메아리(대상) | https://mas.smc.seoul.kr/attach/record/SEOUL/appendix/a11/A0070091.pdf |
| 구름톤 유니브 2024 벚꽃톤 | 35개 대학 300여 명, 팀당 6~7명 | 소상공인 SNS 게시물 자동 생성 AI(대상) | https://blog.goorm.io/goorm_beotkkotthon/ |
| 2025 국토교통 데이터 경진대회 | 193개 팀, 9개 수상작 | AI 시니어 보행 안전지도(대상) | http://www.cenews.kr/news/articleView.html?idxno=38331 |

수상작에는 공통점이 있습니다. 대상자가 고령자, 디지털 소외 계층, 중장년 소상공인처럼 분명했고, 음성·자동 생성·지도처럼 입력 부담을 줄이는 방식을 썼습니다(추정). 이번 대회의 배점표는 공개되지 않았습니다. 다른 공공 데이터 대회는 공공데이터 활용, 독창성, 기술성(완성도), 발전 가능성을 주로 심사했습니다. [출처: https://www.mofa.go.kr/www/brd/m_4075/view.do?seq=369236 , https://data.mafra.go.kr/contest/noticeViewNew.do?bbs_no=635]

구름은 2024 벚꽃톤 상위 5개 팀의 서비스화를 지원하겠다고 밝혔습니다. 이번 대회도 MVP를 현장에 연계하는 것을 목표로 두어, 실제 운영 기관에 붙일 수 있는 서비스가 유리합니다(추정). [출처: https://blog.goorm.io/goorm_beotkkotthon/ , https://goorm.notion.site/2026-AI-3ec4e6997fb0806ca882d12e501f97c9]

## 4. 트랙별 조사 결과

공지에 적힌 문제 근거 수치 가운데 일부는 서울이 아닌 전국·수도권 값이거나 기준일이 없습니다. 발표 자료에는 아래 표의 원출처 값과 범위를 쓰는 편이 안전합니다.

| 공지 수치 | 확인한 값 | 범위와 기준 | 출처 |
|---|---|---|---|
| 고령인구 약 196만 명(20.8%) | 2025년 184.3만 명, 19.9% | 서울, 2025년 | https://data.si.re.kr/smr/smr2025/reports/SMR2025_01_POPULATION_SI.html |
| 등록장애인 약 38만 명 | 384,934명 | 서울, 2025년 12월 말 | https://wis.seoul.go.kr/wfs/dhs/reg/policy.do?crtId=PLP01050303 |
| 폐업률 8.87%, 약 54만 8천 개 | 547,764개 | 수도권, 2025년 국세청 사업자 | https://www.mss.go.kr/site/daejeon/ex/bbs/View.do?bcIdx=1069524&cbIdx=172 |
| 소매업 15.4%, 음식점업 15.1% | 전국 업종 폐업률 | 전국, 2025년, 전년보다 낮음 | https://www.mss.go.kr/site/daejeon/ex/bbs/View.do?bcIdx=1069524&cbIdx=172 |
| 폐업 사유 사업부진 50.4% | 전체 폐업 사업자 중 비중 | 전국, 2025년 | https://www.mss.go.kr/site/daejeon/ex/bbs/View.do?bcIdx=1069524&cbIdx=172 |
| 서울 가동사업자 1.2만 명 순감 | 서울 원표 확인 못 함 | 전국 음식업 신규와 폐업의 차이(12,443명)와 수치가 같음 | https://www.mss.go.kr/site/daejeon/ex/bbs/View.do?bcIdx=1069524&cbIdx=172 |
| 폐업자 평균 부채 약 8,500만 원 | 부채가 있는 응답자의 평균 | 전국 조사 참여자, 2026년 5월 | https://www.mss.go.kr/site/daejeon/ex/bbs/View.do?bcIdx=1069524&cbIdx=172 |
| 쉬었음 청년 40만 명 이상 | 2025년 8월 44.6만 명, 2026년 9월 36.4만 명 | 전국 15~29세 | https://mods.go.kr/board.es?act=view&bid=210&list_no=447479&mid=a10301010000 |
| 원하는 일자리가 없어서 34.1% | 34.1% | 전국 15~29세 쉬었음 응답자, 2025년 8월 | https://www.kostat.go.kr/boardDownload.es?bid=210&list_no=439131&seq=5 |

영유아·초등 아동 약 80만 명은 공지의 원출처와 연령 기준을 확인하지 못했습니다.

### 4.1 트랙 A 돌봄과 복지

- 2024년 서울 1인가구는 약 166만 가구로 전체 가구의 39.9%입니다. [출처: https://news.seoul.go.kr/welfare/archives/577951] 서울 1인가구의 62.1%가 외로움을 호소하고, 서울시는 고립·은둔 청년을 약 13만 명으로 추산합니다. [출처: https://english.seoul.go.kr/seoul-policy-archive/seoul-without-loneliness/]
- 2024년 전국 고독사 사망자는 3,924명으로 2023년 3,661명보다 늘었습니다. [출처: https://www.mohw.go.kr/board.es?act=view&bid=0027&list_no=1488039&mid=a10503010100&nPage=1&tag=]
- 2025년 디지털 취약계층의 디지털정보화 수준은 일반 국민 대비 77.9%입니다(전국). [출처: https://eiec.kdi.re.kr/policy/materialView.do?num=278528&pg=&pp=&topic=C]
- 서울시는 위기가구를 18개 기관 44종 빅데이터로 발굴하고, AI 안부확인을 18개 자치구에서 운영합니다. 서울형 통합돌봄 대상은 65세 이상과 65세 미만 심한 장애인으로 한정됩니다. [출처: https://wis.seoul.go.kr/was/cfs/crisisFamilyInfo.do , https://news.seoul.go.kr/welfare/archives/574354 , https://www.newspim.com/news/view/20261021000563]
- 복지로 앱은 복지위기 알림과 시설 검색을 제공하고 평점 3.8점을 표시합니다. 국민비서 129 챗봇은 로그인 없이 24시간 쓸 수 있습니다. [출처: https://apps.apple.com/kr/app/%EB%B3%B5%EC%A7%80%EB%A1%9C/id490534512 , https://www.129.go.kr/counsel/counsel04.do]
- 쓸 수 있는 데이터는 서울시 복지서비스 목록, 장애인 등록현황, 장애인 편의시설 설치현황, 교통약자이용정보 등 12종입니다. 개인 단위 위험 데이터는 개방되지 않아 합성 데이터로 시연해야 합니다. 상세는 11.4절에 있습니다.

### 4.2 트랙 B 소상공인

- 2022~2024년 서울 소상공인의 폐업 고려 비율은 14.4%에서 20.2%로 올랐습니다. 2024년 폐업 이유는 경기침체 29.7%, 매출부진 23.4%입니다. [출처: https://mediahub.seoul.go.kr/archives/2016341]
- 2024년 서울 신규 사업자는 22.6만 명, 폐업 사업자는 19.6만 명입니다. [출처: https://data.si.re.kr/smr/smr2025/reports/SMR2025_03_INDECON_SI.html]
- 2024년 디지털·스마트 기술을 쓰는 소상공인은 27.2%입니다(전국). [출처: https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1066231&cbIdx=86]
- 서울시는 2026년 315억 원으로 소상공인 2만 4천여 명을 지원하고, 금융자료로 위기 징후를 찾아 3천 명을 조기 발굴합니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=452037 , https://news.seoul.go.kr/economy/archives/567673]
- 서울시 상권분석서비스는 1,650개 상권과 100개 업종 정보를 제공하고, AI 기반 분석은 2027년에 추진합니다. [출처: https://scpm.seoul.go.kr/seoul-policy/evt0253]
- 서울 상권 데이터(추정매출, 점포, 길단위인구)는 OpenAPI와 파일로 제공되며 인증키가 필요합니다. 상세는 12.4절에 있습니다. [출처: https://data.seoul.go.kr/dataList/OA-15577/S/1/datasetView.do]

### 4.3 트랙 C 청년 일자리

- 2026년 5월 전국 청년 고용률은 43.8%입니다. 전공과 매우 일치하는 취업은 27.0%이고 첫 취업까지 평균 11.2개월이 걸렸습니다. [출처: https://www.korea.kr/news/policyNewsView.do?newsId=156771847]
- 2026년 9월 전국 15~29세 쉬었음 인구는 36만 4천 명으로 전년보다 4만 4천 명 줄었습니다. [출처: https://mods.go.kr/board.es?act=view&bid=210&list_no=447479&mid=a10301010000]
- 서울연구원은 질 낮은 과거 일자리 경험, 역량 부족, 관계 단절, 정책 정보 부족이 쉬었음 위험을 높인다고 분석했습니다. [출처: https://www.si.re.kr/bbs/view.do?key=2024100039&pstSn=2606190001]
- 서울시는 2021년부터 2025년 8월까지 18개 청년 일자리 사업에 7,455억 원을 투입했습니다. 청년취업사관학교의 2025년 취업률은 77%입니다. [출처: https://news.seoul.go.kr/gov/archives/571364 , https://www.seoul.go.kr/news/news_report.do?nttNo=457379]
- 고용24와 잡케어는 이미 AI 매칭을 제공하며, 2025년 말 기준 이용 후 취업자는 17만 2천 명입니다. 이력서 정보가 없는 사용자는 입력 부담이 큽니다. [출처: https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=19100 , https://www.keis.or.kr/keis/ko/conts/100/web.do]
- 훈련과정 API는 자동승인, 훈련기관 목록은 키 없는 CSV입니다. 채용·직무 API는 심사 후 키를 줍니다. 상세는 13.4절에 있습니다.

### 4.4 트랙 D 자유주제

- 2024년 서울 보행 교통사고 사망자는 117명이고, 이 가운데 65세 이상이 68.4%입니다. [출처: https://news.seoul.go.kr/traffic/archives/335 , https://news.seoul.go.kr/traffic/archives/514766?listPage=1]
- 2025년 5월 15일~7월 7일 서울 온열질환자는 85명으로 전년 같은 기간 27명보다 늘었습니다. [출처: https://news.seoul.go.kr/welfare/archives/571990]
- 2023년 보도 기준 공공 모바일 앱 233개 중 접근성 인증 앱은 13개(5%)입니다. [출처: https://zdnet.co.kr/view/?no=20231016095118]
- 서울시는 서울동행맵, 서울톡(현장 민원 54종), 서울안전누리를 운영합니다. 이미 받은 안내문을 쉬운 글과 음성으로 바꾸는 기능은 확인되지 않았습니다. [출처: https://english.seoul.go.kr/seoul-helping-map-app-wins-uitp-awards-2025-for-diversity-and-inclusion/ , https://news.seoul.go.kr/gov/archives/511223]
- 서울 실시간 도시데이터는 주요 장소 121곳의 인구·도로(5분), 날씨·환경(10분)을 줍니다. 무더위쉼터 데이터는 2026년 8월 10일 뒤 일부 항목이 빈값입니다. [출처: https://data.seoul.go.kr/dataVisual/seoul/guide.do , https://data.seoul.go.kr/dataList/OA-21065/S/1/datasetView.do?tab=A]

## 5. 트랙 비교와 추천

점수는 1~5점입니다. 경쟁 예상은 경쟁이 적을수록 높습니다. 경쟁 예상 점수는 모두 추정입니다.

| 항목 | A 복지·돌봄 | B 소상공인 | C 청년 일자리 | D 자유주제 |
|---|---|---|---|---|
| 문제 근거 강도 | 5 | 5 | 4 | 4 |
| 데이터 가용성 | 3 | 4 | 3 | 4 |
| 6시간 실현성 | 4 | 4 | 4 | 4 |
| 심사 기준 적합도 | 5 | 5 | 3 | 4 |
| 경쟁 예상 | 2 | 2 | 2 | 2 |
| 합계 | 19 | 20 | 16 | 18 |
| 추천도 | 상 | 상 | 중 | 상 |

추천 1순위는 트랙 B입니다. 서울 상권 데이터가 공공누리 1유형 OpenAPI와 파일로 열려 있고, 서울 소상공인의 폐업 고려 비율이 2022년 14.4%에서 2024년 20.2%로 올랐습니다. [출처: https://data.seoul.go.kr/dataList/OA-15577/S/1/datasetView.do , https://mediahub.seoul.go.kr/archives/2016341] 공지는 대상 예시로 소상공인을 직접 들고, 디지털·스마트 기술을 쓰는 소상공인은 27.2%입니다. 입력을 줄인 서비스가 디지털 포용 점수로 이어집니다. [출처: https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1066231&cbIdx=86] 구름 벚꽃톤 대상도 중장년 소상공인용 AI였습니다. [출처: https://blog.goorm.io/goorm_beotkkotthon/]

추천 2순위는 트랙 A입니다. 문제 근거와 심사 기준 적합도가 가장 높고, 합성 데이터로도 시연이 완결되는 아이디어가 있습니다. 복지 안내 챗봇형 팀이 몰릴 가능성이 커서, 음성 입력과 담당자 연결처럼 시연에서 보이는 차별점이 필요합니다(추정).

트랙 D는 외부 데이터 없이 완성되는 쉬운말 서울이 가장 안전합니다. 다만 자유주제는 시민 체감형 공익 가치와 포용적 AI 방향을 설명해야 하는 부담이 있습니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08] 트랙 C는 핵심 고전24 API가 심사 후 키를 주고, 기본 대상이 일반 구직 청년이라 정보 약자 설계를 따로 만들어야 합니다.

### 5.1 추천 아이디어

| 순위 | 트랙 | 아이디어 | 핵심 장면 | 데이터 |
|---|---|---|---|---|
| 1 | B | 가게 건강검진과 지원금 길잡이 | 큰 버튼 선택, 신호등·음성 안내, 지원사업 연결 | 상권 데이터, 지원사업 표 |
| 2 | A | 말로 찾는 복지 길잡이 | 말로 상황 설명, 쉬운 말 추천, 창구 안내 | 복지서비스 목록 |
| 3 | D | 쉬운말 서울 | 안내문을 네 줄 쉬운 글 카드로 바꾸고 읽어 줌 | 서울시 공개 안내문 |

트랙별 아이디어 전체(트랙마다 4개)와 시연 장면, 위험, 데이터 상세는 11.5, 12.5, 13.5, 14.5절에 있습니다.

## 6. 팀 역할 분담

구름 벚꽃톤은 기획 1, 디자인 1, 프론트엔드 2, 백엔드 2로 팀을 짰습니다. [출처: https://blog.goorm.io/goorm_beotkkotthon/] 이번 대회는 제출물에 기획·기대효과서 PDF와 접근성 시연 발표가 포함되므로 문서 담당을 따로 둡니다.

| 역할 | 6인 팀 | 5인 팀 | 당일 하는 일 |
|---|---|---|---|
| 팀장·기획 | 1명 | 1명(발표 겸임) | 범위 결정, 시간 관리, 심사 기준과 기능 대조 |
| 디자인·접근성 | 1명 | 1명 | 큰 글씨·고대비·음성 안내 점검, 발표 화면 제작 |
| 프론트엔드 | 2명 | 1명 | 화면 구현, 음성 입출력, 배포 |
| 백엔드·데이터·AI | 1명 | 1명 | 공공데이터 호출, LLM 프롬프트, 예비 데이터 |
| 문서·발표 | 1명 | 1명(디자인과 분담) | 기획·기대효과서 PDF, README, 시연 대본 |

## 7. 본선 6시간 일정 초안

본선은 09:00~19:00이고 개발은 6시간입니다. 개발 시작 시각은 공지에 없어, 아래는 개발 시작을 0시간으로 둔 상대 일정입니다. [출처: https://linkareer.com/activity/357358]

| 시간 | 하는 일 | 끝낼 기준 |
|---|---|---|
| 0:00~0:30 | 사전 제출물 피드백 반영, 기능 3개 확정, 저장소 첫 커밋 | 역할별 작업 목록 |
| 0:30~2:30 | 핵심 기능 1 구현, 데이터 호출 확인, 예비 데이터 준비 | 배포 주소에서 핵심 흐름 1회 작동 |
| 2:30~4:00 | 핵심 기능 2·3, 음성·큰 글씨 모드 | 시연 시나리오 끝까지 작동 |
| 4:00~5:00 | 접근성 점검, 모바일 확인, 오류 수정, 기능 동결 | 새 기능 추가 중단 |
| 5:00~5:40 | 기획·기대효과서 PDF, README, 발표자료 마무리 | 제출물 4종 완성 |
| 5:40~6:00 | 시연 리허설 2회, 제출 | 제출 완료 |

기획·문서 담당은 개발 시작부터 문서를 동시에 씁니다. 무료 LLM 한도가 바닥나면 시연이 멈추므로, 미리 저장해 둔 응답으로 전환하는 길을 두 시간 안에 만듭니다. OpenRouter 무료 요금제는 하루 50회 요청으로 제한됩니다. [출처: https://openrouter.ai/pricing/]

## 8. 사전 세미나 전까지 준비할 것

모두 FAQ의 사전 준비 허용 범위 안의 일입니다. 핵심 기능 코드는 쓰지 않습니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

1. 11/8 마감 전에 구글폼으로 신청합니다. 5~6인 팀을 맞추고 구현 인원을 포함합니다.
2. 트랙과 아이디어를 정하고, 문제 정의·사용자 시나리오·발표 구성을 문서로 만듭니다.
3. 와이어프레임과 큰 글씨·고대비 화면안을 그립니다. KWCAG 항목 중 대체 텍스트, 명도 대비, 키보드 사용을 먼저 반영합니다. 상세는 10.6절에 있습니다.
4. 서울 열린데이터광장과 공공데이터포털 인증키를 미리 발급하고, 쓸 API를 한 번씩 호출해 응답 형식을 기록합니다. 고전24 API처럼 심사가 있는 키는 가장 먼저 신청합니다.
5. GitHub 저장소를 만들고, 빈 프로젝트 구조와 배포 환경(Vercel, Cloudflare Pages 등)을 연결합니다. 사전 커밋에는 스캐폴딩과 문서만 넣습니다.
6. 무료 LLM API 키(Gemini, Groq, OpenRouter 중 1~2개)를 받고 계정별 한도를 확인합니다. Gemini 무료 등급은 모든 프로젝트에 주어지지 않습니다. [출처: https://ai.google.dev/gemini-api/docs/troubleshooting]
7. ERD와 데이터 흐름 문서, 기획·기대효과서 PDF 목차를 만듭니다.
8. 11/14 사전 세미나에서 사전 제출 작업물의 제출 방법과 개발 시작 시각, 배점표를 묻습니다. 세 가지 모두 공지에서 확인하지 못했습니다.

## 9. 출처

본문과 표의 URL이 출처입니다. 10~14절의 근거 메모에는 수치마다 출처와 게시일을 달았습니다.

## 10. 부록 공통. 대회·데이터·도구 근거

### 10.1 공식 규칙

대회는 현장에서 작동하는 실용성, 정보 약자도 쉽게 쓰는 디지털 포용, 시민이 체감하는 효과를 핵심 가치와 평가 기준으로 제시합니다. [출처: https://goorm.notion.site/2026-AI-3ec4e6997fb0806ca882d12e501f97c9]

팀은 실제 작동 프로토타입, 서비스 기획 및 기대효과서 PDF, GitHub 소스코드 저장소, 정보 약자 접근성을 반영한 시연 발표자료를 제출합니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

본선 핵심 기능은 당일 코딩해야 합니다. 사전 개발은 커밋 기록 확인을 통해 적발될 수 있으며, 적발 시 실격 처리합니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

사전 준비 범위에는 기획, 디자인, 개발 환경 설정, 보일러플레이트가 포함됩니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

기획에는 문제 정의, 기능 기획, 사용자 시나리오와 발표 자료 구성을 포함합니다. 디자인에는 와이어프레임, UI, 로고 제작이 포함됩니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

환경 설정에는 계정과 GitHub 저장소 준비, 배포 환경 구성, 프레임워크·라이브러리 설치, ERD·파이프라인 문서 작성이 포함됩니다. 빈 프로젝트 구조와 공개 오픈소스·공개 API 활용도 허용합니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

서울시 데이터 사용을 권장하며, 저작권 문제가 없는 다른 공공데이터와 직접 구축한 데이터도 사용할 수 있습니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

참가 대상은 만 19세 이상 만 39세 이하이며 직업 제한은 없습니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

팀은 5~6명으로 구성합니다. [출처: https://linkareer.com/activity/357358]

기획이나 디자인만으로 구성된 팀도 참가할 수 있습니다. 다만 최종 산출물로 작동하는 MVP 제출이 필수이므로 웹이나 앱을 구현할 인원을 포함하는 편이 권장됩니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

모집 기간은 10월 12일부터 11월 8일까지입니다. 사전 세미나는 11월 14일 13시부터 18시까지 구름스퀘어 강남에서 온·오프라인으로 진행합니다. 본선은 11월 21일 9시부터 19시까지 아키스케치 성수에서 열리며 개발 시간은 6시간입니다. [출처: https://linkareer.com/activity/357358]

링커리어 페이지 상단은 접수 시작일을 2026년 10월 16일로 표시하지만, 본문 일정은 10월 12일로 표시합니다. 공식 공고 본문 일정과 목록 표기 사이에 시작일 차이가 있습니다. [출처: https://linkareer.com/activity/357358]

총 시상 규모는 300만 원 상당이며 세부 내역은 추후 공지입니다. [출처: https://linkareer.com/activity/357358]

본선 당일 상위 4팀의 결과를 발표합니다. 시상식은 12월 8일(화) 용산아이파크몰 7층 CGV에서 열릴 예정이며, FAQ는 날짜를 미정으로 표기합니다. 수상팀 대표 1인이 참석해야 합니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

참가팀이 만든 지식재산권은 참가팀에 귀속됩니다. [출처: https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08]

### 10.2 주최·운영 기관과 서울디지털배움터

서울시는 2020년부터 디지털배움터를 운영해 어르신 등 디지털 취약계층의 기초 디지털 역량을 지원했고, 2025년까지 누적 48만 명이 교육을 받았습니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=457102&srchCtgry=474]

서울시는 2026년 사업을 지자체 자율편성으로 전환하고, 서울AI디지털배움터에서 시민 대상 실전형 AI 교육을 추진합니다. 2026년 교육 목표는 시민 10만 명입니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=457102&srchCtgry=474]

서울시는 2026년 10월 27일 보도자료에서 AI디지털배움터 7개 자치구(강동·강서·마포·도봉·동작·성동·구로) 거점의 공간 전환과 조성을 10월에 완료했다고 밝혔습니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=468920] 이 7개 자치구는 거점 수와 다른 집계 단위이므로 센터 수와 직접 합산하지 않습니다.


### 10.3 구름과 공공 해커톤의 지난 수상작과 심사 경향

2024년 구름 벚꽃톤은 IT 기술로 사회문제를 해결하는 행사로 소개됐으며, 전국 35개 대학에서 300여 명이 참여했습니다. 역할별 구성은 기획 1명, 디자인 1명, 프론트엔드 2명, 백엔드 2명으로 안내됐고, 행사 전 약 10일간 기획·개발 기간을 뒀습니다. [출처: https://blog.goorm.io/goorm_beotkkotthon/]

벚꽃톤 대상은 중장년 소상공인이 메뉴 이름·가격·사진을 입력하면 SNS 게시물을 만드는 AI 마케팅 서비스였습니다. 최우수상에는 발표 대본 생성·연습 서비스와 20대 백신 조회·추천 서비스가 포함됐습니다. [출처: https://blog.goorm.io/goorm_beotkkotthon/]

서울 프롬프톤은 2024년 생성형 AI 기반 행정서비스 발굴 행사로 열렸으며, 67개 팀 190명이 참가하고 10개 팀이 시상 대상에 올랐습니다. 대상은 디지털 소외 계층을 위한 음성 기반 버스 예매 서비스 제안이었습니다. [출처: https://mas.smc.seoul.kr/attach/record/SEOUL/appendix/a11/A0068626.pdf?time=20260415224434]

외교부 2025 공공데이터 대회 심사기준에는 공공데이터 활용, AI 혁신성, 독창성, 완성도, 발전 가능성, ESG 혁신 등이 포함됩니다. [출처: https://www.mofa.go.kr/www/brd/m_4075/view.do?seq=369236]

2022 오픈데이터포럼 해커톤 대상은 시각장애인을 위한 점자 지도 생성 도구였습니다. [출처: https://www.odf.or.kr/archive-project/?bmode=view&idx=90843475]

### 10.4 서울 공공데이터 사용법

서울 열린데이터광장 계정을 만든 뒤 인증키를 신청하고, 사용할 서비스의 이용 조건과 호출 제한을 확인합니다. [출처: https://data.seoul.go.kr/together/notice/faqList.do?bbsCd=10002&ditcCd=FAQ02&seq=d47bc57aea53d6c6ab244c05a6eb2259]

서울 API는 기본적으로 GET 요청을 사용하며, 기본 주소는 http://openapi.seoul.go.kr:8088/ 입니다. 서비스별 주소와 요청 항목은 메타데이터에서 확인합니다. [출처: https://data.seoul.go.kr/together/notice/faqList.do?bbsCd=10002&ditcCd=FAQ02&seq=d47bc57aea53d6c6ab244c05a6eb2259]

호출 경로에는 인증키, 응답 형식, 서비스명, 시작·종료 행 번호가 들어갑니다. 응답 형식은 JSON·XML·XLS 중 서비스가 지원하는 형식으로 지정합니다. [출처: https://data.seoul.go.kr/together/notice/faqList.do?bbsCd=10002&ditcCd=FAQ02&seq=d47bc57aea53d6c6ab244c05a6eb2259]

샘플 키는 최초 5건까지만 호출할 수 있고, 일반 호출은 요청당 최대 1,000건입니다. 실시간 지하철 API는 하루 최대 1,000회로 제한됩니다. 서비스마다 별도 제한이 있을 수 있습니다. [출처: https://data.seoul.go.kr/together/guide/useGuide.do]

브라우저에서 교차 출처 호출이 항상 허용된다는 공식 보장은 확인되지 않았습니다. 브라우저 직접 호출에서 CORS 오류가 나면 서버 측에서 API를 호출하는 구조를 사용하고, 선택한 서비스로 실제 요청을 확인합니다. [출처: https://data.seoul.go.kr/together/guide/useGuide.do]

### 10.5 무료 AI·배포 도구

무료 한도는 2026년 10월 28일 확인한 제공사 공개 자료 기준입니다. 무료 제공 여부와 한도는 계정·모델·서비스별로 달라질 수 있습니다. [출처: https://ai.google.dev/gemini-api/docs/pricing]

| 도구 | 무료 한도 | 키 발급 | 확인 날짜 | URL |
|---|---|---|---|---|
| Gemini API | 일부 모델 입력·출력 토큰 무료, 모델별 제한은 AI Studio에서 확인 | Google AI Studio에서 키 생성 | 2026-10-28 | https://ai.google.dev/gemini-api/docs/pricing |
| Groq API | GPT-OSS-20B 예시 한도는 개발자 플랜 기준: 분당 30회, 일 1,000회, 분당 8천 토큰. 무료 한도는 계정별 Limits 페이지에서 확인 | Groq 콘솔에서 API 키 생성 | 2026-10-28 | https://console.groq.com/docs/rate-limits |
| OpenRouter | 무료 모델 요청 일 50회, 분당 20회; 모델 제공자별 제한 별도 적용 | OpenRouter 계정에서 키 생성 | 2026-10-28 | https://openrouter.ai/pricing/ |
| Cloudflare Workers AI | 매일 10,000 Neurons 무료 할당량 | Cloudflare 대시보드에서 계정 토큰 설정 | 2026-10-28 | https://developers.cloudflare.com/workers-ai/platform/pricing/ |
| Upstage API | 가입 시 10달러 크레딧 제공 | 콘솔 API keys에서 키 생성 | 2026-10-28 | https://console.upstage.ai/docs/getting-started |
| Vercel Hobby | 무료 플랜, 함수 호출 월 100만 회; 개인·비상업 용도 | Vercel 계정 생성 후 프로젝트 연결 | 2026-10-28 | https://vercel.com/docs/plans/hobby |
| Cloudflare Pages | 월 500회 빌드, 동시 빌드 1개, 빌드 제한 시간 20분 | Cloudflare 계정에서 Git 저장소 연결 | 2026-10-28 | https://developers.cloudflare.com/pages/platform/limits/ |
| Netlify | 크레딧 기반 무료 플랜은 프로덕션 배포 1회당 15크레딧 | Netlify 계정 생성 후 저장소 연결 | 2026-10-28 | https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/ |
| Render | 무료 웹 서비스는 요청이 15분 없으면 중지되며 재가동에 약 1분 소요 | Render 계정에서 서비스 생성 | 2026-10-28 | https://render.com/docs/free |
| Supabase | 무료 데이터베이스 프로젝트당 500MB, 비활성 1주 후 일시 중지 | Supabase 프로젝트 설정에서 API 키 확인 | 2026-10-28 | https://supabase.com/pricing |
| Firebase Spark | 무료 요금제, 결제수단 등록 불필요 | Firebase 콘솔에서 프로젝트 생성 | 2026-10-28 | https://firebase.google.com/pricing |

### 10.6 정보 약자 접근성 기준

심사 시연에서는 핵심 과업을 키보드만으로 완료하고, 현재 초점 위치가 화면에 분명히 보이는지 확인할 수 있습니다. 한국형 웹 콘텐츠 접근성 지침은 웹 기능의 키보드 사용을 요구합니다. [출처: https://a11ykr.github.io/kwcag22/]

상태나 선택 결과는 색상만으로 구분하지 않고 글자·아이콘 등으로 함께 표시합니다. 입력 오류가 나면 오류 위치와 원인을 안내하고, 수정 방법을 제공합니다. [출처: https://a11ykr.github.io/kwcag22/]

버튼과 입력 영역은 충분한 크기로 만들고, 글자 크기와 줄 간격을 조절할 수 있게 합니다. 제어 요소의 대각선 길이 6밀리미터 이상은 지침의 권고 사항입니다. [출처: https://a11ykr.github.io/kwcag22/]

키오스크형 화면은 단계 수를 줄이고 쉬운 단어를 사용하며, 화면 구조와 조작 방식을 일관되게 유지합니다. NIA는 기기별 UI 가이드와 리소스를 제공하고 쉬운 언어 사용 지침을 안내합니다. [출처: https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=27275&cbIdx=90549]

음성 기능이 없어도 같은 과업을 완료할 수 있도록 텍스트 입력·읽기 경로를 제공합니다. 브라우저 음성 인식은 지원 여부와 개인정보 처리 방식이 환경별로 다르므로 대체 입력 경로를 함께 시연합니다. [출처: https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition]

### 10.7 출처

- 공식 대회 안내 및 FAQ: https://goorm.notion.site/2026-AI-3ec4e6997fb0806ca882d12e501f97c9, https://goorm.notion.site/FAQ-3ec4e6997fb0806bafedff5e0ab0ba08
- 모집 일정과 운영 표기: https://linkareer.com/activity/357358
- 구름·공공 해커톤 사례와 심사 기준: https://blog.goorm.io/goorm_beotkkotthon/, https://mas.smc.seoul.kr/attach/record/SEOUL/appendix/a11/A0068626.pdf?time=20260415224434, https://mas.smc.seoul.kr/attach/record/SEOUL/appendix/a11/A0070091.pdf?time=20260416043212, https://www.mofa.go.kr/www/brd/m_4075/view.do?seq=369236
- 서울디지털배움터와 운영기관: https://www.seoul.go.kr/news/news_report.do?nttNo=457102&srchCtgry=474, https://www.seoul.go.kr/news/news_report.do?nttNo=468920
- 서울 공공데이터: https://data.seoul.go.kr/together/guide/useGuide.do, https://data.seoul.go.kr/together/notice/faqList.do?bbsCd=10002&ditcCd=FAQ02&seq=d47bc57aea53d6c6ab244c05a6eb2259
- 무료 도구 공식 문서: https://ai.google.dev/gemini-api/docs/pricing, https://console.groq.com/docs/rate-limits, https://openrouter.ai/pricing/, https://developers.cloudflare.com/workers-ai/platform/pricing/, https://console.upstage.ai/docs/getting-started, https://vercel.com/docs/plans/hobby, https://developers.cloudflare.com/pages/platform/limits/, https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/, https://render.com/docs/free, https://supabase.com/pricing, https://firebase.google.com/pricing
- 접근성 기준: https://a11ykr.github.io/kwcag22/, https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=27275&cbIdx=90549, https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition

## 11. 부록 A. 트랙 A 돌봄과 복지 근거

### 11.1 서울의 실제 문제 현황과 수치

- 2023년 기준 서울 1인가구는 약 163만 가구로, 전체 가구 414만 가구의 39.3%를 차지합니다. [출처: https://news.seoul.go.kr/welfare/archives/569422] (2025-05-19 게시)
- 서울시는 2024년 기준 전체 416만 가구 중 1인가구가 약 166만 가구이며, 비율은 39.9%라고 제시합니다. [출처: https://news.seoul.go.kr/welfare/archives/577951]
- 같은 2024년 기준으로 2024 서울서베이는 1인가구 비율을 39.3%로 적습니다. [출처: https://mediahub.seoul.go.kr/archives/2014052] (2025-04-14 기재)
- 2024 서울서베이에서 1인가구의 연령 구성은 60세 이상 40.6%, 20~30대 34.9%, 40~50대 24.5%입니다. [출처: https://mediahub.seoul.go.kr/archives/2014052] (2025-04-14 기재)
- 2024 서울서베이에서 1인가구가 어렵다고 답한 항목의 점수는 균형 잡힌 식사 4.79점, 아프거나 위급할 때 대처 4.71점, 가사 4.69점, 외로움 4.43점입니다. [출처: https://mediahub.seoul.go.kr/archives/2014052] (2025-04-14 기재)
- 2025년 서울 고령인구(65세 이상)는 184.3만 명이고 비율은 19.9%입니다. 2015년 120.1만 명보다 53.5% 늘었습니다. [출처: https://data.si.re.kr/smr/smr2025/reports/SMR2025_01_POPULATION_SI.html] (2025 리포트, 게시일 미기재)
- 2025년 고령인구 비율은 강북구 25.9%, 도봉구 25.3%, 중랑구 22.7%로 높고, 강남구 16.7%, 마포구 16.8%로 낮습니다. [출처: https://data.si.re.kr/smr/smr2025/reports/SMR2025_01_POPULATION_SI.html] (2025 리포트, 게시일 미기재)
- 2020~2024년 서울 1인가구는 연평균 4.54% 늘어 전체 가구 증가율 1.09%를 웃돌았습니다. [출처: https://data.si.re.kr/smr/smr2025/trends/TIS2025_02_HOUSEHOLD.html] (2025 리포트, 게시일 미기재)
- 2023~2024년 1인가구 증가율은 2.05%로, 과거 평균의 절반 수준까지 낮아졌습니다. [출처: https://data.si.re.kr/smr/smr2025/trends/TIS2025_02_HOUSEHOLD.html] (2025 리포트, 게시일 미기재)
- 2024년 기준 부모와 함께 사는 중장년 인구는 32.9만 명입니다. [출처: https://data.si.re.kr/smr/smr2025/trends/TIS2025_02_HOUSEHOLD.html] (2025 리포트, 게시일 미기재)
- 2024년 전국 고독사 사망자는 3,924명으로, 2023년 3,661명보다 늘었습니다. [출처: https://www.mohw.go.kr/board.es?act=view&bid=0027&list_no=1488039&mid=a10503010100&nPage=1&tag=] (2025-11-27 게시, 전국 값)
- 같은 실태조사에서 50대와 60대 남성이 고독사에 특히 취약하고, 여관·모텔과 고시원에서의 발생 비중은 최근 5년간 늘었습니다. [출처: https://www.mohw.go.kr/board.es?act=view&bid=0027&list_no=1488039&mid=a10503010100&nPage=1&tag=] (2025-11-27 게시, 전국 값)
- 2023년 혼자 사는 고령자 가구는 213만 8천 가구이고, 이 중 18.7%는 도움받을 사람이 없습니다. [출처: https://mods.go.kr/board.es?act=view&bid=10820&list_no=432917&mainXml=Y&mid=a10301010000] (2024 고령자통계 보도자료, 전국 값)
- 65세 이상 고령자의 74.0%는 인터넷을 이용하고, 93.9%는 인스턴트 메신저를 이용합니다. [출처: https://mods.go.kr/board.es?act=view&bid=10820&list_no=432917&mainXml=Y&mid=a10301010000] (2024 고령자통계 보도자료, 전국 값)
- 2025년 디지털 정보격차 실태조사에서 디지털 취약계층의 디지털정보화 수준은 일반 국민 대비 77.9%입니다. 같은 해 8개 업종 1,000개 웹사이트의 접근성 평균 점수는 70.4점입니다. 2024년 조사값은 77.5%, 66.7점이었습니다. [출처: https://eiec.kdi.re.kr/policy/materialView.do?num=278528&pg=&pp=&topic=C] (2026-03-26 발표 재게시, 전국 값)
- 서울시는 고립되거나 은둔한 청년을 약 13만 명으로 추산합니다. [출처: https://english.seoul.go.kr/seoul-policy-archive/seoul-without-loneliness/] (2026-09-21 기준)
- 서울 1인가구의 62.1%가 외로움을 호소합니다. [출처: https://english.seoul.go.kr/seoul-policy-archive/seoul-without-loneliness/] (2026-09-21 기준)
- 2025년 12월 말 기준 서울시 등록장애인은 384,934명입니다. [출처: https://wis.seoul.go.kr/wfs/dhs/reg/policy.do?crtId=PLP01050303]
- 2025년 말 기준 전국 등록장애인은 2,627,761명입니다. [출처: https://www.mohw.go.kr/board.es?act=view&bid=0027&list_no=1490145&mid=a10503010100&nPage=1&tag=] (2026-04-19 작성, 전국 값)
- 서울시는 위기가구를 18개 기관 44종의 빅데이터로 발굴합니다. 신고는 02-120 또는 동주민센터로 받습니다. [출처: https://wis.seoul.go.kr/was/cfs/crisisFamilyInfo.do] (게시일 미기재)
- 복지위기 알림 앱은 2024년 6월 운영을 시작한 뒤 2026년 8월까지 약 2만 9천 건의 요청을 받았습니다. 이 중 약 1만 8천 건을 복지서비스로 연계했습니다. [출처: https://eiec.kdi.re.kr/policy/materialView.do?num=287378] (2026-09-23 보도 재게시, 전국 값)
- 중구는 2024년 복지 사각지대 653가구를 발굴했고, 복지 서비스 783건을 제공했습니다. [출처: https://go.seoul.co.kr/news/newsView.php?id=20250211500041] (2025-02-11 보도)
- 2025년 강동구는 주민등록 사실조사 기간에 19개 동의 복지통장 632명과 복지공동체 인력 1천329명이 위기가구 발굴에 나설 예정이라고 밝혔습니다. [출처: https://www.yna.co.kr/view/AKR20250902030800004]
- 서초구는 2026년 8월 18일부터 10월 16일까지 장기요양 기각·각하자 등 돌봄 고위험군 1,600여 명을 대상으로 발굴 조사를 했습니다. [출처: https://www.seoul.co.kr/news/publicnews/seoul_local/news_seoul/2026/08/12/20260812500184]
- 서울시는 2026년 3월 27일 시행한 서울형 통합돌봄으로 9월 말까지 2만 711명이 신청했고, 1만 4,343명이 6만 9,119건의 서비스를 이용했다고 밝혔습니다. [출처: https://www.newspim.com/news/view/20261021000563]

### 11.2 서울시가 이미 하는 사업과 빈틈

- 서울시는 2022년 1인가구 안심 종합계획을 발표하고, 2022~2025년 4년간 2조 3,545억 원을 투입했습니다. [출처: https://news.seoul.go.kr/welfare/archives/577951] (게시일 미확인)
- 서울시는 2026년 1인가구 정책에 6,316억 원을 투입해 31개 사업을 추진합니다. [출처: https://news.seoul.go.kr/welfare/archives/577951] (게시일 미확인)
- 병원 안심동행은 2025년부터 주 2회 이용에서 월 10회 이용으로 바뀌었습니다. [출처: https://news.seoul.go.kr/welfare/archives/569422] (2025-05-19 게시)
- 병원 안심동행 누적 실적은 7만 1,063건입니다. 2026년에는 건강, 이사, 마음 동행을 묶은 통합 동행서비스로 바뀌며 2만 건 이용을 목표로 합니다. [출처: https://news.seoul.go.kr/welfare/archives/577951] (게시일 미확인)
- 사회적 고립위험가구 전담기구는 2025년 64개소에서 2026년 70개소로 늘어납니다. [출처: https://news.seoul.go.kr/welfare/archives/577951] (게시일 미확인)
- 스마트 안부확인은 2022년부터 누적 8만 3,633명에게 서비스했고, 2026년에는 2만 2,000명을 지원합니다. [출처: https://news.seoul.go.kr/welfare/archives/577951] (게시일 미확인)
- 스마트 안부확인 대상은 7,000가구에서 8,500가구로 늘어납니다. [출처: https://www.sedaily.com/article/20017636] (기사 날짜 미확인)
- 서울시 AI 안부확인은 2025년 11월부터 18개 자치구에서 고독사 저위험군 1,800명을 대상으로 양방향 통화를 시범 운영합니다. [출처: https://news.seoul.go.kr/welfare/archives/574354] (2025-10-21 수정)
- 서울형 통합돌봄 대상은 65세 이상과 65세 미만 심한 장애인으로 한정됩니다. 정신질환자 대상 시범사업도 준비 중입니다. [출처: https://www.newspim.com/news/view/20261021000563] (2026-10-21 보도)
- 고독 120은 2025년 상담 33,148건을 기록했습니다. [출처: https://english.seoul.go.kr/seoul-to-build-a-more-robust-loneliness-prevention-and-care-system-under-the-seoul-no-more-loneliness-initiative-season-2/] (2026-02-12 보도자료, 실적은 2025년 기준)
- 서울잇다 플레이스는 성동구 성수동에 외로움 지휘센터로 세워지며, 2026년 하반기 완공 예정입니다. [출처: https://english.seoul.go.kr/seoul-to-build-a-more-robust-loneliness-prevention-and-care-system-under-the-seoul-no-more-loneliness-initiative-season-2/] (2026-02-12 보도자료)
- 서울마음편의점은 2026년 19개 지역에서 운영 중이며, 서울시는 이를 25개소로 확대한다고 발표했습니다. [출처: https://english.seoul.go.kr/seoul-policy-archive/seoul-without-loneliness/] [출처: https://english.seoul.go.kr/seoul-to-build-a-more-robust-loneliness-prevention-and-care-system-under-the-seoul-no-more-loneliness-initiative-season-2/]
- 빈틈 (추정): 통합돌봄 대상이 65세 이상과 심한 장애인으로 한정되어, 65세 미만 고립 가구는 같은 서비스를 받기 어렵습니다. [출처: https://www.newspim.com/news/view/20261021000563]
- 빈틈 (추정): 자치구마다 서비스 수준이 달라서 표준화 요청이 현장에서 나왔습니다. [출처: https://www.newspim.com/news/view/20261021000563]
- 빈틈 (추정): 발굴 실적은 자치구별로 따로 공개됩니다. 그래서 서울 전체의 발굴 후 연계율은 한눈에 확인하기 어렵습니다. [출처: https://go.seoul.co.kr/news/newsView.php?id=20250211500041] [출처: https://www.yna.co.kr/view/AKR20250902030800004]
- 복지위기 알림 앱은 2026년 8월까지 접수된 도움 요청 약 2만 9천 건 중 약 1만 8천 건(62.1%)을 공공·민간 복지서비스로 연계했습니다. [출처: https://www.yna.co.kr/view/AKR20260923079000530]

### 11.3 기존 민간·공공 서비스와 한계

- 복지로 앱은 복지위기 알림, 이웃 도움요청, 복지시설 검색 기능을 제공합니다. [출처: https://apps.apple.com/kr/app/%EB%B3%B5%EC%A7%80%EB%A1%9C/id490534512] (2024-10-07 리뷰 기준 확인)
- 복지로 앱은 평점 3.8점과 평가 1.4천 개를 표시합니다. 한 리뷰에는 "초기에는 속도나 안정성 문제로 불편함이 있었지만 최근 개선된 점이 눈에 띕니다"라고 적혀 있습니다. [출처: https://apps.apple.com/kr/app/%EB%B3%B5%EC%A7%80%EB%A1%9C/id490534512]
- 국민비서 129 챗봇은 24시간 로그인 없이 쓸 수 있고, 개인정보를 수집하지 않습니다. [출처: https://www.129.go.kr/counsel/counsel04.do] (게시일 미기재)
- 같은 챗봇은 답변이 법적 유권해석이 아니므로 증거자료로 효력이 없을 수 있다고 밝힙니다. [출처: https://www.129.go.kr/counsel/counsel04.do] (게시일 미기재)
- 돌봄SOS는 기준 중위소득 100% 이하 시민에게 서비스 비용을 전액 지원하고, 그 밖의 시민은 자부담합니다. [출처: https://wis.seoul.go.kr/sec/ctg/categoryDetail.do?id=88] (게시일 미표기)
- 돌봄SOS 신청은 주민등록 관할 동주민센터 방문 또는 서울복지포털 온라인으로 합니다. [출처: https://wis.seoul.go.kr/sec/ctg/categoryDetail.do?id=88] (게시일 미표기)
- 서울시는 위기상황 알림, 연락 미수신, 상담 요청이 들어오면 동 복지플래너 상담과 긴급출동으로 대응합니다. [출처: https://www.seoul.go.kr/policy/view.do?id=1056&lan=KO] (게시일 미표기)
- AI 안부확인은 자동 전화로 안부를 묻고 결과를 동주민센터에 전달합니다. 대상자가 직접 신청하는 경로는 확인되지 않았습니다. [출처: https://news.seoul.go.kr/welfare/archives/574354] (2025-10-21 수정)
- 2023년 서울복지재단 조사에서 응답자의 59%가 언제든 전화를 걸 수 있기를 원했습니다. [출처: https://news.seoul.go.kr/welfare/archives/574354] (2025-10-21 수정)
- 서울 AI 안부확인은 25개 자치구 중 18개 구가 도입했습니다. [출처: https://www.munhwa.com/article/11565804] (기사 날짜 미확인)
- 우리동네돌봄단은 주민 1,200명으로 구성됩니다. [출처: https://www.sedaily.com/article/20017636] (기사 날짜 미확인)
- 네이버 CareCall 자체 분석은 도입 지역에서 60세 이상 고독사율 증가폭이 작았다고 밝혔습니다. [출처: https://www.navercorp.com/en/media/naverReportsDetail?seq=10034552] (2026-08-04 기업 발표)
- 이 분석은 기업 자체 분석이므로 독립적인 인과 효과로 보기 어렵다고 추정합니다. [출처: https://www.navercorp.com/en/media/naverReportsDetail?seq=10034552]

### 11.4 쓸 수 있는 공개 데이터·API

| 이름 | 제공 기관 | 제공 형태 | 인증키 | 갱신 주기 | 활용 | URL |
|---|---|---|---|---|---|---|
| 서울시 장애인 등록현황 | 서울시 | 데이터셋 | 미확인 | 매년 | 자치구별 수요 비교 | https://data.seoul.go.kr/dataList/OA-22212/F/1/datasetView.do |
| 노인·장애인 보호구역 | 서울시 | HWPX 파일 | 없음 | 2026-07-15 수정 | 보행 취약 구역 표시 | https://data.seoul.go.kr/dataList/OA-13682/F/1/datasetView.do |
| 서울시 복지서비스 목록 정보 | 한국사회보장정보원 | 목록 조회, 상세 조회 | 미확인 | 미확인 | 서비스 안내 데이터 기초 | https://data.seoul.go.kr/dataList/OA-23013/S/1/datasetView.do |
| 노인복지 생활시설 현황 | 보건복지부 | REST API | 필요 | 연간 | 시설 현황 집계 | https://www.data.go.kr/data/15098829/openapi.do |
| 무더위쉼터 API | 행정안전부 | LINK형 API | 미확인 | 실시간 | 폭염 시 쉼터 안내 | https://www.data.go.kr/data/15138456/openapi.do |
| 장애인 편의시설 설치현황 | 보건복지부 | CSV | 없음 | 5년 주기 | 접근 가능 시설 표시 | https://www.data.go.kr/data/15003356/fileData.do |
| 기초생활수급자 동별 통계 | 서울시 | DB 표, 파일 없음 | 없음 | 매년 12월 | 수급 현황 참고 | https://data.seoul.go.kr/dataList/DT201004O1100342020/S/2/datasetView.do |
| 장애인 거주시설 현황 | 보건복지부 | REST API | 미확인 | 연간 | 시설 입소 현황 | https://www.data.go.kr/data/15098801/openapi.do |
| 서울시 무더위쉼터 CSV | 서울시 | CSV | 없음 | 2021 스냅샷 | 과거 목록, 현황용 부적합 | https://www.data.go.kr/data/15088159/fileData.do |
| 서울시 자치구별 장애인 등록현황 파일 (용산구 예) | 서울특별시 용산구 | 파일 | 해당 없음 | 파일 2026-09-18 | 자치구 단위 비교 | https://www.data.go.kr/data/3077817/fileData.do |
| 교통약자이용정보 API | 서울교통공사 | REST API | 미확인 | 수시 | 엘리베이터, 장애인화장실 등 9종 정보 | https://www.data.go.kr/data/15143843/openapi.do |
| 자치구별 사회복지시설 | 서울시 | 공개 목록 | 없음 | 연 1회 | 시설 위치 기초 자료 | https://opengov.seoul.go.kr/public/list/10496 |

### 11.5 6시간 아이디어 후보

- 아이디어 1. 말해요 복지 (말로 찾는 우리동네 복지 길잡이)
  - 한 줄 요약: 상황을 음성이나 글로 말하면 서울시 복지서비스를 쉬운 말로 골라 주고 신청 창구를 안내하는 웹앱입니다.
  - 대상 사용자: 복지 검색이 어려운 고령자, 1인가구, 장애인과 이들을 돕는 가족이나 주민센터 직원입니다.
  - 핵심 기능: 음성, 글자, 큰 버튼으로 입력받고, LLM이 주제를 분류합니다. 분류 결과로 서비스 목록을 걸러 상위 3개를 큰 글씨 카드로 보여 줍니다. 카드마다 동주민센터, 서울복지포털, 02-120 중 가능한 창구를 안내합니다.
  - 쓰는 데이터: 서울시 복지서비스 목록 정보 [출처: https://data.seoul.go.kr/dataList/OA-23013/S/1/datasetView.do], 돌봄SOS 비용 기준 [출처: https://wis.seoul.go.kr/sec/ctg/categoryDetail.do?id=88], 위기가구 신고 창구 [출처: https://wis.seoul.go.kr/was/cfs/crisisFamilyInfo.do]
  - 6시간 범위: 입력 화면, LLM 분류, 목록 필터링, 카드와 음성 읽기, 배포를 직접 만듭니다. 신청 기능은 만들지 않습니다. 목록 API가 막히면 20~30건의 합성 데이터로 대신합니다.
  - 위험: LLM이 없는 제도를 만들 수 있습니다. LLM은 분류만 하고, 카드 내용은 목록 데이터에서만 가져옵니다.
  - 실현성: 상 (추정). 외부 의존이 적어 합성 데이터로도 시연이 끝까지 됩니다.
  - 차별점: 복지로 앱과 기능이 겹칠 수 있습니다. 음성과 큰 글씨 중심의 입력 흐름으로 차별화합니다 (추정).

- 아이디어 2. 이웃살핌 한 줄 (이웃이 쉽게 알리는 위기 신호 도우미)
  - 한 줄 요약: 이웃의 관찰을 3개 질문에 버튼으로 답하면, 위기 단서를 정리해 신고서 초안과 연락처를 만들어 주는 웹앱입니다.
  - 대상 사용자: 위기 징후를 봤지만 어디에 어떻게 알릴지 모르는 이웃, 경비원, 소규모 상점 주인입니다.
  - 핵심 기능: 누가, 어떤 모습인지, 얼마나 오래인지 3개 질문에 답합니다. LLM이 관찰을 사실 문장으로 정리하고, 긴급도 3단계를 제안합니다. 신고서 초안, 02-120과 동주민센터 연락 안내, 실명과 익명 선택을 제공합니다.
  - 쓰는 데이터: 서울시 위기가구 발굴 안내 [출처: https://wis.seoul.go.kr/was/cfs/crisisFamilyInfo.do], 복지위기 알림 앱 실적 [출처: https://eiec.kdi.re.kr/policy/materialView.do?num=287378], 고독사 취약 집단 통계 [출처: https://www.mohw.go.kr/board.es?act=view&bid=0027&list_no=1488039&mid=a10503010100&nPage=1&tag=]
  - 6시간 범위: 질문 흐름, 요약과 긴급도 제안, 신고서 초안, 복사 기능, 배포를 직접 만듭니다. 실제 접수는 하지 않습니다. 데모 입력은 모두 가상 사례입니다.
  - 위험: 긴급도 판단이 틀릴 수 있습니다. 위급 키워드는 규칙으로 먼저 119와 112 안내를 띄웁니다. [출처: https://www.mois.go.kr/frt/sub/a06/b10/emergencycall/screen.do] 이름과 주소 입력란은 만들지 않습니다.
  - 실현성: 상 (추정). 화면 4개와 LLM 호출 1개로 구성됩니다.
  - 차별점: 복지위기 알림 앱은 이웃 신고와 실명, 익명 선택을 이미 제공합니다. 이 아이디어는 무엇을 위기 신호로 볼지 모르는 사람을 돕는 질문 안내에 집중합니다 (추정).

- 아이디어 3. 안부 한마디 (AI 안부 전화 연습장과 인수인계 요약)
  - 한 줄 요약: 고령자가 안부 전화 질문에 답하는 연습을 하고, AI가 답변에서 건강, 식사, 외로움 신호를 찾아 담당자용 한 줄 요약을 만드는 웹 시연입니다.
  - 대상 사용자: 혼자 사는 고령자와 동주민센터 복지플래너입니다.
  - 핵심 기능: 질문 3개를 음성과 큰 자막으로 읽어 줍니다. 버튼 또는 음성으로 답하면 LLM이 신호를 표시합니다. 담당자 화면에 확인 필요 목록과 한 줄 요약을 보여 줍니다.
  - 쓰는 데이터: 서울시 AI 안부확인 정책 [출처: https://news.seoul.go.kr/welfare/archives/574354], 대상자 요구 조사 [출처: https://news.seoul.go.kr/welfare/archives/574354], 서울시 대응 체계 [출처: https://www.seoul.go.kr/policy/view.do?id=1056&lan=KO]
  - 6시간 범위: 질문 흐름, 음성 읽기, 답변 입력, 신호 분류, 담당자 요약 화면, 배포를 직접 만듭니다. 실제 전화 발신과 통신, 전력 데이터 연동은 하지 않습니다. 담당자 목록은 가상 어르신 5명의 합성 데이터입니다.
  - 위험: 서울시 사업과 겹쳐 보일 수 있습니다. 1,800명 시범 밖에서 연습하는 도구와 담당자 요약 형식을 제안하는 보완 사업으로 설명합니다 (추정). CareCall 수치는 효과 근거로 쓰지 않습니다.
  - 실현성: 중 (추정). 브라우저 음성 입출력 호환성 점검이 필요합니다.
  - 차별점: 서울시 AI 안부확인은 자동 전화 후 동주민센터에 전달하는 구조입니다. 이 아이디어는 답변 연습 흐름과 담당자 요약 화면에 집중합니다 (추정).

- 아이디어 4. 갈 수 있는 곳 지도 (접근 가능 쉼터와 시설 지도)
  - 한 줄 요약: 휠체어를 쓰는 사람과 보행이 불편한 어르신이 갈 수 있는 시설만 걸러서 보는 큰 글씨 지도입니다.
  - 대상 사용자: 장애인, 거동이 불편한 고령자, 이들과 함께 이동하는 가족과 활동지원인입니다.
  - 핵심 기능: 엘리베이터, 장애인화장실 같은 조건 토글을 제공합니다. 조건에 맞는 시설과 무더위쉼터를 지도에 표시합니다. 시설을 누르면 주소, 편의 정보, 전화 연결을 보여 줍니다.
  - 쓰는 데이터: 교통약자이용정보 API [출처: https://www.data.go.kr/data/15143843/openapi.do], 장애인 편의시설 설치현황 [출처: https://www.data.go.kr/data/15003356/fileData.do], 무더위쉼터 API [출처: https://www.data.go.kr/data/15138456/openapi.do]
  - 6시간 범위: 지도 화면, 조건 토글, 상세 카드, 데이터 정제, 배포를 직접 만듭니다. 길찾기와 실시간 고장 정보는 만들지 않습니다.
  - 위험: 좌표가 없는 시설이 많을 수 있습니다. 무더위쉼터 CSV는 2021년 스냅샷이므로 API를 우선합니다. [출처: https://www.data.go.kr/data/15088159/fileData.do]
  - 실현성: 중 (추정). 화면은 단순하지만 데이터 정제 시간이 변수입니다.
  - 차별점: 복지로 앱에서 접근성 조건으로 시설을 거르는 기능은 확인하지 못했습니다. 이 아이디어는 접근성 조건 필터와 무더위쉼터 정보를 한 지도에 모읍니다 (추정).

### 11.6 트랙 추천도

| 항목 | 점수 (5점 만점) | 근거 |
|---|---|---|
| 문제 근거 강도 | 5 | 서울시 자료의 1인가구 166만 가구, 39.9% (2024) [출처: https://news.seoul.go.kr/welfare/archives/577951], 전국 고독사 3,924명 (2024) [출처: https://www.mohw.go.kr/board.es?act=view&bid=0027&list_no=1488039&mid=a10503010100&nPage=1&tag=] |
| 데이터 가용성 | 3 | 복지서비스 목록, 시설, 접근성 데이터는 있습니다. 개인 단위 고독사 위험도나 대상자 연락처는 개방되어 있지 않습니다 [출처: https://data.seoul.go.kr/dataList/DT201004O1100342020/S/2/datasetView.do]. |
| 6시간 실현성 | 4 | 아이디어 1, 2는 합성 데이터로도 시연이 끝납니다 (추정). |
| 심사 기준 적합도 | 5 | 고령자, 1인가구, 장애인 대상이라 이 트랙의 문제와 직접 맞습니다 (추정). |
| 경쟁 예상 | 2 | 복지 안내형 앱이 많을 것으로 추정합니다. 차별은 시연 완성도에서 갈릴 것입니다 (추정). |

전체 등급은 상입니다. 문제 근거와 심사 기준 적합도가 높고, 아이디어 1과 2는 6시간 안에 끝까지 작동하는 시연을 만들기 쉽습니다. 다만 경쟁이 몰릴 가능성이 가장 큰 약점이므로, 음성 입력이나 질문 안내처럼 차별점을 시연에서 분명히 보여 주는 안을 고르는 편이 좋습니다.

### 11.7 출처

1. https://news.seoul.go.kr/welfare/archives/569422
2. https://news.seoul.go.kr/welfare/archives/577951
3. https://mediahub.seoul.go.kr/archives/2014052
4. https://data.si.re.kr/smr/smr2025/reports/SMR2025_01_POPULATION_SI.html
5. https://data.si.re.kr/smr/smr2025/trends/TIS2025_02_HOUSEHOLD.html
6. https://www.mohw.go.kr/board.es?act=view&bid=0027&list_no=1488039&mid=a10503010100&nPage=1&tag=
7. https://mods.go.kr/board.es?act=view&bid=10820&list_no=432917&mainXml=Y&mid=a10301010000
8. https://eiec.kdi.re.kr/policy/materialView.do?num=264828&pg=&pp=&topic=O
9. https://english.seoul.go.kr/seoul-policy-archive/seoul-without-loneliness/
10. https://www.mohw.go.kr/board.es?act=view&bid=0027&list_no=1490145&mid=a10503010100&nPage=1&tag=
11. https://wis.seoul.go.kr/was/cfs/crisisFamilyInfo.do
12. https://eiec.kdi.re.kr/policy/materialView.do?num=287378
13. https://go.seoul.co.kr/news/newsView.php?id=20250211500041
14. https://www.yna.co.kr/view/AKR20250902030800004
15. https://www.seoul.co.kr/news/publicnews/seoul_local/news_seoul/2026/08/12/20260812500184
16. https://www.newspim.com/news/view/20261021000563
17. https://www.sedaily.com/article/20017636
18. https://news.seoul.go.kr/welfare/archives/574354
19. https://english.seoul.go.kr/seoul-to-build-a-more-robust-loneliness-prevention-and-care-system-under-the-seoul-no-more-loneliness-initiative-season-2/
20. https://apps.apple.com/kr/app/%EB%B3%B5%EC%A7%80%EB%A1%9C/id490534512
21. https://www.129.go.kr/counsel/counsel04.do
22. https://wis.seoul.go.kr/sec/ctg/categoryDetail.do?id=88
23. https://www.seoul.go.kr/policy/view.do?id=1056&lan=KO
24. https://www.munhwa.com/article/11565804
25. https://www.navercorp.com/en/media/naverReportsDetail?seq=10034552
26. https://data.seoul.go.kr/dataList/OA-22212/F/1/datasetView.do
27. https://data.seoul.go.kr/dataList/OA-13682/F/1/datasetView.do
28. https://data.seoul.go.kr/dataList/OA-23013/S/1/datasetView.do
29. https://www.data.go.kr/data/15098829/openapi.do
30. https://www.data.go.kr/data/15138456/openapi.do
31. https://www.data.go.kr/data/15003356/fileData.do
32. https://data.seoul.go.kr/dataList/DT201004O1100342020/S/2/datasetView.do
33. https://www.data.go.kr/data/15098801/openapi.do
34. https://www.data.go.kr/data/15088159/fileData.do
35. https://www.data.go.kr/data/3077817/fileData.do
36. https://www.data.go.kr/data/15143843/openapi.do
37. https://opengov.seoul.go.kr/public/list/10496

## 12. 부록 B. 트랙 B 소상공인 근거

### 12.1 서울의 실제 문제 현황과 수치

- 2024년 기준 소상공인 경영애로 응답에서 경쟁심화가 61.0%, 원재료비가 49.6%, 상권쇠퇴가 33.5%를 차지했습니다. [출처: https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1066231&cbIdx=86]
- 2024년 기준 디지털·스마트 기술을 활용하는 소상공인은 27.2%이며, 전년보다 9.2%p 증가했습니다. [출처: https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1066231&cbIdx=86]
- 2022년부터 2024년까지 서울 소상공인의 폐업 고려 비율은 14.4%에서 20.2%로 증가했습니다. 2024년 폐업 이유는 경기침체 29.7%, 매출부진 23.4%였습니다. [출처: https://mediahub.seoul.go.kr/archives/2016341]
- 2024년 서울의 신규 사업자는 22.6만 명, 폐업 사업자는 19.6만 명입니다. [출처: https://data.si.re.kr/smr/smr2025/reports/SMR2025_03_INDECON_SI.html]
- 2023년 전국 기업체당 매출액은 1억 9,900만 원, 영업이익은 2,500만 원입니다. 이 통계는 전국 소상공인 잠정결과입니다. [출처: https://www.bizinfo.go.kr/biz/biza/selectBIZA200Detail.do?policyNewsId=83802]
- 2026년 3월 13일 발표 기준 소상공인 기업체는 613만 개, 종사자는 961만 명입니다. 2024년 기준 조사에서 디지털·스마트 기술 활용 비중도 27.2%로 집계됐습니다. [출처: https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1066231&cbIdx=86]
- 2026년 9월 조사에서 전통시장 체감 BSI는 92.1로 전월보다 35.1포인트 상승했습니다. [출처: https://www.newsis.com/view/NISX20260930_0003808987]

### 12.2 서울시가 이미 하는 사업과 빈틈

- 서울시는 2026년에 315억 원을 투입해 소상공인 2만 4천여 명을 지원하고, 4개 분야 8개 사업을 상시 신청 방식으로 운영한다고 발표했습니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=452037]
- 서울시 상권분석서비스는 2026년 3월 31일 발표 기준 서울의 1,650개 상권과 100개 생활밀접업종 정보를 제공합니다. 유동인구, 점포 수, 평균매출을 확인하고 자가진단을 할 수 있습니다. [출처: https://scpm.seoul.go.kr/seoul-policy/evt0253]
- 서울시는 2026년 3월 31일 상권분석서비스 개편을 발표하며 챗봇과 자가진단 도입을 예정했고, AI 기반 분석은 2027년에 추진한다고 밝혔습니다. [출처: https://scpm.seoul.go.kr/seoul-policy/evt0253]
- 서울시 지원 페이지에는 창업 전 상권·입지 분석과 사업계획서 컨설팅, 자영업 클리닉 37개 분야가 안내되어 있습니다. [출처: https://news.seoul.go.kr/economy/small-business-supports]
- 서울시는 2026년 위기 소상공인 선제지원에서 경영개선 비용을 최대 300만 원 지원한다고 안내합니다. 2026년 2월 11일 발표는 금융자료로 위기 징후를 찾고 3천 명을 조기 발굴한다고 밝혔습니다. [출처: https://news.seoul.go.kr/economy/archives/567673]
- 온라인 신청이 어려운 소상공인은 서울신용보증재단 영업점에서 일대일 상담을 받을 수 있습니다. [출처: https://love.seoul.go.kr/articles/10311]
- 2026년 6월 15일 서울시 발표에서 지원 참여업체는 1년 뒤 매출액이 4.8% 증가했고, 금융지원만 받은 업체보다 증가율이 2.9%p 높았습니다. 폐업률은 비교 업체보다 2.1%p 낮았습니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=459714&srchCtgry=464]

### 12.3 기존 민간·공공 서비스와 한계

- 소상공인365는 2024년 12월 31일 발표 기준 공공·민간 데이터 64개를 22종으로 융합하고, 상권분석·경영진단·핫트렌드·정책정보 서비스를 제공합니다. [출처: https://www.mss.go.kr/common/board/Download.do?bcIdx=1055566&cbIdx=86&streFileNm=0fca561e-2efe-47d0-b3e0-8450c98a5ba8.pdf]
- 2025년 2월 기준 소상공인365는 서울의 100개 생활밀접업종 중 76개를 다뤘습니다. 자료원과 갱신 주기, 점포 기준이 서울시 상권분석서비스와 다를 수 있습니다. [출처: https://korea.nabo.go.kr/board/file/down.do?fid=33318912]
- 서울시 Talk는 2026년 10월 12일 수정 페이지 기준 8개 분야 약 500종의 행정정보를 안내합니다. 소상공인 전문 진단은 안내 범위에 포함되지 않습니다. [출처: https://news.seoul.go.kr/gov/archives/511223]
- 네이버 스마트플레이스 AI 리뷰 통계는 2025년 12월 23일 시작한 베타 서비스로, 음식점 사업자가 대상이며 리뷰 분석은 이틀 전 등록분을 기준으로 합니다. [출처: https://smartplace.naver.com/notices/945]
- 민간 소상공인 통합 서비스는 2026년 10월 28일 확인 페이지에서 배달·지도 플랫폼 5곳 리뷰 통합과 매출 통합 조회를 홍보합니다. 해당 내용은 업체의 서비스 설명입니다. [출처: https://sosanghi.com/]
- 상권정보의 개·폐업 흐름은 참고 지표입니다. 서울시 서비스는 2026년 10월 28일 확인 페이지에서 정보의 정확성이나 신뢰성을 보증하지 않는다고 안내합니다. [출처: https://golmok.seoul.go.kr/introduce1.do]

### 12.4 쓸 수 있는 공개 데이터·API

| 이름 | 제공 기관 | 제공 형태 | 인증키 | 갱신 주기 | 활용 | URL |
|---|---|---|---|---|---|---|
| 서울시 상권분석서비스 점포-상권 | 서울신용보증재단 | OpenAPI, CSV, ZIP | 필요 | 연간 | 점포 수, 개업·폐업 수와 비율을 상권별로 비교합니다. | https://data.seoul.go.kr/dataList/OA-15577/S/1/datasetView.do |
| 서울시 상권분석서비스 추정매출-상권 | 서울신용보증재단 | OpenAPI, 파일 | 필요 | 분기별 | 상권 추정매출과 분기 변화를 확인합니다. 2024년부터 표준단위구역 기준이며, 2026년 7월 3일부터 2021년 이후 자료를 제공합니다. | https://data.seoul.go.kr/dataList/OA-15572/A/1/datasetView.do |
| 서울시 상권변화지표 | 서울신용보증재단 | OpenAPI, 파일 | 필요 | 페이지에 별도 주기 미표기 | 평균 영업기간 기반 네 유형으로 상권 변화를 비교합니다. | https://data.seoul.go.kr/dataList/OA-15576/A/1/datasetView.do |
| 서울시 상권영역 경계 | 서울신용보증재단 | OpenAPI, ZIP | 필요 | 페이지에 별도 주기 미표기 | 상권 경계를 지도에 표시합니다. 좌표계는 EPSG:5181입니다. | https://data.seoul.go.kr/dataList/OA-15560/S/1/datasetView.do |
| 서울시 상권배후지 추정매출 | 서울신용보증재단 | OpenAPI, 파일 | 필요 | 월간 | 배후지의 원 단위 추정매출을 확인합니다. | https://data.seoul.go.kr/dataList/OA-15573/S/1/datasetView.do |
| 소상공인 상가정보 | 소상공인시장진흥공단 | REST API, JSON·XML | 필요 | 실시간 | 상호, 주소, 업종, 경도·위도를 이용해 주변 업종 점포를 셉니다. | https://www.data.go.kr/data/15012005/openapi.do |
| 서울시 추정매출-행정동 | 서울시 | CSV | 불필요 | 페이지에 별도 주기 미표기 | 행정동·업종별 매출과 거래 건수, 요일·성별·연령별 매출을 비교합니다. | https://www.data.go.kr/data/15147235/fileData.do |
| 서울시 업체현황 종사자수 통계 | 서울시 | CSV | 불필요 | 매년 | 구·동·산업대분류별 사업체 수와 종사자 수를 확인합니다. | https://www.data.go.kr/data/15146304/fileData.do |

### 12.5 6시간 아이디어 후보

#### 1. 사장님 가게 건강검진

- 한 줄 요약: 동네와 업종을 고르면 상권의 폐업 흐름과 매출 추이를 쉬운 문장, 신호등, 음성으로 안내합니다.
- 대상 사용자: 디지털 기기에 익숙하지 않은 고령 사장님, 1인 사업자, 폐업을 고민하는 소상공인입니다.
- 핵심 기능: 자치구·동네·업종 선택, 개·폐업률과 추정매출 요약, 쉬운 말 설명과 읽어 주기, 상담 경로 안내입니다.
- 데이터: 서울시 점포-상권, 추정매출-상권, 상권변화지표, 상권영역 경계 데이터입니다.
- 6시간 구현 범위: 선택 화면, 신호등 카드, 서버 API 호출, 단순 집계, 문장 생성, 음성 안내를 구현합니다. 지도는 목록으로 대체하고 차트와 상담처는 간단한 정적 자료로 구성합니다.
- 시연: 마포구 카페를 선택하고 비교 결과와 근거 분기를 확인한 뒤 상담 안내를 엽니다.
- 심사 포인트: 서울 공공데이터를 즉시 조회하고 큰 버튼과 음성으로 디지털 접근을 돕습니다.
- 위험과 대응: 데이터 공간 단위와 갱신 주기가 다르므로 같은 분기와 상권 코드만 비교합니다. 인증키를 사전 발급하고 결과를 캐시합니다.
- 실현 가능성: 상. 단일 데이터 출처와 세 화면 안팎으로 구현할 수 있습니다.
- 차별점: 분석 지표 나열 대신 한 장 요약과 음성 안내를 제공합니다.

#### 2. 지원금 길잡이

- 한 줄 요약: 다섯 가지 예·아니요 질문으로 현재 확인할 지원사업과 준비할 일을 안내합니다.
- 대상 사용자: 지원사업을 찾기 어렵거나 신청 과정에 어려움을 겪는 고령 사장님, 1인 사업자, 소상공인입니다.
- 핵심 기능: 5문항 선택, 규칙 기반 사업 추천, 서류·방문 안내 체크리스트와 인쇄용 요약입니다.
- 데이터: 서울시 공식 지원사업을 정리한 정적 표를 사용하며 인증키는 필요하지 않습니다.
- 6시간 구현 범위: 질문 흐름, 추천 규칙, 카드, 체크리스트, 인쇄 화면, 읽어 주기를 구현합니다. 신청은 공식 사이트로 연결합니다.
- 시연: 다섯 문항에 답하고 지원 카드와 오늘 할 일 세 가지를 확인해 한 장으로 인쇄합니다.
- 심사 포인트: 입력을 단순화하고 공식 출처와 확인일, 오프라인 상담 경로를 제시합니다.
- 위험과 대응: 지원 조건과 기간이 바뀔 수 있으므로 공식 링크와 확인일을 표시하고 자격을 확정하지 않습니다. 세부 사업은 6건부터 입력합니다.
- 실현 가능성: 상. 외부 API 없이 정적 자료와 규칙으로 작동합니다.
- 차별점: 질문 5개, 추천 결과, 오늘 할 일의 짧은 흐름에 집중합니다.

#### 3. 오늘의 장부 한마디

- 한 줄 요약: 하루 매출을 입력하면 최근 흐름과 동네 같은 업종의 평균을 비교해 다음 행동을 한 문장으로 안내합니다.
- 대상 사용자: 별도 장부를 쓰지 않는 소규모 식당·카페·소매점 사업자입니다.
- 핵심 기능: 큰 숫자 키패드, 7일 추이와 동네 평균 비교, 쉬운 조언과 음성 읽기입니다.
- 데이터: 서울시 추정매출-행정동 CSV와 추정매출-상권배후지 데이터를 씁니다. 데모 매출은 합성 자료입니다.
- 6시간 구현 범위: 키패드, 브라우저 로컬 저장, 차트, 평균 비교, 문장 생성, 읽어 주기를 구현합니다. 음성 입력과 합성 매출 자료는 선택 기능으로 둡니다.
- 시연: 합성 가게 매출을 입력하고 7일 추이, 평균 대비 결과, 오늘의 한마디를 확인합니다.
- 심사 포인트: 가입 없이 큰 키패드로 빠르게 기록하고 결과를 색상 외 텍스트로도 전달합니다.
- 위험과 대응: 월간 평균을 일 단위와 비교하면 오차가 생길 수 있으므로 근사값으로 표시하고 세 단계로 안내합니다.
- 실현 가능성: 중. CSV 정제와 업종·행정동 코드 대응에 시간이 필요합니다.
- 차별점: 매출 플랫폼 연동 없이 숫자 하나를 입력하는 기록 도구입니다.

#### 4. 가게 자리 신호등

- 한 줄 요약: 후보 위치와 업종을 선택하면 주변 같은 업종 점포 수와 폐업 흐름을 보여 줍니다.
- 대상 사용자: 창업이나 이전을 준비하는 예비 창업자와 소규모 사업자입니다.
- 핵심 기능: 지도 위치 선택, 주변 업종 점포 집계, 상권 신호등과 확인 질문 세 가지입니다.
- 데이터: 소상공인 상가정보 API, 서울시 점포-상권, 상권변화지표, 카카오맵 JavaScript SDK를 씁니다.
- 6시간 구현 범위: 지도 클릭, 점포 API 호출, 반경 집계, 간단한 신호등, 질문 생성을 구현합니다. 상권 경계 매칭은 가까운 상권 기준으로 대체합니다.
- 시연: 성수동 후보지를 누르고 카페를 골라 주변 점포와 상권 정보를 확인한 뒤 다른 위치와 비교합니다.
- 심사 포인트: 실제 상가 API와 지도를 활용하며 동네 목록 선택도 제공합니다.
- 위험과 대응: 지도 사용이 어려운 사용자를 위해 목록 입력을 지원합니다. 데이터 출처와 상권 매칭 기준을 화면에 적습니다.
- 실현 가능성: 중. 외부 API와 지도 도메인 설정, 좌표 처리가 필요합니다.
- 차별점: 지표 열람에 그치지 않고 예비 창업자가 확인할 질문을 제공합니다.

### 12.6 트랙 추천도

| 평가 항목 | 점수 | 근거 |
|---|---:|---|
| 문제 근거 강도 | 5/5 | 2024년 경영애로와 디지털 활용 수치, 2022~2024년 폐업 고려 비율이 확인됩니다. [출처: https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1066231&cbIdx=86] [출처: https://mediahub.seoul.go.kr/archives/2016341] |
| 데이터 가용성 | 4/5 | 서울시 상권 데이터가 OpenAPI와 파일로 제공되며, 데이터별 인증과 갱신 주기가 다릅니다. [출처: https://data.seoul.go.kr/dataList/OA-15577/S/1/datasetView.do] |
| 6시간 실현성 | 4/5 | 건강검진과 지원금 안내는 제한된 화면과 단순 집계로 구현할 수 있습니다. |
| 심사 기준 적합도 | 5/5 | 해커톤 평가 기준은 현장 실용성, 디지털 포용 UX, 시민 체감 효과를 제시합니다. [출처: https://goorm.notion.site/2026-AI-3ec4e6997fb0806bafedff5e0ab0ba08] |
| 예상 경쟁도 | 2/5 | 경쟁이 적을수록 높은 점수입니다. 상권 데이터가 풍부하고 서울시가 2026년 AI 분석 도입을 예고해 유사 주제가 나올 가능성은 추정입니다. [출처: https://scpm.seoul.go.kr/seoul-policy/evt0253] |

**종합 추천도: 상**

문제 수치와 공개 데이터가 충분하고, 입력을 단순하게 만든 서비스는 디지털 포용과 시민 체감 효과를 함께 제시할 수 있습니다. 건강검진 결과에서 지원사업 안내로 이어지는 구성이 6시간 구현 범위와 차별성을 함께 확보합니다.

### 12.7 출처

1. https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1066231&cbIdx=86
2. https://mediahub.seoul.go.kr/archives/2016341
3. https://data.si.re.kr/smr/smr2025/reports/SMR2025_03_INDECON_SI.html
4. https://www.bizinfo.go.kr/biz/biza/selectBIZA200Detail.do?policyNewsId=83802
5. https://www.seoul.go.kr/news/news_report.do?nttNo=452037
6. https://scpm.seoul.go.kr/seoul-policy/evt0253
7. https://news.seoul.go.kr/economy/small-business-supports
8. https://news.seoul.go.kr/economy/archives/567673
9. https://love.seoul.go.kr/articles/10311
10. https://www.seoul.go.kr/news/news_report.do?nttNo=459714&srchCtgry=464
11. https://www.mss.go.kr/common/board/Download.do?bcIdx=1055566&cbIdx=86&streFileNm=0fca561e-2efe-47d0-b3e0-8450c98a5ba8.pdf
12. https://korea.nabo.go.kr/board/file/down.do?fid=33318912
13. https://news.seoul.go.kr/gov/archives/511223
14. https://smartplace.naver.com/notices/945
15. https://sosanghi.com/
16. https://golmok.seoul.go.kr/introduce1.do
17. https://data.seoul.go.kr/dataList/OA-15577/S/1/datasetView.do
18. https://data.seoul.go.kr/dataList/OA-15572/A/1/datasetView.do
19. https://data.seoul.go.kr/dataList/OA-15576/A/1/datasetView.do
20. https://data.seoul.go.kr/dataList/OA-15560/S/1/datasetView.do
21. https://data.seoul.go.kr/dataList/OA-15573/S/1/datasetView.do
22. https://www.data.go.kr/data/15012005/openapi.do
23. https://www.data.go.kr/data/15147235/fileData.do
24. https://www.data.go.kr/data/15146304/fileData.do
25. https://www.newsis.com/view/NISX20260930_0003808987
26. https://goorm.notion.site/2026-AI-3ec4e6997fb0806bafedff5e0ab0ba08

## 13. 부록 C. 트랙 C 청년 일자리 근거

### 13.1 서울의 실제 문제 현황과 수치

- 2026년 5월 전국 청년층 인구는 782만 2천 명으로 전년 동월보다 15만 2천 명 줄었습니다. 같은 달 청년 고용률은 43.8%로 전년 동월 대비 2.4%p 떨어졌습니다. [출처: https://mods.go.kr/board.es?act=view&bid=210&list_no=446080&mid=a10301010000] (페이지 게시일 2026-07-23)
- 2026년 5월 졸업 후 취업 경험자 비율은 84.8%로 전년 동월보다 1.6%p 낮아졌습니다. 같은 기간 전공과 매우 일치하는 취업 비율은 27.0%였고, 취업 경험이 있는 청년 졸업자 중 첫 일자리가 임금근로자인 경우 첫 취업까지 평균 11.2개월이 걸렸습니다. [출처: https://www.korea.kr/news/policyNewsView.do?newsId=156771847] (페이지 게시일 2026-07-23)
- 2025년 5월 전국 청년층 고용률은 46.2%, 경제활동참가율은 49.5%, 실업률은 6.6%였습니다. [출처: https://www.mods.go.kr/board.es?act=view&bid=210&list_no=437676&mid=a10301010000&nPage=1] (페이지 게시일 2025-07-24)
- 2025년 5월 기준 졸업 후 첫 일자리를 얻기까지 평균 11.3개월이 걸렸고, 고졸 이하는 1년 4.5개월, 대졸 이상은 8.8개월이 걸렸습니다. [출처: https://www.mods.go.kr/board.es?act=view&bid=210&list_no=437676&mid=a10301010000&nPage=1] (페이지 게시일 2025-07-24)
- 2025년 5월 재학 또는 휴학 중 직장 체험 경험이 있는 청년층 비율은 43.2%였습니다. [출처: https://www.mods.go.kr/board.es?act=view&bid=210&list_no=437676&mid=a10301010000&nPage=1] (페이지 게시일 2025-07-24)
- 2025년 5월 비경제활동 인구 중 취업시험 준비자 비율은 14.5%였고, 준비 분야는 일반기업체 36.0%, 일반직 공무원 18.2%, 기능분야 자격증 및 기타 17.8%였습니다. [출처: https://www.mods.go.kr/board.es?act=view&bid=210&list_no=437676&mid=a10301010000&nPage=1] (페이지 게시일 2025-07-24)
- 2025년 8월 15~29세 쉬었음 인구는 44.6만 명이었고, 이 연령대에서 원하는 일자리를 찾기 어려워서 쉬는 응답은 34.1%였습니다. [출처: https://www.kostat.go.kr/boardDownload.es?bid=210&list_no=439131&seq=5] (보도자료 2025-11-05)
- 전체 쉬었음 인구 중 원하는 일자리를 찾기 어려워서 쉬는 사유 비율은 2024년 8월 17.9%에서 2025년 8월 19.0%로 1.1%p 올랐습니다. [출처: https://www.kostat.go.kr/boardDownload.es?bid=210&list_no=439131&seq=5] (보도자료 2025-11-05)
- 가장 최근인 2026년 9월 15~29세 쉬었음 인구는 36만 4천 명으로 전년 같은 달보다 4만 4천 명(10.9%) 줄었습니다. 쉬는 이유 34.1%는 2025년 8월 부가조사 값이라 이 인원에 곱하지 않습니다. [출처: https://mods.go.kr/board.es?act=view&bid=210&list_no=447479&mid=a10301010000] (2026년 9월 고용동향, 2026-10-16 발표, 18쪽 표)
- 2026년 7월 청년(15~29세) 쉬었음 인구는 36만 7천 명으로 전년 동기보다 6만 9천 명, 15.8% 줄었습니다. 2025년 8월 수치와 기간이 달라 두 값은 함께 쓰지 않습니다. [출처: https://www.hani.co.kr/arti/economy/economy_general/1273108.html] (기사 2026-08, 국가데이터처 7월 마이크로데이터 인용)
- 2025년 하반기 서울 자치구별 청년 고용률은 금천구 59.7%가 가장 높았고 동대문구 32.9%가 가장 낮았으며, 서울 안 격차는 26.8%p였습니다. 이 값은 언론 보도 인용이며 원자료는 확인하지 못했습니다. [출처: https://www.mk.co.kr/news/economy/11970891] (기사 2026-02-24, 국가데이터처 2025년 하반기 지역별 고용조사 인용)
- 서울 전체 고용률은 61.5%였습니다. 청년만을 가리키는 수치가 아니므로 청년 고용률로 쓰지 않습니다. [출처: https://data.si.re.kr/smr/smr2025/reports/SMR2025_03_INDECON_SI.html] (서울연구원 2025년 보고서)
- 서울 청년의 생성형 AI 사용 경험률은 2023년 17.6%에서 2025년 44.5%로 올랐고, 20~30대 청년은 70%를 넘었습니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=460837&srchCtgry=474] (서울시 보도자료 2026-07-02)
- 대한상공회의소 조사를 인용한 서울시 자료에 따르면 기업 10곳 중 7곳이 채용 시 AI 역량을 고려하고 있었습니다. 원자료의 표본과 질문은 확인하지 못했습니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=460837&srchCtgry=474] (서울시 보도자료 2026-07-02, 2025년 하반기 조사 인용)
- 전공과 직무가 일치하지 않을수록, 기술 수준이 과잉 또는 부족한 집단일수록 이직 확률이 높아지는 경향이 나타났습니다. [출처: https://www.keis.or.kr/keis/ko/proj/113/pblc/detail.do?categoryIdx=131&pubIdx=11293] (게시일 미확인)
- 서울연구원은 2023년 기준 20~37세 청년의 쉬었음 비율을 약 5.0%로 제시했습니다. [출처: https://www.si.re.kr/bbs/view.do?key=2024100039&pstSn=2606190001] (2023년 기준, 페이지 날짜 미추출)

### 13.2 서울시가 이미 하는 사업과 빈틈

- 서울시는 2021년부터 2025년 8월까지 18개 청년 일자리 사업에 총 89만여 명이 참여했고, 총 7,455억 원을 투입했습니다. [출처: https://news.seoul.go.kr/gov/archives/571364] (수정 2025-09-19)
- 청년취업사관학교는 2021~2024년 272개 과정을 운영하며 5,952명을 누적으로 수료시켰고, 평균 취업률은 75.4%였습니다. 이 값은 누적 수치입니다. [출처: https://news.seoul.go.kr/gov/archives/571364] (수정 2025-09-19)
- 청년취업사관학교 2025년 취업률은 77%로 2024년 76.1%보다 올랐다고 서울시가 발표했습니다. 게시일은 확인하지 못했습니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=457379] (게시일 미확인)
- 서울시는 2030년까지 연간 1만 명의 AI 인재를 양성하고 취업률 80~90%를 목표로 제시했습니다. 달성 실적이 아닌 목표입니다. [출처: https://news.seoul.go.kr/economy/archives/569635?listPage=1] (게시일 미확인, 2026-10-28 조회)
- 서울형 청년인턴 직무캠프는 2024년 184명 중 108명, 58.7%가 정규직으로 전환되었습니다. [출처: https://news.seoul.go.kr/gov/archives/571364] (수정 2025-09-19)
- 2025년 초 서울형 청년인턴 직무캠프는 인턴십 기간을 3개월에서 4개월로 늘렸고, 96개 기업에 청년 229명을 매칭했습니다. [출처: https://news.seoul.go.kr/gov/archives/571364] (수정 2025-09-19)
- 2026년 서울형 청년인턴 직무캠프의 AI·디지털 분야는 청년취업사관학교 AI교육 수료생에 한정되었고, 신청 자격은 만 18~34세 서울 거주 구직자였습니다. [출처: https://job.seoul.go.kr/hmpg/yijc/yimp/yimpInfo.do] (2026년 모집 안내)
- 2026년 청년수당은 월 50만 원씩 최대 6개월 구직 활동비를 주고, 선정 인원은 2만 명 내외로 제시되었습니다. [출처: https://mediahub.seoul.go.kr/archives/2017342] (2026-03-05)
- 2026년 청년수당에는 1:1 취업 컨설팅이 신규로 더해졌고, 선배 멘토링은 600명으로 전년의 2배가 되었습니다. [출처: https://mediahub.seoul.go.kr/archives/2017342] (2026-03-05)
- 2026년 서울 매력일자리는 총 3,600명 규모이며 공공형 1,620명, 민간형 1,980명입니다. [출처: https://news.seoul.go.kr/economy/archives/570024] (2025년 말 2026년 사업 안내)
- 서울연구원은 질 낮은 과거 일자리 경험이 이후 쉬었음 상태를 크게 예측한다고 분석했습니다. 개인 역량 부족, 관계 단절, 정책 정보 부족도 쉬었음 위험을 높인다고 보았습니다. [출처: https://www.si.re.kr/bbs/view.do?key=2024100039&pstSn=2606190001] (페이지 날짜 미추출)
- 서울연구원은 현행 고용정책이 인턴과 직업훈련 중심이라고 지적했습니다. 대학 재학 시기부터 예방하는 접근이 부족하고, 연계 일자리의 질을 관리하는 체계도 미흡하다고 보았습니다. [출처: https://www.si.re.kr/bbs/view.do?key=2024100039&pstSn=2606190001] (페이지 날짜 미추출)
- 빈틈 추정: 서울시 성과 페이지는 수료자 수와 취업률은 보여 주지만, 개인별 적합도나 고용 유지 기간은 나타내지 않습니다. 개인 단위로 왜 이 직무가 맞는지 설명하는 도구는 공개 자료에서 확인하지 못했습니다. [출처: https://news.seoul.go.kr/gov/archives/571364] (수정 2025-09-19, 이 페이지에 한정한 관찰)

### 13.3 기존 민간·공공 서비스와 한계

- 고용24는 고용 관련 서비스를 통합 제공하고 맞춤형 추천 기능을 안내합니다. [출처: https://www.keis.or.kr/keis/ko/conts/101/web.do] (게시일 미표시, 2026-10-28 조회)
- 잡케어는 직무 역량 분석으로 경력개발 로드맵과 상담에 쓸 시장 정보를 제공하며, 2023년 3월부터 누구나 이용하도록 대국민용으로 확대되었습니다. [출처: https://www.keis.or.kr/keis/ko/conts/100/web.do] (게시일 미표시, 2026-10-28 조회)
- 잡케어 등 공공 AI 매칭은 전공, 자격증, 직업훈련, 경력, 경험을 이력서 정보로 쓰고 유사 사용자의 선호도 분석합니다. 이 경우 이력서 정보가 없는 사용자는 입력 부담이 큽니다. [출처: https://www.keis.or.kr/keis/ko/conts/100/web.do] (게시일 미표시, 2026-10-28 조회)
- 2023년 AI 매칭 취업은 57,844명에서 75,546명으로 약 30.6% 늘었습니다. [출처: https://www.keis.or.kr/keis/en/bbs/300/detail.do?pageIndex=1&pstSn=5] (게시일 2025-01-21)
- 2025년 말 기준 공공 AI 매칭 이용 후 취업자는 17만 2천 명이었고, 추천 공고에 지원한 뒤 해당 일자리에 취업한 사람은 2만 1천 명이었습니다. 이용자 대비 비율과 인과 효과는 확인하지 못했습니다. [출처: https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=19100] (게시일 2026-03-20)
- 고용노동부는 2026년 신규 AI 구직 컨설팅을 2개월 시범 운영한 뒤 8월부터 정식 운영한다고 밝혔습니다. 이 서비스는 희망 직종 취업 확률과 이력서, 자기소개서, 직업훈련의 보완점을 안내합니다. [출처: https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=19582] (게시일 2026-06-30)
- 고용노동부는 AI 고용서비스의 비용과 편익, 품질을 평가하는 연구를 공고했습니다. [출처: https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20260500140] (게시일 2026-05-06)
- 사람인 AI 매치는 로그인 없이도 쓸 수 있으며, 구직 활동과 이력서 희망 조건을 바탕으로 공고를 추천합니다. [출처: https://www2.saramin.co.kr/zf_user/help/help-word/view?idx=533&list_idx=16&page=1] (원등록 2019-01-10, 수정 2026-03-24)
- 사람인 AI 모의면접은 상품을 구매해야 하고, 카메라, 마이크, 스피커가 필요합니다. [출처: https://www2.saramin.co.kr/zf_user/help/help-word/main?inquiryCode=1646&memberCode=1638] (게시일 미표시, 2026-10-28 조회)
- 청년몽땅정보통은 과정과 기간별 훈련 모집 공고를 게시합니다. 강북캠퍼스 DX 5기 모집은 2026년 10월 12일부터 11월 8일까지였고, 신청 자격은 서울시민 또는 서울 거주자였습니다. [출처: https://youth.seoul.go.kr/infoData/sprtInfo/view.do?key=2309130006&sprtInfoId=74771] (모집 2026-10-12~2026-11-08)
- 20~30대 구직 플랫폼 UX 연구는 플랫폼마다 평가가 달랐고, 한 플랫폼은 찾기 기능과 접근성에서 약점을 보였다고 보고했습니다. [출처: https://journal.kci.go.kr/ipir/archive/articleView?artiId=ART003172615] (2025년, 권 10호 1, 163-172쪽)

### 13.4 쓸 수 있는 공개 데이터·API

| 이름 | 제공 기관 | 제공 형태 | 인증키 | 갱신 주기 | 활용 | URL |
|---|---|---|---|---|---|---|
| 청년(15~29세) 고용동향 | 서울특별시 | 데이터셋 페이지, 정기 공표 | 불필요 | 정기(매년), 2026-10-28 조회 | 청년 고용 기준선 | https://data.seoul.go.kr/bsp/wgs/dataView/data300View/467.do |
| 연령별 실업자 분기 통계 | 서울특별시 | 페이지(파일 없음) | 불필요 | 분기 갱신 2026.05.04 | 분기 추세 확인 | https://data.seoul.go.kr/dataList/DT201004D010018/S/2/datasetView.do |
| 서울 열린데이터광장 OpenAPI | 서울특별시 | OpenAPI (xml, xls, json) | 필요 | 미확인 | 서울 데이터 직접 호출 | https://data.seoul.go.kr/together/guide/useGuide.do |
| 고용행정통계 구인·구직 API | 고용노동부 고용24 | 기초자료 API(XML) | 미확인 | 월 단위 | 지역·5세 단위 연령·직종별 구인 수요 | https://eis.work24.go.kr/eisps/opiv/selectOpivList.do |
| 고용24 채용정보 API | 고용노동부 고용24 | 목록·상세 API (XML) | 필요, 심사 후 발급 | 미확인 | 공고 검색 | https://www.work24.go.kr/cm/e/a/0110/selectOpenApiSvcInfo.do?fullApiSvcId=000000000000000000000000000000 |
| 고용24 표준직무기술서 API | 고용노동부 고용24 | API (JSON) | 필요 | 미확인 | 직무 번역, NCS 능력단위 정의 | https://www.work24.go.kr/cm/e/a/0110/selectOpenApiSvcInfo.do?fullApiSvcId=000000000000000000000000000096 |
| 고용24 국민내일배움카드 훈련 API | 고용노동부 고용24 | API | 필요 | 미확인 | 훈련과정 검색, NCS 직종 분류 | https://www.work24.go.kr/cm/e/a/0110/selectOpenApiSvcInfo.do?fullApiSvcId=000000000000000000000000000004 |
| 고용24 정부지원일자리 API | 고용노동부 고용24 | API (XML), 성별·연령·지역별 참여자 통계 | 필요 | 미확인 | 지원사업 연결 | https://www.work24.go.kr/cm/e/a/0110/selectOpenApiSvcInfo.do?apiSvcId=000000000000000000000000000047&fullApiSvcId=000000000000000000000000000045%5E000000000000000000000000000055&upprApiSvcId=000000000000000000000000000045 |
| KEIS 컨소시엄 훈련과정 API | 한국고용정보원 (KEIS) | API (XML) | 활용신청, 자동승인 | 실시간, 무료 | 훈련과정 조회 | https://www.data.go.kr/data/15037380/openapi.do |
| KEIS 훈련 공통코드 API | 한국고용정보원 (KEIS) | API (XML) | 활용신청, 자동승인 | 실시간, 무료 | 훈련 지역·분야 코드 | https://www.data.go.kr/data/15037382/openapi.do |
| 직업훈련기관 파일데이터 | 한국고용정보원(KEIS), data.go.kr 게시 | CSV(기관명·시군구·주소·위도·경도) | 불필요 | 연간, 차기 등록 예정 2027-09-30 | 훈련기관 지도 | https://www.data.go.kr/data/15149261/fileData.do |
| KOSIS 지표정보 API | KOSIS, data.go.kr 게시 | REST API (JSON, XML) | 미확인 | 미확인 | 고용·노동 지표 조회 | https://www.data.go.kr/data/15127763/openapi.do |
| 워크넷 LOD | 고용노동부 | Linked Open Data, SPARQL 엔드포인트 | 필요, 회원가입 후 신청 | 미확인 | 직무·자격 용어 연결 | https://lod.work.go.kr/openAPI_guide.do |

### 13.5 6시간 아이디어 후보

대회 조건은 다음과 같습니다. 본선은 2026년 11월 21일 당일 6시간 동안 실제 작동하는 서비스를 개발하고 배포하는 방식입니다. [출처: https://yoill.com/contest-2026-seoul-ai-digital-hackathon/] (정보 확인일 2026.10.18) 평가는 실제 작동 여부, 정보 약자의 접근성을 고려한 화면, 시민이 체감할 효과를 봅니다. [출처: https://yoill.com/contest-2026-seoul-ai-digital-hackathon/] (정보 확인일 2026.10.18) 핵심 기능 코딩은 본선 당일에 진행해야 하며 커밋 기록으로 확인합니다. [출처: https://yoill.com/contest-2026-seoul-ai-digital-hackathon/] (정보 확인일 2026.10.18)

- 아이디어 1. 쉬운공고. 채용공고를 하는 일, 필요한 것, 근무 조건의 세 칸으로 풀어 주고, 이용자 경험과 비교해 부족한 역량을 훈련과정과 연결합니다. 대상은 구직 초심자, 오래 쉰 청년, 공고 용어가 어려운 정보 약자입니다. 핵심 기능은 공고 쉬운말 변환과 음성 읽기, 경험 체크, 훈련과정 3건 연결입니다. 데이터는 고용24 채용정보 API, KEIS 컨소시엄 훈련과정 API, KEIS 공통코드 API를 씁니다. 6시간 실현성은 상입니다. 주요 위험은 고용24 키 지연이며, 합성 공고로 대체하고 연동 위치를 발표 자료에 넣습니다. 차별점은 공고 문장 자체를 풀어쓰는 점입니다. 사람인 AI 매치는 추천이 중심이고, 고용24 추천은 이용자 정보 기반입니다. [출처: https://www2.saramin.co.kr/zf_user/help/help-word/view?idx=533&list_idx=16&page=1] [출처: https://www.keis.or.kr/keis/ko/conts/101/web.do]
- 아이디어 2. 경험 번역기. 아르바이트, 동아리 같은 비정형 경험을 글이나 칩으로 입력하면 NCS 직무 언어로 바꾸고, 직무 후보 3개와 가진 능력, 더 필요한 능력을 보여 줍니다. 대상은 전공과 일이 맞지 않는 청년, 쉬었음 청년, 경력이 짧은 청년입니다. 핵심 기능은 경험 입력, 직무 번역, 다음 걸음 안내입니다. 데이터는 고용24 표준직무기술서 API, KEIS 컨소시엄 훈련과정 API, 고용24 훈련 API, 청년몽땅정보통 공고를 씁니다. 6시간 실현성은 중입니다. 직무 후보 품질을 맞추려면 프롬프트 시험이 필요하고, 훈련과 직무 연결이 개인 적합성을 보장한다고 오해받지 않도록 참고용 안내 문구를 고정합니다. 차별점은 이력서가 없어도 말 한 줄로 시작하는 입구입니다. 잡케어는 이력서 정보를 바탕으로 분석합니다. [출처: https://www.keis.or.kr/keis/ko/conts/100/web.do] 전공과 직무가 맞지 않을수록 이직 확률이 높다는 연구도 근거로 쓸 수 있습니다. [출처: https://www.keis.or.kr/keis/ko/proj/113/pblc/detail.do?categoryIdx=131&pubIdx=11293]
- 아이디어 3. 가까운 배움터 지도. 자치구와 분야를 고르면 직업훈련기관을 목록과 지도 핀으로 보여 주고, 인쇄용 한 장 카드를 만듭니다. 대상은 이동 부담이 큰 청년, 장애인, 1인가구, 야간 근로자, 자치구 일자리센터 상담원입니다. 위치 정보는 수집하지 않습니다. 데이터는 훈련기관 CSV, KEIS 컨소시엄 훈련과정 API, KEIS 공통코드 API를 씁니다. 6시간 실현성은 상입니다. 핵심 데이터가 키 없는 CSV이고 나머지는 자동승인 API라 외부 의존이 가장 낮습니다. CSV에는 위도와 경도 값이 빈 행이 있을 수 있으므로 지도에서만 빼고 목록에는 남깁니다. [출처: https://www.data.go.kr/data/15149261/fileData.do] 차별점은 개인 정보 없이 자치구 선택만으로 동작하는 점입니다. 자치구 고용률 격차는 발표 맥락으로만 씁니다. [출처: https://www.mk.co.kr/news/economy/11970891]
- 아이디어 4. 사장님 구인문 도우미. 소상공인 사업주가 업무를 말하거나 적으면 쉬운 구인문, 필수 요건, 우대 요건, NCS 능력단위를 만듭니다. 과한 경력 요건은 되묻고, 임금과 시간은 입력값만 씁니다. 대상은 소상공인 사업주와 그 공고를 읽는 청년입니다. 데이터는 고용24 표준직무기술서 API, 고용24 채용정보 API, KEIS 컨소시엄 훈련과정 API를 씁니다. 6시간 실현성은 중입니다. 요건 점검 규칙과 문구 품질 확인에 시간이 들지만, LLM만으로 동작하는 폴백이 있습니다. 차별점은 조사 범위의 서비스가 대부분 구직자용이고, 공급자 쪽 쉬운 구인문 도구는 확인하지 못했다는 점입니다. 없다고 단정하지는 않습니다. [출처: https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=19582]

### 13.6 트랙 추천도

| 항목 | 점수 (1~5) | 이유 |
|---|---|---|
| 문제 근거 강도 | 4 | 전국 청년 고용, 전공 일치, 쉬었음 통계와 서울연구원 분석이 1차 출처로 확인되었습니다. 서울 청년 단독 최신 수치는 부족합니다. |
| 데이터 가용성 | 3 | 훈련과정 API와 훈련기관 CSV는 바로 쓸 수 있습니다. 고용24 공고와 직무 API는 심사 후 키가 필요합니다. |
| 6시간 실현성 | 4 | 아이디어마다 화면과 LLM 호출, API가 적어 범위가 작습니다. 추정으로는 무료 LLM 한도와 키 지연이 가장 큰 변수입니다. |
| 심사 기준 적합도 | 3 | 실제 작동, 포용 UX, 체감 효과를 맞출 수 있습니다. 다만 정보 약자 설계를 직접 만들어야 합니다. |
| 경쟁 예상 (추정) | 2 | 이력서 분석과 직무 추천형 아이디어에 팀이 몰릴 가능성이 큽니다 (추정). |

종합 추천도는 중입니다. 문제 근거와 실현성은 충분하지만, 경쟁이 몰릴 가능성이 크고 핵심 API가 키에 묶여 있습니다. 추정으로는 아이디어 3을 기본으로 두고, 아이디어 1의 쉬운말 변환을 더하면 접근성 차별점이 살아납니다. [출처: https://www.keis.or.kr/keis/ko/conts/101/web.do]

### 13.7 출처

1. https://mods.go.kr/board.es?act=view&bid=210&list_no=446080&mid=a10301010000
2. https://www.korea.kr/news/policyNewsView.do?newsId=156771847
3. https://www.mods.go.kr/board.es?act=view&bid=210&list_no=437676&mid=a10301010000&nPage=1
4. https://www.kostat.go.kr/boardDownload.es?bid=210&list_no=439131&seq=5
5. https://www.hani.co.kr/arti/economy/economy_general/1273108.html
6. https://www.mk.co.kr/news/economy/11970891
7. https://data.si.re.kr/smr/smr2025/reports/SMR2025_03_INDECON_SI.html
8. https://www.seoul.go.kr/news/news_report.do?nttNo=460837&srchCtgry=474
9. https://www.keis.or.kr/keis/ko/proj/113/pblc/detail.do?categoryIdx=131&pubIdx=11293
10. https://www.si.re.kr/bbs/view.do?key=2024100039&pstSn=2606190001
11. https://news.seoul.go.kr/gov/archives/571364
12. https://www.seoul.go.kr/news/news_report.do?nttNo=457379
13. https://news.seoul.go.kr/economy/archives/569635?listPage=1
14. https://job.seoul.go.kr/hmpg/yijc/yimp/yimpInfo.do
15. https://mediahub.seoul.go.kr/archives/2017342
16. https://news.seoul.go.kr/economy/archives/570024
17. https://www.keis.or.kr/keis/ko/conts/101/web.do
18. https://www.keis.or.kr/keis/ko/conts/100/web.do
19. https://www.keis.or.kr/keis/en/bbs/300/detail.do?pageIndex=1&pstSn=5
20. https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=19100
21. https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=19582
22. https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20260500140
23. https://www2.saramin.co.kr/zf_user/help/help-word/view?idx=533&list_idx=16&page=1
24. https://www2.saramin.co.kr/zf_user/help/help-word/main?inquiryCode=1646&memberCode=1638
25. https://youth.seoul.go.kr/infoData/sprtInfo/view.do?key=2309130006&sprtInfoId=74771
26. https://journal.kci.go.kr/ipir/archive/articleView?artiId=ART003172615
27. https://data.seoul.go.kr/bsp/wgs/dataView/data300View/467.do
28. https://data.seoul.go.kr/dataList/DT201004D010018/S/2/datasetView.do
29. https://data.seoul.go.kr/together/guide/useGuide.do
30. https://eis.work24.go.kr/eisps/opiv/selectOpivList.do
31. https://www.work24.go.kr/cm/e/a/0110/selectOpenApiSvcInfo.do?fullApiSvcId=000000000000000000000000000000
32. https://www.work24.go.kr/cm/e/a/0110/selectOpenApiSvcInfo.do?fullApiSvcId=000000000000000000000000000096
33. https://www.work24.go.kr/cm/e/a/0110/selectOpenApiSvcInfo.do?fullApiSvcId=000000000000000000000000000004
34. https://www.work24.go.kr/cm/e/a/0110/selectOpenApiSvcInfo.do?apiSvcId=000000000000000000000000000047&fullApiSvcId=000000000000000000000000000045%5E000000000000000000000000000055&upprApiSvcId=000000000000000000000000000045
35. https://www.data.go.kr/data/15037380/openapi.do
36. https://www.data.go.kr/data/15037382/openapi.do
37. https://www.data.go.kr/data/15149261/fileData.do
38. https://www.data.go.kr/data/15127763/openapi.do
39. https://lod.work.go.kr/openAPI_guide.do
40. https://www.50plus.or.kr/apiIndex.do
41. https://yoill.com/contest-2026-seoul-ai-digital-hackathon/

## 14. 부록 D. 트랙 D 자유주제 근거

### 14.1 서울의 실제 문제 현황과 수치

- 서울 보행 교통사고 사망자는 2024년 117명이며, 전체 도로 사망자는 2024년 212명입니다. [출처: https://news.seoul.go.kr/traffic/archives/335]
- 서울 보행 교통사고 사망자 중 65세 이상 비율은 2024년 68.4%입니다. [출처: https://news.seoul.go.kr/traffic/archives/514766?listPage=1]
- 서울 온열질환자는 2025년 5월 15일~7월 7일 85명으로, 전년 같은 기간의 27명보다 58명 늘었습니다. 발생 시간 중 오전 10~12시 비중은 2025년 자료에서 44%입니다. [출처: https://news.seoul.go.kr/welfare/archives/571990]
- 서울 오존 평균 농도는 2015년 0.024ppm, 2024년 0.037ppm입니다. 오존주의보 발령일수는 2015년 3일, 2024년 8월 기준 31일이며, 발령 횟수는 같은 자료에서 4회와 109회로 제시됩니다. [출처: https://news.seoul.go.kr/env/archives/559396]
- 1인당 도시공원 면적은 2003년 15.38㎡, 2023년 17.90㎡입니다. 공원율은 2003년 26.12%, 2023년 28.59%입니다. 서울시는 생활권 녹지 공급이 과거에 다소 부족했다고 설명했습니다. [출처: https://news.seoul.go.kr/env/archives/563012]
- 서울 지하철 민원 챗봇 또타24는 2025년 1~5월 126,747건을 처리했고, 이 중 냉·난방 민원은 95,510건이었습니다. [출처: https://news.seoul.go.kr/traffic/archives/514663]
- 2023년 보도에서 공공 모바일 앱 233개 중 접근성 인증 앱은 13개(5%)였다고 전했습니다. 이는 2023년 보도에 인용된 조사 수치입니다. [출처: https://zdnet.co.kr/view/?no=20231016095118]

### 14.2 서울시가 이미 하는 사업과 빈틈

- 서울시는 교통약자, 고령자, 임산부를 위한 서울동행맵을 2024년 11월에 출시했고, 보도자료는 경사도·보도 폭 안내와 저상버스 예약, 장애인콜택시 등 교통 지원 기능을 소개했습니다. [출처: https://english.seoul.go.kr/seoul-helping-map-app-wins-uitp-awards-2025-for-diversity-and-inclusion/]
- 서울시는 2026년 공공시설 입지 분석에서 50m 격자로 CCTV, 전기차 충전소 등 5종 시설을 분석하고, 생활인구·안전 수요·교통 접근성·기존 시설 분포를 고려한다고 밝혔습니다. 분석 시간이 기존 최소 한 달에서 약 한 시간으로 줄고 약 12억 원 규모의 비용을 절감했다고 발표했습니다. [출처: https://www.seoul.go.kr/news/news_report.do?nttNo=453763&srchCtgry=474]
- 서울연구원은 스마트쉼터 13곳을 2021년 8월부터 시범 운영한 평가에서 이용자가 승차 시스템을 잘 모르거나 시스템 작동을 믿지 못해 지정 승차 위치를 이용하지 않는 사례를 확인했습니다. 고장 시설을 방치하지 않도록 지속적인 관리가 필요하다고 제시했습니다. [출처: https://www.si.re.kr/bbs/view.do?key=2024100039&pstSn=2507280003]
- 서울톡은 서울시정 문의에 답하고 불법주정차 신고, 소음 신고, 방역 요청 등 현장 민원 54종을 접수합니다. 2026년 10월 12일 수정 페이지는 교통·환경·문화·안전 분야를 안내합니다. [출처: https://news.seoul.go.kr/gov/archives/511223]
- 서울안전누리는 재난·사고 속보, 행동요령, 가까운 대피장소와 의료기관, 날씨·생활지수를 제공합니다. [출처: https://safecity.seoul.go.kr/guide.do]
- 서울시민 안전보험은 2026년 1월 1일~12월 31일 서울에 주민등록된 시민을 자동 가입 대상으로 안내하며, 등록외국인도 포함합니다. 지반침하 사망·후유장해 보장도 2026년부터 추가됐습니다. [출처: https://news.seoul.go.kr/safe/archives/506117]
- 서울의 시민참여예산 데이터에는 사업 위치, 사업비, 제안 취지, 사업 내용과 효과가 포함됩니다. 위치 기반으로 사업을 살펴보는 시민 참여 기능에 활용할 수 있습니다. [출처: https://data.seoul.go.kr/dataList/OA-15414/S/1/datasetView.do]

### 14.3 기존 민간·공공 서비스와 한계

- 서울톡은 시정 문의에 답하고 현장 민원 54종을 접수하며, 또타24는 서울 지하철 1~8호선 민원을 24시간 처리합니다. 쉬운 문장으로 이미 받은 안내문을 바꾸고 근거 문장과 음성을 함께 제공하는 기능은 확인된 설명에 나타나지 않습니다. [출처: https://news.seoul.go.kr/gov/archives/511223] [출처: https://news.seoul.go.kr/traffic/archives/514663]
- Seoul Verse는 서울 공공데이터를 일상 언어로 검색하지만, 서비스 안내는 날씨·일반 지식·개인 질문에서 정확도가 제한될 수 있다고 알립니다. [출처: https://data.seoul.go.kr/bsp/wgs/chatbot/chatbotMain.do]
- 서울안전누리는 다양한 재난 정보와 주변 시설을 제공하고, 위치 기반 안내와 시설 공유 기능도 지원합니다. 특정 질문에 대한 짧은 행동 안내와 음성 중심 사용 흐름은 별도 아이디어로 제안할 수 있습니다. [출처: https://safecity.seoul.go.kr/guide.do]
- 복지로는 복지서비스 검색, 맞춤급여 안내, 온라인 신청, 복지시설 지도와 도움 요청 기능을 제공합니다. 공공 앱 접근성 인증은 2023년 보도에서 233개 중 13개로 집계됐습니다. [출처: https://m.bokjiro.go.kr/ssis-tem/cms/mob/intro/intro/intro/index.html] [출처: https://zdnet.co.kr/view/?no=20231016095118]
- 서울 실시간 도시데이터는 현장 상황 조회용 API이며 장기 적재와 통계 분석을 목적으로 하지 않습니다. 실시간 인구는 통신사 기지국 자료를 가공하므로 실제 현장 인원과 다를 수 있습니다. [출처: https://data.seoul.go.kr/dataVisual/seoul/guide.do]

### 14.4 쓸 수 있는 공개 데이터·API

| 이름 | 제공 기관 | 제공 형태 | 인증키 | 갱신 주기 | 활용 | URL |
|---|---|---|---|---|---|---|
| 도시데이터 | 서울특별시 | OPEN API/XML | 서울 키 필요 | 인구·도로·교통 5분, 상권·날씨 10분, 행사 1일 | 혼잡·날씨·교통·행사 안내 | https://data.seoul.go.kr/dataList/OA-21285/A/1/datasetView.do |
| 서울 자치구 실시간 대기환경 | 서울특별시 | 텍스트/CSV | 필요 | 매시간 | 자치구 대기질 안내 | https://data.seoul.go.kr/dataList/OA-1200/A/1/datasetView.do |
| 하천수위 최신값 | 서울특별시 | SHEET/OPEN API | 필요 | 10분 | 수위와 침수·통제수위 비교 | https://data.seoul.go.kr/dataList/datasetView.do?currentPageNo=null&infId=OA-1167&serviceKind=1&srvType=S |
| 강우량·하천 수위 안내 | 서울특별시 | SHEET/OPEN API/FILE | 안내 페이지 기준 | 개별 갱신일 미확인 | 관측소·시우량·일일 누계 안내 | https://data.seoul.go.kr/dataList/22/literacyView.do |
| 도로 소통 정보 | 서울특별시 | OPEN API/XML | 필요 | 실시간 | 도로 구간 속도·통행시간 안내 | https://data.seoul.go.kr/dataList/datasetView.do?currentPageNo=1&infId=OA-13291&serviceKind=1&srvType=A |
| 따릉이 실시간 대여 정보 | 서울특별시 | OPEN API/JSON | 필요 | 실시간 | 대여 가능 자전거와 대여소 위치 표시 | https://data.seoul.go.kr/dataList/OA-15493/A/1/datasetView.do |
| 공공 전기차 충전소 | 서울특별시 | 텍스트/CSV | 필요 여부 미확인 | 분기 | 위치·충전기 종류·이용 조건 안내 | https://data.seoul.go.kr/dataList/OA-23033/S/1/datasetView.do |
| 무더위쉼터 현황 | 서울특별시 | 공개 데이터 페이지/API | 필요 | 페이지 갱신일 2026년 10월 27일 | 주소·좌표·보유품목·운영시간 안내. 시설면적·이용가능인원·비고는 2026년 8월 10일 이후 빈값으로 제공됩니다. 샘플 API 요청은 정상 응답했습니다. [출처: https://data.seoul.go.kr/dataList/OA-21065/S/1/datasetView.do?tab=A] |
| 서울시 버스 위치 정보 | 서울특별시 | OPEN API/JSON/XML | 필요, 개발단계 자동승인 | 실시간 | 버스 위치와 이동 안내 | https://www.data.go.kr/data/15000332/openapi.do |

### 14.5 6시간 아이디어 후보

#### 쉬운말 서울

- 한 줄 요약: 서울시 안내문을 대상·혜택·신청 방법·마감 네 줄로 바꾸고 음성으로 읽습니다.
- 대상 사용자: 고령자, 발달장애인, 글 읽기가 어려운 시민, 한국어가 서툰 거주민.
- 핵심 기능: 네 줄 카드 요약, 원문 근거 연결, 큰 글씨·고대비·음성 읽기를 제공합니다.
- 데이터·API: 서울시 공개 안내문을 바탕으로 만든 시연 문서, Groq 선택 사용, 브라우저 음성 합성을 이용합니다.
- 6시간 구현 범위: 입력과 샘플 선택, 요약 함수, 근거 하이라이트, 글자 설정, 음성 읽기를 구현합니다. 계정·저장·다국어·실시간 문서 수집은 목업으로 둡니다.
- 시연 장면: 동행안심벨 안내를 선택하고 쉬운 글 카드와 원문 근거를 확인한 뒤 음성 읽기를 시연합니다.
- 심사 포인트: 정보 접근성을 개선하고 안내문의 신청 조건을 한 화면에 모읍니다.
- 위험과 대응: 요약 오류에 대비해 날짜와 숫자를 원문에서 보존하고 시연 문장을 사전 검수합니다.
- 실현 가능성: 상, 외부 데이터 호출 없이 한 화면 중심으로 구현합니다.
- 차별점: 서울톡·Seoul Verse의 질문·검색 방식과 달리 안내문 문장 변환, 근거 연결, 음성 읽기에 집중합니다.

#### 오늘 나가도 돼요?

- 한 줄 요약: 자치구 대기질과 날씨를 세 단계 신호와 한 문장 행동 안내로 제공합니다.
- 대상 사용자: 야외 활동이 잦은 고령자, 만성질환자, 혼자 사는 사람.
- 핵심 기능: 자치구 선택, 대기질·기온 신호, 음성 안내와 여름 시나리오 재생을 제공합니다.
- 데이터·API: 서울 자치구 대기환경, 서울 실시간 도시데이터 날씨, 무더위쉼터 데이터를 활용합니다.
- 6시간 구현 범위: API 프록시, 규칙 판정, 신호 화면, 음성, 시나리오 재생을 구현합니다. 지도와 알림은 목업으로 둡니다.
- 시연 장면: 자치구 상태와 갱신 시각을 보여 준 뒤 폭염 시나리오에서 쉼터 정보를 안내합니다.
- 심사 포인트: 고령자가 큰 글씨와 음성으로 외출 참고 정보를 확인합니다.
- 위험과 대응: 쉼터 데이터 상태가 충돌하므로 응답을 확인하고, 제공 정보의 기준 시점을 표시합니다.
- 실현 가능성: 상, 판정 화면은 단순하며 쉼터 자료 확인이 필요합니다.
- 차별점: 서울안전누리의 폭넓은 정보와 달리 지금 외출 판단에 필요한 한 문장 안내에 집중합니다.

#### 오늘 장사 어때

- 한 줄 요약: 주요 장소의 혼잡·날씨·행사·도로 상황을 모아 하루 준비 세 가지를 제안합니다.
- 대상 사용자: 음식점·카페·소매점 소상공인과 1인 사업자.
- 핵심 기능: 장소별 현황 요약, 준비 행동 제안, 음성 브리핑을 제공합니다.
- 데이터·API: 서울 실시간 도시데이터와 도로·행사 정보를 활용하고, 필요하면 문장 생성에 LLM을 씁니다.
- 6시간 구현 범위: 장소 선택, XML 프록시, 요약 카드, 근거 수치가 붙은 준비 제안을 구현합니다. 매출 연동과 알림은 목업으로 둡니다.
- 시연 장면: 한 장소를 선택해 현황 네 항목과 오늘 준비할 일 세 가지를 확인합니다.
- 심사 포인트: 소상공인의 하루 운영 준비를 돕습니다.
- 위험과 대응: 장소 수는 자료에 따라 120곳 또는 121곳으로 다르게 표기됩니다. 시연 장소를 미리 골라 API 응답을 확인합니다.
- 실현 가능성: 중, XML 필드 확인과 장소별 응답 검증이 필요합니다.
- 차별점: 조회형 데이터와 달리 가게 운영 상황에 맞춘 준비 행동으로 바꿉니다.

#### 비 오는 날 우리 동네

- 한 줄 요약: 하천 수위와 강우량을 안전 단계와 행동 안내로 표시합니다.
- 대상 사용자: 하천 주변 주민, 고령자, 1인 가구, 이동이 불편한 시민.
- 핵심 기능: 관측소 선택, 수위와 기준 수위 비교, 큰 글씨 행동 카드와 음성을 제공합니다.
- 데이터·API: 하천 수위 최신값 API와 강우량·하천 수위 관측소 정보를 이용합니다.
- 6시간 구현 범위: 수위 프록시, 기준 비교 막대, 강우 요약, 행동 카드, 합성 폭우 재생을 구현합니다. 위치 자동 선택과 푸시는 목업으로 둡니다.
- 시연 장면: 평상시 수위에서 시작해 합성 폭우 재생으로 주의·위험 단계를 보여 줍니다.
- 심사 포인트: 복잡한 수위 수치를 직관적인 막대와 음성으로 안내합니다.
- 위험과 대응: 11월 시연에는 폭우 실시간 상황이 드물 수 있어 합성 데이터 재생 모드를 표시합니다.
- 실현 가능성: 중, 수위 API 연동과 합성 시나리오가 필요합니다.
- 차별점: 서울안전누리의 종합 안내와 달리 하천 수위와 기준 수위의 거리를 한 화면에서 설명합니다.

### 14.6 트랙 추천도

| 항목 | 점수(1~5) | 판단 근거 |
|---|---:|---|
| 문제 근거 강도 | 4 | 온열질환, 보행 사고, 접근성 관련 수치가 확인됩니다. |
| 데이터 가용성 | 4 | 대기질·도시데이터·수위 자료가 공개되어 있고 갱신 정보가 있습니다. |
| 6시간 실현성 | 4 | 쉬운말 서울은 데이터 의존이 낮고, 나머지도 핵심 화면을 제한해 구현할 수 있습니다. |
| 심사 기준 적합도 | 4 | 시민 체감과 디지털 포용에 직접 연결되는 후보가 있습니다. |
| 경쟁 예상 | 2 | 자유 주제의 참가 규모는 확인하지 못했으며, 경쟁 가능성은 추정입니다. |

종합 추천도: 상

쉬운말 서울은 외부 데이터 의존이 낮고, 근거 문장·큰 글씨·음성을 한 번에 시연할 수 있습니다. 오늘 나가도 돼요?는 확인된 폭염 수치와 실시간 공공 데이터를 결합할 수 있어 두 번째 후보로 적합합니다.

### 14.7 출처

1. https://news.seoul.go.kr/traffic/archives/335
2. https://news.seoul.go.kr/traffic/archives/514766?listPage=1
3. https://news.seoul.go.kr/welfare/archives/571990
4. https://news.seoul.go.kr/env/archives/559396
5. https://news.seoul.go.kr/env/archives/563012
6. https://news.seoul.go.kr/traffic/archives/514663
7. https://zdnet.co.kr/view/?no=20231016095118
8. https://english.seoul.go.kr/seoul-helping-map-app-wins-uitp-awards-2025-for-diversity-and-inclusion/
9. https://www.seoul.go.kr/news/news_report.do?nttNo=453763&srchCtgry=474
10. https://www.si.re.kr/bbs/view.do?key=2024100039&pstSn=2507280003
11. https://news.seoul.go.kr/gov/archives/511223
12. https://safecity.seoul.go.kr/guide.do
13. https://news.seoul.go.kr/safe/archives/506117
14. https://data.seoul.go.kr/dataList/OA-15414/S/1/datasetView.do
15. https://data.seoul.go.kr/bsp/wgs/chatbot/chatbotMain.do
16. https://m.bokjiro.go.kr/ssis-tem/cms/mob/intro/intro/intro/index.html
17. https://data.seoul.go.kr/dataVisual/seoul/guide.do
18. https://data.seoul.go.kr/dataList/OA-21285/A/1/datasetView.do
19. https://data.seoul.go.kr/dataList/OA-1200/A/1/datasetView.do
20. https://data.seoul.go.kr/dataList/datasetView.do?currentPageNo=null&infId=OA-1167&serviceKind=1&srvType=S
21. https://data.seoul.go.kr/dataList/22/literacyView.do
22. https://data.seoul.go.kr/dataList/datasetView.do?currentPageNo=1&infId=OA-13291&serviceKind=1&srvType=A
23. https://data.seoul.go.kr/dataList/OA-15493/A/1/datasetView.do
24. https://data.seoul.go.kr/dataList/OA-23033/S/1/datasetView.do
25. https://data.seoul.go.kr/dataList/OA-21065/S/1/datasetView.do?tab=A
26. https://www.data.go.kr/data/15000332/openapi.do
