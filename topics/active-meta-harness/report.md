---
title: 능동형 메타하네스(학생 요청형 하네스 최적화) 선행연구 조사
subtitle: 연구 아이디어 검토
summary: 학생 에이전트가 풀이 중 스킬·도구·가드레일을 교사에게 요청하고 교사가 하네스를 고치는 구조의 선행연구 157편을 원문으로 확인하고 새로움, 반론, 최소 실험 설계를 정리했습니다.
created: 2026-11-20
updated: 2026-11-20
---

# Meta-Harness + Active Learning 결합 연구 조사

작성일: 2026-11-20. 조사 기준 시점: 2026-11-20에 공개된 arXiv 원문.

## 요약

**결론.** 이 아이디어는 세 단계입니다. 학생 하네스가 문제를 푸는 도중 필요한 스킬, 도구, 가드레일을 교사에게 요청합니다. 교사는 그 요청과 trajectory를 함께 보고 하네스를 고칩니다. 요청 채널의 효과를 대조군으로 측정합니다. 이 세 단계를 모두 갖춘 논문은 이번 조사 범위에서 찾지 못했습니다. 다만 구성요소는 2026년에 대부분 따로 발표되었습니다. 따라서 "요청 채널을 붙였더니 올랐다"는 주장만으로는 새로움이 약합니다. 논문이 되려면 요청 신호가 무엇을 더 알려 주는지(정보량), 언제 요청해야 하는지(시점), 요청이 정답 누설과 과적합을 일으키지 않는지(통제)를 대조 실험으로 보여야 합니다.

**가장 가까운 선행연구 3편.**

1. HarnessCompass (arXiv 2608.01918, 2026-08). 실패한 과제마다 같은 모델에게 "하네스에 있었으면 했던 기능"을 사후에 보고하게 합니다. trajectory로 검증한 보고만 메타 에이전트의 하네스 진화 증거로 씁니다. 학생 신호를 하네스 최적화에 넣는다는 점에서 가장 가깝습니다. 차이는 시스템이 풀이 후에 묻는 방식이며, 학생이 풀이 중 스스로 요청하지 않는다는 점입니다.
2. Evo-Harness (arXiv 2608.15071, 2026-08). 과제 묶음이 끝날 때마다 solver가 "빠졌던 행동, 명령, 도구 호출, 도메인 규칙"을 분석해 재사용 스킬을 제안하고, evolver가 제안을 받아들이거나 합쳐 하네스에 넣습니다. 학생 쪽 제안 채널이 있다는 점에서 가깝습니다. 차이는 제안이 풀이 후에 나오고, evolver는 제안을 고르는 큐레이터이며 도구나 가드레일을 설계하는 교사가 없다는 점입니다.
3. MetaForge (arXiv 2606.01801, 2026-06). 정책이 풀이 중 기존 도구로 안 되면 자연어 요구를 담아 create_skill을 호출하고, 별도 tool-forging 모델이 도구를 만들어 검증 후 도구 풀에 남깁니다. "풀이 중 요청 → 다른 모델이 만듦 → 다음 과제에 남음"의 세 단계를 갖춘 가장 가까운 사례입니다. 차이는 요청 대상이 도구뿐이고, trace와 점수를 보고 하네스 전체를 반복 최적화하는 교사가 없다는 점입니다.

4위와 5위는 How² (arXiv 2510.11144)와 Teaching the Harness/SAT (arXiv 2611.13144)입니다. How²는 학생이 풀이 중 교사에게 질문하고 답을 메모리에 남기지만 교사가 하네스를 고치지 않습니다. SAT는 교사가 학생을 진단해 스킬을 쓰지만 능동성이 교사 쪽에 있습니다. 이 아이디어는 SAT의 방향을 뒤집은 구조이므로 SAT가 가장 직접적인 비교 기준선입니다.

**Motivation.** 처음 세운 서사 "proposer는 정적인 정보만 본다"는 그대로 쓰기 어렵습니다. Meta-Harness의 proposer도 학생 출력을 포함한 전체 trace를 읽기 때문입니다. 권하는 서사는 "trace는 학생이 한 일만 남기고, 결정 시점에 무엇이 모자랐는지는 학생만 안다"입니다(5절).

**논문성 판단.** 가능성은 있습니다. 다만 경쟁이 매우 빠릅니다. 2026년 11월 한 달에만 SAT(11-09)와 자기개선 하네스 서베이(11-17)가 나왔습니다. 핵심 위험은 두 가지입니다. 첫째, HarnessCompass의 절제 실험에서 1인칭 피드백을 넣자 진화 과제 정답률은 올랐지만 held-out 정답률은 58.4%에서 55.8%로 내려갔습니다. 요청 신호는 과적합을 키울 수 있습니다. 둘째, "같은 모델이 사후에 반성한 것"과 "풀이 중 요청한 것"의 차이를 대조군으로 분리하지 못하면 self-reflection의 변형으로 읽힙니다.

**권고.** 주제는 "능동 요청 채널이 바깥 하네스 최적화에 주는 정보 가치"로 한정하는 것이 좋습니다. 대조군은 (a) 수동 Meta-Harness형, (b) 사후 보고형(HarnessCompass형), (c) 풀이 중 요청형, (d) 요청 내용을 섞은 셔플 대조, (e) 학생이 자기 요청을 스스로 구현하는 self-harness 대조입니다. 같은 교사 토큰 예산과 같은 평가 횟수에서 held-out 성능을 비교합니다. 1차 벤치마크는 HarnessCompass와 직접 비교할 수 있는 SWE-bench Verified 분할이고, 2차는 EHRSQL 같은 EHR text-to-SQL 벤치마크입니다. 마감이 공식 확인된 학회는 ACL 2027(ARR 2027-01-04)과 ICML 2027(초록 2027-01-14, 본문 2027-01-22)입니다. 남은 기간이 6~9주이므로 현실적인 목표는 공식 일정이 아직 없는 COLM 2027 또는 NeurIPS 2027입니다.

## 1. 조사 범위와 방법

- 사실로 쓴 내용은 모두 arXiv 원문(HTML 또는 abs 페이지)이나 공식 페이지를 직접 읽고 확인했습니다. abs 페이지의 citation_title 메타데이터로 제목을 대조했습니다. 검색 결과 요약만 본 항목은 "확인 못 함"으로 표시했습니다.
- arXiv 검색 API(export.arxiv.org)는 조사 중 HTTP 429를 반환했고, 반환된 일부 목록은 id와 제목이 실제 원문과 달랐습니다. 예를 들어 목록에 "Harness Handbook"으로 나온 2611.04579는 실제로 "FreeForm Harness" 논문이었습니다. 그래서 API 목록은 버리고, 웹 검색 결과와 참고문헌에서 얻은 id를 abs 페이지에서 하나씩 대조했습니다.
- 원문을 읽은 논문은 157편입니다(papers.csv). 하네스 최적화 계열과 학생 요청 계열은 별도 조사 lane이 각각 67편, 38편을 읽었고, 나머지는 직접 읽었습니다. 반대 검색으로 찾은 2026년 하네스 진화 논문 21편은 본문에서 학생 요청 채널을 정규식으로 찾았고, 해당 채널은 나오지 않았습니다.
- 유료 API는 쓰지 않았습니다.

## 2. Meta-Harness와 하네스 최적화 계열

### 2.1 Meta-Harness 원문

Meta-Harness: End-to-End Optimization of Model Harnesses (Lee, Nair, Zhang, Lee, Khattab, Finn; arXiv 2603.28052, 2026-03-30)를 원문으로 확인했습니다. [링크](https://arxiv.org/abs/2603.28052), 코드 [stanford-iris-lab/meta-harness](https://github.com/stanford-iris-lab/meta-harness).

- 구조: 바깥 루프의 proposer는 코딩 에이전트(Claude Code, Opus-4.6)입니다. proposer는 이전 모든 후보 하네스의 소스 코드, 점수, 실행 trace가 저장된 파일시스템을 grep, cat으로 읽고 새 하네스를 제안합니다. 원문은 이 점을 "an outer-loop system that searches over harness code"라고 씁니다.
- 규모: 보통 한 번의 실행에서 20회 반복 동안 약 60개 하네스를 평가합니다. 가장 무거운 설정에서 proposer는 반복당 중앙값 82개 파일을 읽습니다.
- 결과: 온라인 텍스트 분류에서 ACE보다 7.7점 높고 문맥 토큰은 4분의 1입니다. IMO 수준 수학 200문항에서 held-out 모델 5개 평균 4.7점 향상입니다. TerminalBench-2에서 Opus 4.6 기준 76.4%, Haiku 4.5 기준 37.6%입니다.
- 학생(하네스 안의 고정 모델)의 역할: 학생은 주어진 하네스로 과제를 풀고 trace를 남길 뿐입니다. 학생이 proposer에게 무엇을 요청하는 경로는 원문에 없습니다. 이 아이디어가 문제 삼는 "passive" 구조와 일치합니다.

같은 이름 주의: MoMHa (arXiv 2609.30967)도 초록에서 자기 시스템을 "Meta-Harness"라고 부릅니다. 정확도, 안전, 토큰 비용의 다목적 하네스 탐색입니다. 인용할 때 저자로 구분해야 합니다.

### 2.2 2026년 하네스 진화 계열

2026년에 "하네스 자동 진화"가 하나의 연구 계열이 되었습니다. 원문으로 확인한 대표 논문과 학생 요청 채널 유무는 아래와 같습니다. 모두 학생 요청 채널이 없거나, 있어도 시스템이 사후에 묻는 형태입니다.

| 논문 | arXiv | 바깥 최적화기 | 학생 요청 채널 |
|---|---|---|---|
| Agentic Harness Engineering (AHE) | 2604.25850 | 관측성 기반 진화 에이전트 | 없음 |
| HarnessCompass | 2608.01918 | 메타 에이전트(학생과 같은 GPT-5.4) | 사후 1인칭 보고(실패 과제만) |
| Training the Whole Agent (HarnessAdapt-RL) | 2610.28069 | RL 중 교사가 스킬, 도구, 훅 진화 | 없음(실패 시 시스템이 스킬 생성) |
| VERSE | 2610.02616 | 스스로 진화하는 최적화기 | 없음(최적화기가 능동 탐침) |
| Self-Harness | 2606.09498 | 학생 자신 | 해당 없음(자기 개선) |
| Multi-Task Self-Evolving Harnesses | 2609.38372 | 같은 모델이 solver 후 proposer | 해당 없음(자기 개선) |
| AI4AI at Test-Time | 2608.12307 | 강한 builder가 약한 target의 하네스 구성 | 없음 |
| Learning Meta-Skills for Harness Design | 2609.38143 | builder가 meta-skill 학습 | 없음 |
| ActiveSaddler | 2610.00906 | 최적화기가 학습 시나리오(커리큘럼) 선택 | 없음 |
| Harness Learning | 2609.35738 | RL로 훈련한 proposer | 없음 |
| Harnesses That Improve Themselves (서베이) | 2611.22299 | 4단계 루프 정리 | 분류 축에 없음 |

"Active"라는 이름 충돌도 있습니다. ActiveSaddler는 최적화기가 어떤 학습 시나리오를 쓸지 고르는 커리큘럼 학습을 "Active"라고 부릅니다. 우리 아이디어의 "학생이 능동적으로 요청한다"와 뜻이 다르므로, 제목에서 active를 쓰면 구분 문장이 필요합니다.

### 2.3 고전 계열과 2025년 계열

브리프가 지정한 고전 계열은 모두 원문으로 확인했습니다. 학생이 최적화기에 요청하는 경로는 어느 논문에도 정의되어 있지 않습니다. 요청과 비슷한 행동이 있는 경우만 아래에 적습니다.

| 논문 | arXiv | 최적화 방식 | 요청과 비슷한 행동 |
|---|---|---|---|
| ADAS | 2408.08435 | 메타 에이전트가 에이전트 코드를 쓰고 아카이브로 탐색 | 없음 |
| AFlow | 2410.10762 | MCTS로 코드형 워크플로 수정 | 없음 |
| Gödel Agent | 2410.04444 (ACL 2025) | 에이전트가 실행 중 자기 코드를 교체 | 제약 없는 변형에서 "spontaneous requests for assistance from more powerful models"를 관찰. 설계된 채널은 아님 |
| Darwin Gödel Machine | 2505.22954 | 아카이브 기반 자기 수정 코딩 에이전트 | 없음(자기 수정) |
| DSPy | 2310.03714 | trace 부트스트랩으로 데모와 모듈 최적화 | 없음 |
| MIPRO | 2406.11695 (EMNLP 2024) | 지시문과 데모를 베이지안 최적화 | 없음 |
| GEPA | 2507.19457 (ICLR 2026) | trace 반성 기반 프롬프트 진화 | 없음 |
| TextGrad | 2406.07496 | 텍스트 피드백 역전파 | 없음 |
| Trace / OPTO | 2406.16218 | 실행 그래프 trace로 생성형 최적화. OPTO는 이 논문 안의 정식화 | 없음 |
| Promptbreeder | 2309.16797 | 과제 프롬프트와 변이 프롬프트를 함께 진화 | 없음 |
| Agent Workflow Memory | 2409.07429 | trajectory에서 워크플로를 유도해 메모리에 추가 | 없음 |
| Voyager | 2305.16291 | 자동 커리큘럼과 스킬 라이브러리 | 커리큘럼이 현재 상태로 스스로 질문 |
| LATM | 2305.17126 | 강한 모델이 도구를 만들고 약한 모델이 사용 | dispatcher가 도구 제작을 촉발 |
| CREATOR | 2305.14318 (Findings of EMNLP 2023) | 생성-결정-실행-수정 파이프라인 | 없음 |
| CRAFT | 2309.17428 (ICLR 2024) | 오프라인 도구셋 생성과 검색 | 모델이 필요한 함수를 서술해 검색 질의로 사용 |
| Alita | 2505.20286 | 관리자가 역량 공백을 찾아 MCP 도구 생성 | 관리자가 빌더에게 하위 과제 설명 전달 |
| ACE | 2510.04618 (ICLR 2026) | Generator-Reflector-Curator로 playbook 진화 | Generator가 항목의 유용성을 표시 |

2025년 이후 자기 개선 계열(Live-SWE-agent 2511.13646, SICA 2504.15228, EvoAgentX 2507.03616, Agent KB 2507.06229, SkillWeaver 2504.07079)도 확인했습니다. 에이전트가 자기 도구를 직접 쓰거나 최적화기가 실행 기록을 읽는 구조이고, 학생이 외부 최적화기에 요청하는 구조는 없습니다. 학회명은 arXiv 원문 주석에 적힌 경우만 적었습니다.

## 3. 학생이 요청하는 계열

학생 쪽 능동성은 오래된 연구 계열입니다. 다만 요청의 결과가 그 에피소드 안에서 끝나는 경우가 대부분이고, 요청이 교사의 하네스 수정으로 이어지는 경우는 확인하지 못했습니다. 학생 요청 계열 조사 lane이 38편의 원문을 읽고 abs 메타데이터로 제목과 날짜를 대조했습니다.

### 3.1 요청 결과가 다음 과제까지 남는 연구

| 논문 | arXiv | 누가 누구에게 무엇을 요청하는가 | 무엇이 남는가 |
|---|---|---|---|
| How² | 2510.11144 | 에이전트가 교사에게 how-to 질문 | 상태와 분리한 지시문을 메모리에 저장해 재사용 |
| LATM | 2305.17126 | dispatcher가 강한 모델에게 도구 제작 요청 | 검증된 도구를 캐시에 저장 |
| UCT | 2602.01983 | 에이전트가 없는 도구를 build ticket으로 요청 | 시험을 통과한 도구를 라이브러리에 등록 |
| Uni-Skill | 2603.02623 | 계획 파이프라인이 부족한 스킬 구현을 요청 | 스킬 저장소(새 구현의 재사용은 원문에서 분명하지 않음) |
| STELLA | 2507.02004 | 관리 에이전트가 도구 제작 에이전트에게 위임 | Template Library, Tool Ocean |
| SMITH | 2512.11303 | planner가 developer-tester 루프에 하위 의도를 위임 | 도구와 과제 간 에피소드 메모리 |
| Ask Now, Use Later | 2605.28108 | 에이전트가 사용자에게 지속 선호와 제약을 질문 | 이후 세션에서 쓰는 고정 문맥 |
| MetaAgent | 2508.00271 | 추론 에이전트가 tool router에게 자연어 help request | 경험 텍스트와 지식베이스(router는 고정) |
| MCP-Zero | 2506.01056 | 에이전트가 역량 공백을 찾아 구조화된 도구 요청(Active Tool Request) | 기존 MCP 서버 풀에서 검색한 도구를 누적. 새 도구를 만들지 않음 |

LATM은 이 아이디어의 "도구 요청" 부분에 가장 오래된 선례입니다. 원문 표현은 "dispatcher determines whether it needs to request tool-making"입니다. 다만 요청 주체가 도구를 쓰는 학생과 다른 dispatcher이고, 학생에 맞춰 하네스를 반복 최적화하는 루프는 없습니다.

### 3.2 요청 결과가 그 에피소드에서 끝나는 연구

- 도움 요청 시점 학습: Robots That Ask For Help/KnowNo (2307.01928), Ask4Help (2211.09960), Learning When to Ask for Help (2305.16502), R2V Agent (2605.16604), Bayesian Self-Escalation (2608.24087), Inference-Time Distillation (2512.02543), AHCE (2602.22546). 앞의 세 편은 LLM이 아닌 로봇 또는 내비게이션 정책입니다.
- 명확화 질문: ClarifyGPT (2310.10996), STaR-GATE (2403.19154), Learning to Ask (2409.00557), TO-GATE (2506.02827), Modeling Future Conversation Turns (2410.13788), Ask-before-Plan (2406.12639), Asking Before Acting (2305.15695), 임베디드 MLLM의 도움 요청 (2504.00907).
- 교사에게 질문하며 배우기: Socratic Students (2512.13102), INTERACT (2412.11388, ACL 2025), AI Pedagogy (2507.21065), Active Inquiry/LaMAI (2402.03719), Knowledge Distillation with Training Wheels (2502.17717).

Learning to Ask (2409.00557)는 기존 API로 풀 수 없을 때 도구 한계를 보고하라고 지시합니다. 새 도구를 요청하거나 만드는 경로는 없습니다. 이 아이디어는 이 "보고"를 "요청"으로 바꾸고 교사가 응답하게 하는 확장으로 볼 수 있습니다.

### 3.3 교사가 하네스를 고치지만 학생 요청이 촉발하지 않는 연구

- Teaching the Harness/SAT (2611.13144), SkillGen (2605.10999), AgentDistill (2506.14728), Compiling Deterministic Structure into SLM Harnesses (2604.17450), Harness Compilation (2610.11231).
- 가드레일: GuardAgent (2406.09187)와 AGrail (2502.11448)은 운영자 기준과 관찰한 행동으로 검사 규칙을 추가하고 고칩니다. AGrail은 검사 규칙을 메모리에 남겨 이후 과제에 씁니다. 대상 에이전트가 가드레일을 요청하는 경로는 없습니다.

Harness Compilation (arXiv 2610.11231)은 반론 근거로 중요합니다. 큰 교사가 작은 VLM 학생의 실행 trace로 하네스를 고치는데, 학생에게 자원을 명시적으로 요청하게 하면 성능이 떨어졌습니다. 원문은 "Requiring an explicit resource request costs 9.0 points on InfoSeek and 2.7 on DocVQA"라고 보고합니다. 작은 학생에게는 요청 행위 자체가 부담일 수 있다는 뜻입니다. 6.2절의 반론 5에 반영했습니다.

## 4. 결합의 직접 선행연구: 가장 가까운 5편

"학생 요청 → 교사의 하네스 수정 → 성능 측정"의 세 고리를 기준으로 비교했습니다.

| 순위 | 논문 | 학생이 요청하는가 | 다른 주체가 하네스를 고치는가 | 요청 효과를 대조로 측정했는가 |
|---|---|---|---|---|
| 1 | HarnessCompass (2608.01918) | 풀이 후 시스템이 물으면 보고 | 예(메타 에이전트, 학생과 같은 모델) | 절제 실험 1행 |
| 2 | Evo-Harness (2608.15071) | 풀이 후 solver가 스킬 제안 | 예(evolver가 받아들이거나 합침) | 제안 채널 자체의 절제는 확인 못 함 |
| 3 | MetaForge (2606.01801) | 예(풀이 중 create_skill) | 도구만(별도 tool-forging 모델) | 요청 채널 자체의 절제는 확인 못 함 |
| 4 | How² (2510.11144) | 예(풀이 중 how-to 질문) | 아니오(답을 메모리에 저장) | 교사 답의 추상화 수준 비교 |
| 5 | SAT (2611.13144) | 아니오(교사가 탐침 요청) | 예(스킬 라이브러리) | 학습자 모델 유무 비교 |

### 4.1 HarnessCompass (arXiv 2608.01918)

[원문](https://arxiv.org/abs/2608.01918). 자동 하네스 진화에 세 원칙(제약된 진화, proactive feedback, 구성요소별 최적화)을 더합니다. proactive feedback은 실패한 과제마다 같은 모델에게 두 번 묻습니다. 첫째는 판정을 숨긴 "blind report"입니다. 여기서 하네스가 어디서 방해했는지와 "capabilities you WISHED EXISTED"(있었으면 했던 기능)를 받습니다. 둘째는 판정을 보여 준 "hindsight report"입니다. 여기서 실패 원인을 하네스, 자기 추론, 과제 모호성, 환경 중 하나로 돌립니다. 새 기능 요청은 trajectory가 구체적 공백을 보여 줄 때만 남깁니다. 모든 역할이 GPT-5.4를 쓰고, SWE-bench Verified를 진화 50과제와 held-out 450과제로 나눕니다.

절제 결과가 우리에게 가장 중요합니다. 일반화 게이트만 넣었을 때 진화 과제 62.0%, held-out 58.4%였습니다. 여기에 proactive feedback을 더하자 진화 과제는 66.0%로 올랐지만 held-out은 55.8%로 내려가고 반복 수는 2에서 12로 늘었습니다. 구성요소 병합(R3)을 더해야 held-out 60.4%로 회복했습니다. 원문은 이를 "feedback-driven edits may overfit to the evolution set"으로 해석합니다.

우리 아이디어와의 차이: (1) 보고 시점이 풀이 후입니다. (2) 시스템이 실패 과제에만 묻습니다. (3) 학생과 메타 에이전트가 같은 모델입니다. (4) 요청에 대한 응답이 그 에피소드 안에 돌아오지 않습니다. (5) 요청 신호 유무를 같은 예산에서 분리한 실험은 절제 표 1행뿐입니다.

### 4.2 Evo-Harness (arXiv 2608.15071)

[원문](https://arxiv.org/abs/2608.15071). 고정된 에이전트가 과제 흐름을 풀며 외부 하네스를 계속 갱신하는 "online harness learning"을 정식화합니다. 과제 묶음이 끝나면 solver 쪽 프롬프트가 실행 결과, 검증기 피드백, 압축 trajectory를 받습니다. solver는 "the concrete missing action, command, tool call, navigation step, or domain rule"을 찾고 "Propose a reusable skill"을 수행합니다(NEW, ENHANCE, NONE 중 선택). evolver 쪽 큐레이터는 각 제안을 ACCEPT, MERGE, SKIP 중 하나로 처리하고, 여러 미지 과제에 쓸모 있는지 일반화 시험을 적용합니다. 평가는 TerminalBench2, SWE-bench Lite, CL-Bench, τ-bench, WebArena-Infinity 다섯 개입니다. Claude Sonnet 4.5가 학습 분할에서 진화시킨 스킬을 Opus 4.7 solver가 시험 분할에서 쓰는 전이 실험도 있습니다.

우리 아이디어와의 차이: (1) 제안이 풀이 후 반성 단계에서 나옵니다. (2) 제안 대상이 스킬(지시문)이며 도구, 가드레일, 코드 수정은 없습니다. (3) evolver는 제안을 고르는 큐레이터이고, 학생이 원하는 것을 보고 새로 설계하는 교사가 아닙니다. (4) 제안 채널이 있을 때와 없을 때를 같은 예산에서 비교했는지는 확인하지 못했습니다.

### 4.3 MetaForge (arXiv 2606.01801)

[원문](https://arxiv.org/abs/2606.01801). 멀티모달 에이전트의 도구 사용을 Decide, Retrieve, Adapt, Forge 네 단계로 나눕니다. 원문은 "When no existing tool can handle a task, the policy triggers a create_skill action with a natural language requirement"라고 씁니다. 이어서 별도 tool-forging 모델이 계획과 구현 두 단계로 도구를 만듭니다. 검증을 통과한 도구는 용량 제한이 있는 도구 라이브러리에 들어가 재사용됩니다. 정책은 정답, 도구 필요성, 도구 생성 성공, 호출 비용을 합친 보상으로 RL 학습합니다. 12개 벤치마크에서 16개 기준선과 비교합니다.

우리 아이디어와의 차이: (1) 요청 대상이 도구뿐입니다. (2) tool-forging 모델은 요청 하나에 도구 하나로 응답하며, 여러 과제의 trace와 점수를 보고 하네스 전체(프롬프트, 워크플로, 가드레일)를 고치는 교사가 아닙니다. (3) 학생 정책을 가중치로 학습합니다. 우리 설계는 학생 가중치를 고정합니다.

### 4.4 How² (arXiv 2510.11144)

[원문](https://arxiv.org/abs/2510.11144). Plancraft(Minecraft 조합 과제)에서 에이전트가 how-to 질문을 하고, 교사 모델이 답하고, 답을 메모리에 저장해 이후 과제에 재사용합니다. 교사 답의 추상화 수준(실행 가능한 행동열부터 고수준 하위목표까지)을 바꿔 비교했습니다. 즉시 성공률은 실행 가능한 답이 가장 높았고, 평생 학습에는 "abstracted and decoupled from the current state"인 답이 가장 유리했습니다.

우리 아이디어와의 차이: 교사는 질문에 답만 하고 도구, 가드레일, 하네스 코드를 고치지 않습니다. 평가 점수를 보고 하네스를 탐색하는 바깥 루프가 없습니다. 환경이 하나입니다. 그러나 "추상적인 답일수록 재사용성이 높다"는 결과는 정답 누설 반론에 대한 설계 근거로 쓸 수 있습니다.

### 4.5 Teaching the Harness / SAT (arXiv 2611.13144)

[원문](https://arxiv.org/abs/2611.13144). 강한 교사가 학습자 모델(경험 프로필과 실패 가설)을 만들고, 가설을 시험하는 탐침 과제를 요청하고, 진단된 실패에 맞는 스킬을 씁니다. 스킬은 matched 개발 과제에서 성공률을 올릴 때만 라이브러리에 들어갑니다. Claude-Sonnet-5가 DeepSeek-V4-Flash를 가르친 주 실험에서 86.46%로, 학습자 모델 없는 교사 81.04%와 가르치지 않은 학생 75.00%보다 높습니다. 교사가 떠난 뒤 저장된 라이브러리가 평균 5.6~11.1점 이득을 유지합니다.

우리 아이디어와의 차이: 능동성이 교사 쪽에 있습니다. 원문 표현은 "The teacher requests probes"입니다. 학생은 탐침 과제를 풀 뿐 요청하지 않습니다.

### 4.6 그 밖에 가까운 연구

- UCT (arXiv 2602.01983): 풀이 중 에이전트가 "requests a tool that does not yet exist"이면 build ticket이 생깁니다. 격리된 빌드 루프가 도구 코드와 시험 스크립트를 만들어 라이브러리에 넣습니다. 빌드 루프도 같은 주 모델("we continue to employ the main model")입니다.
- MUSE-Autoskill (arXiv 2605.27366): 스킬이 부족하면 에이전트가 기능 명세를 넘겨 스킬을 만들고 등록합니다. 별도 교사는 없습니다.
- FreeForm Harness (arXiv 2611.04579): 맞는 확장이 없으면 기기의 에이전트가 Web 코딩 에이전트에게 확장 제작을 의뢰하고, 결과를 기기에서 검증해 받아들입니다. 요청과 외부 제작은 있지만 trace 기반 최적화는 아닙니다.
- Socratic Skill Learning/SSL (arXiv 2610.17860): Educator가 정해진 시점에 학생 작업을 검토하고, 학생은 "can question, test, adapt, or reject advice"합니다. 주 코호트 유틸리티 0.801로 스킬 없음 0.723보다 높고, Issue-Guided 방식은 0.805에 Educator 토큰을 61.7% 줄였습니다. 학생이 도구를 요청하는 경로와 교사의 하네스 수정은 없습니다.

- MetaAgent (arXiv 2508.00271): 지식 공백에서 자연어 help request를 만들고 tool router가 외부 도구로 보냅니다. 스스로 도구와 지식베이스를 쌓습니다. 교사가 하네스를 고치는 구조는 없습니다.
- AHCE (arXiv 2602.22546): 언제 사람 전문가에게 물을지 학습한 정책으로 Minecraft 성공률을 보통 난이도에서 32%, 고난도에서 약 70% 올립니다. 도움은 그 에피소드에만 쓰입니다.
- R2V Agent (arXiv 2605.16604): 작은 모델이 어느 단계에서 큰 모델에게 도움을 청할지 단계별 라우터로 정합니다. 하네스 변경은 없습니다.
- Knowledge Distillation with Training Wheels (arXiv 2502.17717): 학생이 테스트 시 교사의 도움을 청하는 법을 가중치 학습으로 배웁니다.
- HarnessAdapt-RL (arXiv 2610.28069): RL 중 고정 교사가 스킬을 만들고 다른 교사가 도구와 훅을 진화시킵니다. Qwen3.5-9B로 SWE-bench Verified에서 GRPO 대비 9.8점 높습니다. 스킬 생성은 실패 조건이 촉발합니다.
- AgentBrew (arXiv 2607.16851): 학생 실패가 교사 루프를 촉발해 외부 메모리에 노트를 남깁니다. 촉발 주체는 실패 판정입니다.
- LATM (arXiv 2305.17126): 도구 제작 모델이 Python 도구를 만들고 다른(더 작은) 모델이 그 도구를 씁니다. 새 유형의 요청이 들어오면 dispatcher가 도구 제작을 요청할지 정하고, 만든 도구는 캐시에 남습니다. 강한 모델이 약한 모델을 위해 지속 도구를 만드는 가장 이른 사례(2023)입니다. 요청 주체는 도구 사용 모델이 아닌 dispatcher이고, 하네스 최적화 루프는 없습니다.
- Harness Compilation (arXiv 2610.11231): 큰 교사가 작은 VLM의 실행 trace로 하네스의 내용과 제어를 고치고, 별도 검증 세트로 배포 하네스를 고릅니다. 학생 요청은 촉발 조건이 아닙니다.

## 5. Motivation 후보

권고하는 서사는 세 문장입니다. 기존 하네스 최적화는 학생이 한 일(trace)에서 학생에게 없던 것(공백)을 거꾸로 추론합니다. 공백은 결정 시점에 학생에게 가장 잘 보입니다. 학생이 그 시점에 싼 요청을 남기면 교사는 같은 예산으로 더 정확한 수정을 합니다. 후보 1(정보 비대칭)을 중심 주장으로, 후보 3(효율)을 주 결과로, 후보 2(학생 맞춤)를 분석 절로 두는 구성을 권합니다.

### 5.1 처음 세운 서사 평가: "proposer는 정적인 정보만 마주한다"

이 표현을 그대로 쓰면 반박당하기 쉽습니다. Meta-Harness의 proposer는 실행 trace를 원문 그대로 읽고, 원문은 trace에 "prompts, tool calls, model outputs, and state updates"가 들어 있다고 씁니다. 같은 논문은 점수만 준 조건(중앙값 34.6), 요약을 준 조건(34.9), 전체 trace를 준 조건(50.0)을 비교해 "더 풍부한 사후 정보"가 중요하다는 주장을 이미 했습니다. 심사자는 "학생의 출력과 추론이 trace에 다 있는데 무엇이 정적인가"라고 물을 것입니다.

살릴 수 있는 형태는 "trace는 학생이 한 행동만 기록하고, 하지 못해서 원했던 것은 기록하지 않는다"입니다. 이 주장은 HarnessCompass가 이미 했습니다. 원문은 기존 방법이 "show that a task failed and where, but not why the code agent struggled"라고 씁니다. 학생에게 묻는 이유는 "only the code agent knows where it got stuck"입니다. 따라서 원안의 차별점은 정보가 정적인지 여부에서 찾을 수 없고, 신호를 얻는 시점(풀이 중)과 주체(학생이 스스로 요청)에서 찾아야 합니다.

### 5.2 후보 1: 정보 비대칭

주장: proposer는 사후 trajectory로 실패 원인을 추론해야 합니다. 결정 시점에 무엇이 모자랐는지는 학생만 압니다.

같은 주장을 한 논문: HarnessCompass(2608.01918)가 사후 보고 형태로 같은 주장을 했습니다(5.1의 인용). How²(2510.11144)는 에이전트가 how-to 질문으로 "reduce uncertainty and fill knowledge gaps"한다고 쓰며, 학생이 자기 공백을 안다는 전제를 씁니다. 풀이 중 요청과 사후 보고를 같은 예산에서 비교한 논문은 확인하지 못했습니다.

반론:
- HarnessCompass가 이미 했다는 반론에는 시점 차이를 실험으로 보여야 합니다.
- 학생의 자기 진단이 틀릴 수 있습니다. HarnessCompass도 보고를 trajectory로 검증한 뒤에만 썼습니다. 우리도 요청을 후보 증거로만 쓰고 교사가 trace로 확인하게 합니다.
- 요청 도구가 생기면 학생의 풀이 행동 자체가 바뀝니다. 요청 도구는 있지만 교사가 요청을 읽지 않는 조건을 두어 이 효과를 분리합니다.

보여 줄 실험: 교사 예산을 고정하고 C2(사후 보고)와 C3(풀이 중 요청)를 비교합니다. 추가로 교사에게 요청 문장만 주는 조건과 요청 문장과 요청 직전 trace 구간을 함께 주는 조건을 비교합니다. 요청 정확도는 "요청이 가리킨 공백을 채운 수정이 그 과제를 실제로 고친 비율"로 잽니다.

### 5.3 후보 2: 학생 맞춤

주장: 교사가 설계한 도구와 스킬은 학생 능력에 맞지 않을 수 있습니다. 요청은 학생의 능력 경계를 드러냅니다.

같은 주장을 한 논문: 교사 쪽에서 학생을 추론하는 형태로 여러 편이 이미 주장했습니다.
- SAT(2611.13144): 교사가 학습자 모델과 탐침으로 학생 맞춤 스킬을 만들고, 틀린 프로필과 라이브러리 교환 통제로 학생 특이성을 보였습니다.
- EvoMatch(2610.33024): 103개 과제-스킬 쌍에서 같은 스킬이 GPT-5.6-luna를 31.1점 올리고 Gemma-4-E4B를 8.8점 떨어뜨렸습니다.
- AgentBrew(2607.16851): 교사 노트는 "tailored to be concretely executable by a substantially weaker student"여야 한다고 씁니다.
- SKILL-KD(2607.28048): 기존 스킬이 약한 학생에게 "mismatch"를 만든다고 씁니다.

학생이 요청으로 능력 경계를 직접 드러내는 형태는 확인하지 못했습니다.

반론:
- SAT의 교사 탐침이 같은 정보를 얻습니다. 학생 요청과 교사 탐침을 비용 대비로 비교해야 합니다.
- 약한 학생은 자기 공백을 모를 수 있습니다. EvoMatch는 약한 모델 실패의 86%에서 어긴 요구사항이 이미 스킬에 적혀 있었다고 보고합니다. 이런 실패는 요청으로 드러나지 않는 실행 문제입니다.

보여 줄 실험: 학생 모델 2~3개(강, 중, 약)에서 C3와 SAT형 교사 탐침을 같은 예산으로 비교합니다. 학생 A의 요청으로 만든 하네스를 학생 B에 적용하는 교환 통제(SAT의 library swap과 같은 방식)로 맞춤 효과를 확인합니다.

### 5.4 후보 3: 효율

주장: 요청은 학생이 싸게 붙이는 진단 라벨입니다. 같은 교사 예산에서 더 높은 성능, 또는 같은 성능에 더 적은 반복을 얻습니다. active learning에서 학습자가 질의할 표본을 골라 라벨 효율을 높이는 주장과 대응합니다. 대응 관계는 학생이 질의자, 교사가 oracle, 하네스 수정이 라벨입니다.

같은 주장을 한 논문: 최적화기 쪽 능동성으로는 이미 나왔습니다.
- VERSE(2610.02616): 최적화기가 스스로 고른 실험이 중요하다며 "probes the optimizer did not ask for can be worse than none"이라고 씁니다.
- SSL(2610.17860): 미해결 이슈에 검토를 집중해 Educator 토큰을 61.7% 줄였습니다.
- HarnessCompass(2608.01918): AHE 반복의 약 4분의 1로 더 높은 성능에 도달했습니다. 다만 원문은 이 효율을 일반화 게이트와 R3 병합으로 설명하고, 1인칭 피드백만 더한 행에서는 반복이 2에서 12로 늘었습니다.

학생 요청을 라벨로 보고 교사 예산 대비 성능 곡선을 그린 논문은 확인하지 못했습니다.

반론:
- 라벨에 잡음이 많을 수 있습니다. HarnessCompass의 피드백 단독 행은 held-out 하락과 반복 증가를 보였습니다.
- 요청 생성이 학생 토큰을 늘립니다. 학생과 교사를 합한 총비용으로 비교해야 합니다.
- active learning의 라벨은 정답 라벨이고 여기서 "라벨"은 하네스 수정입니다. 비유는 맞지만 이론 결과를 그대로 가져올 수는 없습니다.

보여 줄 실험: 교사 토큰 예산을 세 단계(0.5배, 1배, 2배)로 두고 C1, C2, C3의 held-out 성능 곡선을 그립니다. 요청 신호 절제는 세 가지입니다. (a) C3-shuffle(다른 과제의 요청), (b) 요청 문장을 지우고 요청 위치만 남김, (c) 과제당 요청 횟수 상한 변화. C3의 곡선이 같은 예산에서 C1, C2보다 위에 있고 (a)에서 이 차이가 사라지면 후보 3이 성립합니다.

## 6. 논문성 평가

### 6.1 새로움

조사 범위에서 세 고리(학생의 풀이 중 요청, 교사의 하네스 수정, 요청 효과의 통제 측정)를 모두 갖춘 논문은 찾지 못했습니다. 각 고리는 따로 존재합니다. 풀이 중 요청과 지속 결과는 MetaForge, How², UCT, MUSE-Autoskill이 했습니다. 학생 신호를 하네스 진화에 넣는 것은 HarnessCompass(사후 보고)와 Evo-Harness(사후 스킬 제안)가 했습니다. 교사-학생 하네스 교육은 SAT, SSL, AI4AI, HarnessAdapt-RL, Harness Compilation이 했습니다.

따라서 새로움은 "결합 자체"보다 다음 질문에서 나와야 합니다.

1. 풀이 중 요청은 사후 보고보다 무엇을 더 알려 주는가. 실패 직전 상태와 결정 시점의 맥락이 요청에 담기는지 측정할 수 있습니다.
2. 요청이 있는 과제와 없는 과제의 차이로 학생이 자기 공백을 얼마나 정확히 아는지(요청 보정)를 측정할 수 있습니다. EvoMatch(arXiv 2610.33024)는 103개 과제-스킬 쌍에서 같은 스킬이 GPT-5.6-luna를 31.1점 올리고 Gemma-4-E4B를 8.8점 떨어뜨린다고 보고합니다. 학생 요청은 이런 능력 불일치를 줄이는 신호가 될 수 있습니다.
3. 요청 예산과 교사 비용의 교환 관계입니다.

### 6.2 예상 반론과 대응

**반론 1: 요청 신호가 정답 누설이 된다.** 학생이 "이 테스트를 통과하는 함수를 달라"고 요청하고 교사가 과제별 코드를 넣으면 하네스가 과제를 외웁니다. HarnessCompass의 절제 결과(held-out 58.4% → 55.8%)가 이 위험의 실측 사례입니다. 대응은 네 가지입니다. (a) 교사는 진화 분할만 보고, 수정은 과제 비의존 규칙을 따릅니다(HarnessCompass의 일반화 게이트). (b) 모든 수정을 held-out 분할에서 받아들일지 정합니다. (c) Meta-Harness처럼 과제 문자열 누설을 정규식으로 감사합니다. (d) Bad Genius/CHASE(arXiv 2609.18366)처럼 평가 형식을 바꿔도 이득이 남는지 시험합니다. How²의 결과는 추상적인 응답이 재사용에 유리하다는 설계 근거를 줍니다.

**반론 2: 교사 비용이 늘어난다.** 요청마다 교사가 반응하면 비용이 늘어납니다. 대응은 같은 교사 토큰 예산과 같은 평가 횟수에서 비교하는 것입니다. SAT는 교사 비용을 실행당 달러로 보고하고(부록 G 설정에서 학습자 모델 교사 $1.245, 비교 교사 $0.459), SSL은 Issue-Guided 방식으로 Educator 토큰을 61.7% 줄였습니다. 우리도 요청을 모아 반복마다 한 번 처리하는 배치형을 기본으로 두는 것이 좋습니다.

**반론 3: 단순 self-reflection과 무엇이 다른가.** Self-Harness(2606.09498)와 Multi-Task Self-Evolving Harnesses(2609.38372)는 학생 자신이 하네스를 고칩니다. 대응은 대조군 두 개입니다. (a) 학생이 자기 요청을 스스로 구현하는 self 대조군, (b) 같은 모델이 풀이 후에 반성하는 사후 보고 대조군. 두 대조군보다 "풀이 중 요청 + 강한 교사"가 held-out에서 높아야 주장이 섭니다.

**반론 4: 효과를 내는 것은 요청 내용과 무관한 요청 횟수나 추가 토큰이다.** 대응은 셔플 대조군입니다. 요청 문장을 다른 과제의 요청과 섞어 교사에게 주고, 성능 차이가 사라지는지 봅니다.

**반론 5: 작은 학생에게는 요청 행위가 부담이다.** Harness Compilation(2610.11231)에서 작은 VLM에게 명시적 자원 요청을 요구하자 InfoSeek에서 9.0점, DocVQA에서 2.7점이 떨어졌습니다. 대응은 두 가지입니다. (a) 요청 도구를 선택 사항으로 두고, 요청 도구는 있으나 교사가 읽지 않는 조건으로 요청 행위의 비용을 따로 잽니다. (b) 학생 크기별로 결과를 나눠 보고합니다. 요청이 강한 학생에게만 효과가 있다면 그 자체가 후보 2(학생 맞춤)의 분석 결과가 됩니다.

### 6.3 대조군 설계(최소안)

모든 조건은 같은 학생 모델, 같은 교사 모델, 같은 seed 하네스, 같은 평가 횟수, 같은 교사 토큰 상한을 씁니다.

| 조건 | 교사가 받는 정보 | 학생 쪽 변화 |
|---|---|---|
| C0 | 없음(seed 하네스 고정) | 없음 |
| C1 수동 | trace + 점수(Meta-Harness형) | 없음 |
| C2 사후 보고 | C1 + 실패 후 1인칭 보고(HarnessCompass형) | 풀이 후 질문 응답 |
| C3 능동 요청 | C1 + 풀이 중 요청 로그 | request_capability(type, need, evidence) 도구 추가, 응답은 다음 반복에 반영 |
| C3-shuffle | C1 + 다른 과제의 요청 로그 | C3와 같음 |
| C3-self | 교사 없음, 학생이 자기 요청을 구현 | C3와 같음 |

요청 유형은 tool, skill, guardrail, knowledge 네 가지로 제한합니다. 지표는 held-out pass@1, 목표 점수 도달까지 반복 수, 교사 토큰, 요청 채택률(요청이 받아들여진 수정으로 이어진 비율), 요청 보정(요청한 과제와 실패한 과제의 일치도)입니다.

### 6.4 벤치마크 후보

| 벤치마크 | 원문 | 쓰는 이유 |
|---|---|---|
| SWE-bench Verified | [2310.06770](https://arxiv.org/abs/2310.06770) | HarnessCompass, HarnessAdapt-RL과 직접 비교 가능. HarnessCompass의 50/450 분할을 재사용할 수 있습니다. |
| Terminal-Bench 2 | Meta-Harness 4.3절 | Meta-Harness와 직접 비교. 원문은 별도 분할 없이 89과제에서 탐색과 평가를 같이 했으므로 우리 실험은 분할을 따로 두어야 합니다. |
| τ-bench | [2406.12045](https://arxiv.org/abs/2406.12045) | 도구와 정책(가드레일) 요청이 자연스럽게 생기는 도메인. |
| AppWorld | [2407.18901](https://arxiv.org/abs/2407.18901) | 앱 API 공백이 많아 도구 요청 신호를 보기 좋습니다. |
| WebArena | [2307.13854](https://arxiv.org/abs/2307.13854) | 웹 에이전트 일반성 확인용. |
| EHRSQL | [2301.07695](https://arxiv.org/abs/2301.07695), 2024 shared task [2405.06673](https://arxiv.org/abs/2405.06673) | text-to-SQL on EHR. 2024 shared task는 답할 수 없는 질문을 다루므로 "가드레일 요청"을 시험하기 좋습니다. |

EHR text-to-SQL과 연결하면 요청 유형이 구체적으로 나옵니다. 예를 들어 "OMOP concept 이름 조회 도구", "단위 변환 스킬", "답할 수 없는 질문에서 거절하는 가드레일" 요청이 나올 수 있습니다. 이 연결은 도메인 논문(예: 의료 NLP 워크숍)으로도 쓸 수 있습니다.

### 6.5 최소 실험 규모와 비용 감

아래는 추정이며 원문 수치가 아닙니다. 가정은 Meta-Harness의 "20회 반복, 약 60개 하네스 평가"를 그대로 따르고, 평가 한 번에 진화 분할 50과제를 쓰는 것입니다.

- 학생 에피소드 수 = 조건 6개 × seed 3개 × 하네스 60개 × 50과제 = 54,000회, 여기에 held-out 평가가 더해집니다.
- 이 규모는 학생을 로컬 오픈 모델로 돌릴 때만 현실적입니다. 학생 비용은 GPU 시간이 대부분입니다.
- 교사 비용은 반복 20회 × 조건 5개(C0 제외) × seed 3개 = 300회의 교사 세션입니다. 교사 세션 하나가 trace를 많이 읽으므로 교사 토큰 상한을 조건 공통으로 정해야 합니다.
- 줄인 1차 실험: SWE-bench Verified 대신 τ-bench 한 도메인이나 EHRSQL 일부로 시작하고, 조건을 C1, C2, C3, C3-shuffle 네 개, seed 2개로 줄입니다. 이 규모에서 C3가 C1, C2보다 held-out에서 높지 않으면 주제를 접는 기준으로 씁니다.

### 6.6 목표 학회와 마감

| 학회 | 마감 | 확인 상태 |
|---|---|---|
| ACL 2027 | ARR 제출 2027-01-04 | [공식 CFP](https://2027.aclweb.org/calls/main/)에서 확인 |
| ICML 2027 | 초록 2027-01-14, 본문 2027-01-22 (AoE) | [공식 일정](https://icml.cc/Conferences/2027/Dates)에서 확인 |
| COLM 2027 | 미발표 | 공식 2027 일정 페이지 404. 참고로 COLM 2026은 초록 3월 26일, 본문 3월 31일이었습니다([공식](https://colm.cc/Conferences/2026/Dates), 검색 결과 기준이며 직접 열지 않음) |
| NeurIPS 2027 | 미발표 | 공식 2027 일정 페이지 404 |
| ICLR 2027 | 2026-09-25 마감 지남 | [공식 저자 안내](https://iclr.cc/Conferences/2027/AuthorGuidelines), 검색 결과 기준 |
| KDD 2027 1차 | 2026-07-26 마감 지남 | [공식 CFP](https://kdd2027.kdd.org/research-track-call-for-papers/)에서 확인 |

추천 순서는 COLM 2027(언어모델 에이전트 주제와 맞고, Meta-Harness도 COLM 2026 포스터 페이지가 검색 결과에 있었습니다. 직접 열지 않아 확인 못 함), 다음이 NeurIPS 2027입니다. ACL과 ICML은 6~9주 안에 위 대조 실험을 끝내야 하므로 1차 결과가 12월 중순까지 나올 때만 시도할 만합니다.

### 6.7 ChatGPT 의견 검토

같은 아이디어에 대해 받은 ChatGPT 의견을 이번 조사 결과와 대조했습니다. 의견의 큰 방향은 이 보고서의 결론과 같습니다. 학생 요청이 trajectory 진단보다 무엇을 더 주는지 증명해야 하고, online task recovery와 cross-task improvement를 따로 재야 하며, 첫 프로토타입은 skill과 guardrail 요청으로 한정한다는 점입니다. 다음 네 가지는 고쳐야 합니다.

1. 가칭 "Active Harness Evolution (AHE)"는 약어가 Agentic Harness Engineering(AHE, arXiv 2604.25850)과 겹칩니다. HarnessCompass가 이 AHE를 기준선으로 씁니다.
2. 제안 제목의 "Learning to Ask"는 Learning to Ask: When LLM Agents Meet Unclear Instruction(arXiv 2409.00557)과 같습니다.
3. 의견이 든 선행연구(MCP-Zero, MetaAgent, Meta-Skills, SAT, ActiveSaddler)는 모두 원문으로 확인했습니다. MCP-Zero(2506.01056)는 "Active Tool Request"로 필요한 도구를 요청하지만 기존 서버 풀에서 검색할 뿐입니다. 더 가까운 HarnessCompass, Evo-Harness, MetaForge가 빠져 있습니다. 특히 MetaForge는 풀이 중 create_skill 요청으로 별도 모델이 도구를 만드는 구조이므로, "tool 요청"을 핵심 기여로 내세우면 겹칩니다. skill과 guardrail 요청으로 시작하자는 의견은 이 점에서도 맞습니다.
4. 요청 정책 학습(언제, 무엇을 요청할지)은 AHCE, R2V Agent, KnowNo, Bayesian Self-Escalation이 "언제 도움을 청할지"를 이미 학습했습니다. 이 방향을 기여로 삼으려면 요청 결과가 하네스에 지속되고 다음 과제에 쓰인다는 점에서 차별점을 보여야 합니다.

## 7. 확인하지 못한 것

- 조사 lane이 찾았지만 원문을 열지 못한 후보: Tool-Genesis (2603.05578), Joint Optimization of Tool Creation and Use (2608.24571), Guided-OPD (2606.15912). 세 편 모두 API 목록에만 있었고 abs 페이지로 제목을 대조하지 못했습니다.
- FlowEvo (2607.21596), SkillCraft (2603.00718), AI Pedagogy (2507.21065)는 abs 페이지의 citation_date가 arXiv id의 연월과 맞지 않습니다. papers.csv에는 citation_date의 연도를 적었습니다.
- Uni-Skill (2603.02623)이 배포 중 새로 만든 스킬 구현을 이후 과제에 재사용하는지는 원문에서 분명하지 않습니다.
- Evo-Harness와 MetaForge가 요청(제안) 채널을 끈 조건과 비교했는지는 이번에 읽은 부분에서 확인하지 못했습니다.

- COLM 2027, NeurIPS 2027 공식 마감은 아직 공개되지 않아 확인하지 못했습니다.
- Meta-Harness의 COLM 2026 채택은 검색 결과 요약에만 있고 해당 페이지를 직접 열지 않았습니다.
- Semantic Scholar API는 429를 반환해 인용 그래프 기반 탐색은 하지 못했습니다. 따라서 "직접 선행연구 없음"은 웹 검색, 참고문헌 추적, 반대 검색 21편 기준의 결론입니다.
- 비공개 진행 연구나 arXiv 외 학회 논문집에만 있는 논문은 범위 밖입니다.

## 참고문헌

전체 157편의 제목, 연도, 링크, 분류, 거리는 papers.csv에 있습니다. 본문에서 인용한 주요 문헌은 아래와 같습니다.

1. Meta-Harness: End-to-End Optimization of Model Harnesses (2026). https://arxiv.org/abs/2603.28052
2. MoMHa: Multi-Objective Optimization of LLM Harnesses over Accuracy, Safety, and Tokens (2026). https://arxiv.org/abs/2609.30967
3. HarnessCompass: Guiding Automatic Harness Evolution toward Generalizable and Effective Agent Harnesses (2026). https://arxiv.org/abs/2608.01918
4. Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents (2026). https://arxiv.org/abs/2608.15071
5. MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand (2026). https://arxiv.org/abs/2606.01801
6. $How^{2}$: How to learn from procedural How-to questions (2025). https://arxiv.org/abs/2510.11144
7. Teaching the Harness: Student-Aware Skill Transfer for LLM Agents (2026). https://arxiv.org/abs/2611.13144
8. Evolving from Tool User to Creator via Training-Free Experience Reuse in Multimodal Reasoning (2026). https://arxiv.org/abs/2602.01983
9. Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills (2026). https://arxiv.org/abs/2610.17860
10. Large Language Models as Tool Makers (2023). https://arxiv.org/abs/2305.17126
11. MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation (2026). https://arxiv.org/abs/2605.27366
12. FreeForm Harness: A Mobile-Native Agent Harness for Open and Composable Extensions (2026). https://arxiv.org/abs/2611.04579
13. MetaAgent: Toward Self-Evolving Agent via Tool Meta-Learning (2025). https://arxiv.org/abs/2508.00271
14. Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention (2026). https://arxiv.org/abs/2602.22546
15. R2V Agent: Teaching SLMs When to Ask for Help (2026). https://arxiv.org/abs/2605.16604
16. Knowledge Distillation with Training Wheels (2025). https://arxiv.org/abs/2502.17717
17. Training the Whole Agent, Not Just the Model (2026). https://arxiv.org/abs/2610.28069
18. AgentBrew: Lifelong Knowledge Brewing from Strong Teachers to Weak LLM Agents (2026). https://arxiv.org/abs/2607.16851
19. Harness Compilation: Which Decisions Should a Small Vision-Language Model Keep? (2026). https://arxiv.org/abs/2610.11231
20. Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation (2026). https://arxiv.org/abs/2610.33024
21. SKILL-KD: Contrastive Skill Distillation for LLM Agents (2026). https://arxiv.org/abs/2607.28048
22. VERSE: Verified Self-Evolving Optimizer for Agent Harnesses (2026). https://arxiv.org/abs/2610.02616
23. Self-Harness: Harnesses That Improve Themselves (2026). https://arxiv.org/abs/2606.09498
24. Multi-Task Self-Evolving Harnesses with the Agent as Its Own Optimizer (2026). https://arxiv.org/abs/2609.38372
25. Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts (2026). https://arxiv.org/abs/2609.18366
26. ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization (2026). https://arxiv.org/abs/2610.00906
27. Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses (2026). https://arxiv.org/abs/2611.22299
28. Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses (2026). https://arxiv.org/abs/2604.25850
29. AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses (2026). https://arxiv.org/abs/2608.12307
30. Learning to Ask: When LLM Agents Meet Unclear Instruction (2024). https://arxiv.org/abs/2409.00557
31. Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement (2024). https://arxiv.org/abs/2410.04444
32. SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2023). https://arxiv.org/abs/2310.06770
33. $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (2024). https://arxiv.org/abs/2406.12045
34. AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents (2024). https://arxiv.org/abs/2407.18901
35. WebArena: A Realistic Web Environment for Building Autonomous Agents (2023). https://arxiv.org/abs/2307.13854
36. EHRSQL: A Practical Text-to-SQL Benchmark for Electronic Health Records (2023). https://arxiv.org/abs/2301.07695
37. Overview of the EHRSQL 2024 Shared Task on Reliable Text-to-SQL Modeling on Electronic Health Records (2024). https://arxiv.org/abs/2405.06673

학회 일정: ICML 2027 https://icml.cc/Conferences/2027/Dates , ACL 2027 https://2027.aclweb.org/calls/main/ , KDD 2027 https://kdd2027.kdd.org/research-track-call-for-papers/

코드: Meta-Harness https://github.com/stanford-iris-lab/meta-harness

