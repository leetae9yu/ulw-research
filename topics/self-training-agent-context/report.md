---
title: 에이전트 self-training과 모델 주도 문맥 관리 문헌 조사
subtitle: 텍스트-SQL·EHR 질의 에이전트
summary: EHRSQL 2024 1위 self-training, STaR·ReST 계열, Stream of Search, NVIDIA 모델 주도 문맥 관리를 정리하고 의료 LLM 문헌 4편의 수치를 대조했습니다.
status: draft
created: 2026-11-28
updated: 2026-11-28
---

# 에이전트 self-training과 모델 주도 문맥 관리 문헌 조사

조사 기준일: 2026년 11월 28일. 공개 논문과 공개 페이지만 사용했습니다. 수치는 모두 원문 페이지와 대조했고, 확인하지 못한 곳은 그렇게 표시했습니다.

## 0. 요약

- EHRSQL 2024 공유 과제 1위는 LG AI Research & KAIST의 PLUQ입니다. 이 팀은 GPT-3.5-Turbo를 파인튜닝했습니다. 그다음 라벨 없는 질문 중 모델이 "답 못 함"으로 예측한 것만 null 라벨로 더해 한 번 더 학습했습니다. 시험 세트 RS(10)은 81.32로, 2위보다 6.4점 높습니다(2절).
- PLUQ 점수의 큰 부분은 필터에서 나옵니다. 필터가 없으면 검증 RS(10)은 -69.94이고, 실행 필터와 최대 token entropy 필터를 더하면 88.65입니다. self-training 단계만의 효과는 논문에 따로 나오지 않습니다(2.3절, 2.5절).
- 일반 self-training 문헌(STaR, ReST, ReST-EM, RFT, V-STaR, SPIN 등)은 "스스로 만든 답 중 맞은 것만 골라 다시 학습"이라는 같은 틀을 씁니다. 공통 조건은 자동으로 잴 수 있는 정답 신호입니다. 공통 실패는 초기 모델이 너무 약할 때, 반복을 늘릴 때의 과적합, 생성 데이터만 되풀이해 학습할 때의 분포 꼬리 소실입니다(3절).
- Stream of Search는 탐색 과정 전체(탐색, 막힘, 되돌아가기)를 글로 펼쳐 학습시킵니다. Countdown에서 최적 경로만 학습한 모델은 25.73%, 탐색 과정을 학습한 모델은 51.27%를 풀었습니다. STaR와 APA로 더 학습하면, 처음에 못 풀던 문제의 36%를 풉니다(4절).
- NVIDIA 연구(2026년 11월)는 하네스의 자동 요약 대신 모델이 직접 줄일 범위를 고르고, 원래 기록은 보관해 다시 꺼내게 했습니다. 32K 예산에서 GPT-6.1 Sol의 점수가 21%에서 56%로 올랐습니다. 그러나 같은 도구를 Claude Opus 5.5는 과제의 4%에서만 썼습니다(5절).
- 받은 의료 LLM 문헌 4편의 요약 수치(Bedi 5%, Soroush 50% 미만, Ferber 정확도 상승, NVIDIA 방법 설명)는 원문과 맞습니다. Bedi 논문의 온라인 게재는 2024년이고 권호는 2025년입니다(6절).
- 텍스트-SQL·EHR 질의 에이전트에는 다섯 가지를 권합니다. 잘린 결과에 잘림 표시와 다시 꺼내는 도구를 붙입니다. 빈 결과와 "기록 없음"을 구분합니다. 코드는 사전과 뷰에서 찾게 합니다. 정답률 밖에 답 못 함 판단과 calibration을 잽니다. self-training은 평가 문항과 분리한 합성 질문과 실행 결과 일치 필터로 합니다(7절).

## 1. 조사 범위와 방법

| 주제 | 본 문헌 |
|---|---|
| 텍스트-SQL self-training | EHRSQL 2024 1위 논문, 대회 개요 논문, SENSE, OmniSQL, SQL-R1, Reasoning-SQL |
| 일반 self-training | STaR, ReST, ReST-EM, RFT, V-STaR, Quiet-STaR, SPIN, Self-Rewarding |
| 에이전트 self-training | FireAct, ReST meets ReAct, SWE-Gym, SWE-smith |
| 최근 흐름 | DeepSeek-R1, model collapse(Nature 2024) |
| 탐색 학습 | Stream of Search, Searchformer |
| 문맥 관리 | NVIDIA, Letting Models Manage Their Own Context |
| 의료 LLM 평가·응용 | Bedi(JAMA), Soroush(NEJM AI), Ferber(Nature Cancer) |

## 2. EHRSQL 2024 1위 팀의 self-training(PLUQ)

### 2.1 대회 과제와 평가 지표

EHRSQL 2024는 NAACL 2024 ClinicalNLP 워크숍의 공유 과제입니다. 참가자는 자연어 질문을 MIMIC-IV demo DB의 SQL로 바꿉니다. DB로 답할 수 없는 질문에는 SQL 대신 null을 냅니다. 100명 이상이 신청했고, 8개 팀이 코드와 fact sheet까지 제출했습니다. [출처: https://arxiv.org/abs/2405.06673]

질문 템플릿은 국내 한 대학병원 의료진 200명 이상에게 받은 질문에서 나왔습니다. 학습, 검증, 시험 세트마다 답할 수 없는 질문이 20%입니다. 새로 만든 어려운 답 못 하는 질문은 검증과 시험 세트에만 넣었습니다. 학습 세트에 없는 SQL 유형도 검증과 시험 세트에 들어 있습니다. [출처: https://arxiv.org/html/2405.06673]

주 지표는 Reliability Score RS(c)입니다. 문항마다 아래 점수를 매기고 평균합니다. [출처: https://arxiv.org/html/2405.11162]

| 경우 | 점수 |
|---|---|
| 답할 수 있는 질문에 맞는 SQL을 냄 | 1 |
| 답할 수 있는 질문에 null을 냄 | 0 |
| 답할 수 있는 질문에 틀린 SQL을 냄 | -c |
| 답할 수 없는 질문에 SQL을 냄 | -c |
| 답할 수 없는 질문에 null을 냄 | 1 |

c는 0, 5, 10, N(문항 수)입니다. 순위는 RS(10)으로 정합니다. RS(10)에서는 틀린 답 하나가 맞는 답 10개를 지웁니다. 그래서 확신이 없으면 답하지 않는 쪽이 유리합니다.

### 2.2 방법

논문 제목은 "LG AI Research & KAIST at EHRSQL 2024: Self-Training Large Language Models with Pseudo-Labeled Unanswerable Questions for a Reliable Text-to-SQL System on EHRs"입니다. 저자는 Yongrae Jo, Seongyun Lee, Minju Seo, Sung Ju Hwang, Moontae Lee입니다. ClinicalNLP 2024 논문집 635~643쪽에 실렸습니다. [출처: https://aclanthology.org/2024.clinicalnlp-1.61/]

방법은 두 단계 self-training과 두 단계 필터입니다. [출처: https://arxiv.org/html/2405.11162]

1. 시드 모델 학습: GPT-3.5-Turbo-0125를 OpenAI 파인튜닝 API로 학습 세트 전체에 학습합니다. 입력에는 글로 바꾼 DB 스키마와 답 못 하는 질문의 기준을 넣습니다.
2. 의사 라벨: 시드 모델이 라벨 없는 검증·시험 질문마다 SQL 또는 null을 예측합니다. null로 예측한 질문 K개만 null 라벨로 학습 세트에 더합니다. 정답 SQL을 모르는 답할 수 있는 질문은 더하지 않습니다.
3. 재학습: 늘린 학습 세트로 모델을 다시 학습합니다. 반복은 한 번입니다.
4. 최대 token entropy 필터: 예측 안에서 entropy가 가장 큰 token의 값을 예측의 entropy로 정합니다. entropy 상위 7%를 null로 바꿉니다. 이 비율은 예상되는 답 못 하는 질문 비율에 맞춘 hyperparameter입니다.
5. 실행 필터: 남은 SQL을 sqlite3로 실행합니다. 오류가 나거나, 결과가 비었거나, None이면 null로 바꿉니다.

저자들은 self-training의 이유를 두 가지로 듭니다. 첫째, 학습 세트에 답 못 하는 질문이 적어 class 불균형이 있습니다. 둘째, 학습 질문과 검증·시험 질문의 embedding cosine 유사도 평균이 0.36과 0.34로 낮습니다. [출처: https://arxiv.org/html/2405.11162]

### 2.3 점수와 ablation

| 팀 | 시험 RS(0) | 시험 RS(10) | 시험 RS(N) |
|---|---|---|---|
| PLUQ(LG AI Research & KAIST) | 88.17 | 81.32 | -711.83 |
| PromptMind | 82.6 | 74.89 | -817.4 |
| ProbGate | 81.92 | 74.21 | -818.08 |
| KU-DMIS | 72.07 | 59.21 | -1427.93 |

값은 PLUQ 논문 Table 1에서 가져왔습니다. [출처: https://arxiv.org/html/2405.11162]

| 검증 세트 조건 | RS(0) | RS(10) |
|---|---|---|
| 파인튜닝만 | 83.23 | 73.77 |
| + 스키마 입력 | 89.85 | 77.82 |
| + 답 못 함 기준 입력(최종) | 90.37 | 88.65 |
| 필터 없음 | 80.82 | -69.94 |
| + 실행 필터 | 93.98 | 85.38 |
| + entropy 필터(최종) | 90.37 | 88.65 |
| Flan-T5-base 파인튜닝 | 82.11 | 70.94 |
| GPT-4-Turbo in-context learning(4-shot) | 63.52 | -301.22 |

값은 PLUQ 논문 Table 2~4에서 가져왔습니다. [출처: https://arxiv.org/html/2405.11162]

- 필터가 없으면 RS(10)이 음수입니다. 실행 필터 하나로 RS(10)이 85.38까지 오릅니다.
- 실행 필터만 쓰면 RS(0)은 가장 높지만 RS(10)은 entropy 필터를 더한 쪽이 높습니다. 불확실한 답을 더 버리면 맞는 답 일부를 잃는 대신 벌점이 줄어듭니다.
- 파인튜닝 없이 GPT-4-Turbo를 4-shot으로 쓰면 RS(10)이 -301.22입니다. 파인튜닝한 Flan-T5-base보다 낮습니다.
- 우승 팀도 RS(N)은 음수입니다. 저자들은 한계 절에서 실제 적용에 주의가 필요하다고 적었습니다.

### 2.4 다른 상위 팀의 방법

| 팀 | SQL 생성 | 답 못 함 판단 |
|---|---|---|
| PromptMind | 파인튜닝한 ChatGPT, GPT-4, Claude Opus의 앙상블. 일반·의료 retriever 2개로 비슷한 질문-SQL 예시를 가져옴 | 세 모델의 SQL이 모두 같을 때만 답함 |
| ProbGate | 파인튜닝한 ChatGPT | log-probability 임계값과 오류 처리. 임계값은 검증 세트의 답 못 함 비율로 정함 |
| KU-DMIS | 의사 질문-SQL 쌍을 만들어 시험 분포에 맞춘 뒤 ChatGPT 파인튜닝 | SQL을 여러 번 뽑아 서로 다르면 답하지 않음 |
| AIRI NLP | logistic regression 분류기, T5-3B 파인튜닝 | 분류기와 SQL 실행 가능 여부 |
| LTRC-IIITH | SQLCoder-7b-2 2개(분류용, 생성용) | log-probability와 실행 가능 여부 |

값은 대회 개요 논문 5.2절에서 가져왔습니다. [출처: https://arxiv.org/html/2405.06673]

상위 3팀은 모두 파인튜닝한 모델에 불확실성 신호를 붙여 답을 거릅니다. 신호는 entropy, log-probability, 모델 사이 합의입니다.

### 2.5 읽을 때 주의할 점

- self-training 단계만 뺀 ablation은 논문에 없습니다. Table 3과 4는 입력과 필터의 효과만 보여 줍니다. 그래서 RS 향상 중 의사 라벨 재학습의 몫은 확인할 수 없습니다. [출처: https://arxiv.org/html/2405.11162]
- 의사 라벨은 라벨 없는 검증·시험 질문 자체에 붙입니다. 정답은 쓰지 않지만 시험 입력 분포를 학습에 씁니다(transductive). 실제 서비스에서는 운영 중에 들어온 질문으로 같은 일을 합니다. 저자들도 실제 서비스에서는 사용자 질문을 쉽게 모을 수 있다는 점을 이유로 듭니다. [출처: https://arxiv.org/html/2405.11162]
- 실행 필터는 결과가 빈 SQL을 답 못 함으로 바꿉니다. 실제 EHR에는 "해당 기록 없음"이 맞는 답인 질문이 있습니다. 이런 질문에서는 빈 결과가 정답입니다(7.2절).
- 학습 세트 크기의 표기가 논문 안에서 다릅니다. 3.1절은 5,124개에 두 종류 질문이 모두 들어 있다고 씁니다. 3.2절은 답할 수 있는 질문이 5,124개이고 답 못 하는 질문이 450개라고 씁니다. [출처: https://arxiv.org/html/2405.11162]
- 더한 null 질문의 수 K는 논문에서 찾지 못했습니다.

## 3. 일반 self-training 문헌

### 3.1 공통 틀

대부분의 방법은 같은 순환을 씁니다. 모델이 답을 여러 개 만듭니다. 자동 신호로 답을 거릅니다. 남은 답으로 모델을 다시 학습합니다. 이 순환을 몇 번 되풀이합니다. 방법마다 다른 곳은 거르는 신호, 오답의 사용 여부, 학습 시작점입니다.

| 방법 | 거르는 신호 | 오답 사용 | 학습 시작점 |
|---|---|---|---|
| STaR | 최종 답 일치 | 정답을 힌트로 주고 다시 생성(rationalization) | 매번 처음 모델 |
| ReST | 보상 모델 점수 임계값(점점 높임) | 쓰지 않음 | 이전 반복 모델 |
| ReST-EM | 이진 정답 신호 | 쓰지 않음 | 매번 처음 모델 |
| RFT | 최종 답 일치, 서로 다른 추론 경로만 남김 | 쓰지 않음 | SFT 모델 |
| V-STaR | 최종 답 일치 | 정답·오답 쌍으로 DPO verifier 학습 | 반복 |
| SPIN | 사람이 쓴 SFT 데이터와 자기 답의 구분 | 자기 이전 답을 음성 예로 씀 | 이전 반복 모델 |
| Self-Rewarding | 모델 자신의 LLM-as-a-Judge 점수 | 선호 쌍으로 씀 | 이전 반복 모델(반복 DPO) |
| PLUQ | 모델의 null 예측 | 쓰지 않음 | 시드 모델 학습 후 한 번 재학습 |

### 3.2 방법별 정리

STaR(Zelikman et al., 2022). [출처: https://arxiv.org/abs/2203.14465]
- 몇 개의 예시로 rationale과 답을 만들고, 답이 맞은 rationale만 모아 학습합니다. 틀린 문제는 정답을 힌트로 주고 rationale을 다시 만듭니다(rationalization).
- 새 데이터를 모을 때마다 처음 사전학습 모델에서 다시 학습합니다. 저자들은 과적합을 피하려는 선택이라고 씁니다. [출처: https://ar5iv.labs.arxiv.org/html/2203.14465]
- CommonsenseQA에서 72.5%로, 30배 큰 파인튜닝 GPT-3의 73.0%와 비슷합니다. [출처: https://ar5iv.labs.arxiv.org/html/2203.14465]
- 한계: 첫 반복이 되려면 few-shot 성능이 우연보다 높아야 합니다. GPT-2는 산술에서도 시작하지 못했습니다. 맞은 예만 학습하므로, 못 푸는 문제에서는 신호를 얻지 못합니다. rationale의 정확성은 따로 확인하지 않습니다. [출처: https://ar5iv.labs.arxiv.org/html/2203.14465]

ReST(Gulcehre et al., 2023). [출처: https://arxiv.org/abs/2308.08998]
- Grow 단계에서 정책 모델로 샘플을 만들고, Improve 단계에서 보상으로 거른 데이터에 offline RL을 합니다. 데이터를 offline으로 만들어 다시 쓸 수 있으므로 online RLHF보다 효율적이라고 씁니다.
- 기계 번역에서 자동 지표와 사람 평가가 모두 올랐습니다.

ReST-EM(Singh et al., 2023, Beyond Human Data). [출처: https://arxiv.org/abs/2312.06585]
- 샘플 생성, 이진 정답 신호로 거르기, 학습을 몇 번 되풀이합니다. 매 반복 처음 사전학습 모델을 학습해 과제 과적합을 줄입니다. [출처: https://arxiv.org/html/2312.06585]
- PaLM 2로 MATH(학습 문제 7,500개)와 APPS Introductory(2,342개)에서 사람 데이터만으로 파인튜닝한 것보다 크게 좋았고, 모델이 클수록 효과가 컸습니다.
- 한계: 반복을 몇 번 넘기면 향상이 줄어듭니다. 저자들은 적은 학습 문제에 대한 과적합을 원인으로 듭니다. 새 과제마다 문제 세트와 자동 보상 함수가 필요합니다. [출처: https://arxiv.org/html/2312.06585]

RFT(Yuan et al., 2023). [출처: https://arxiv.org/abs/2308.01825]
- SFT 모델로 추론 경로를 샘플링하고, 맞은 경로를 학습 데이터에 더합니다. 서로 다른 추론 경로가 많을수록 효과가 큽니다. 약한 모델일수록 더 많이 오릅니다.
- 여러 모델의 rejection sample을 합치면 LLaMA-7B의 GSM8K 정답률이 SFT 35.9%에서 49.3%로 오릅니다.

V-STaR(Hosseini et al., 2024). [출처: https://arxiv.org/abs/2402.06457]
- STaR가 버리는 오답도 씁니다. 정답과 오답으로 DPO verifier를 학습하고, 추론 때 여러 후보 중 하나를 verifier로 고릅니다.
- LLaMA2로 코드 생성과 수학에서 기존 self-improvement·검증 방법보다 시험 정답률이 4~17% 높습니다.

Quiet-STaR(Zelikman et al., 2024). [출처: https://arxiv.org/abs/2403.09629]
- 질문-답 대신 일반 글의 token마다 생각을 만들고, 다음 글 예측에 도움이 된 생각을 학습합니다.
- 인터넷 글로 계속 사전학습한 뒤, 과제별 파인튜닝 없이 GSM8K 5.9%에서 10.9%, CommonsenseQA 36.3%에서 47.2%로 올랐습니다.

SPIN(Chen et al., 2024). [출처: https://arxiv.org/abs/2401.01335]
- SFT 모델에서 시작해, 이전 반복의 자기 답과 사람이 쓴 SFT 답을 구분하도록 학습합니다.
- 목적 함수의 최적점은 모델 분포가 목표 데이터 분포와 같을 때뿐이라고 증명합니다. 따라서 상한은 사람이 쓴 SFT 데이터의 분포입니다.

Self-Rewarding Language Models(Yuan et al., 2024). [출처: https://arxiv.org/abs/2401.10020]
- 모델이 LLM-as-a-Judge로 자기 답에 보상을 매기고 반복 DPO를 합니다. Llama 2 70B를 3번 반복하자 AlpacaEval 2.0에서 Claude 2, Gemini Pro, GPT-4 0613보다 높았습니다.

### 3.3 에이전트 self-training

| 연구 | 궤적 생성 | 거르는 신호 | 주요 수치 | 출처 |
|---|---|---|---|---|
| FireAct(2023) | GPT-4가 검색 API로 만든 QA 궤적 | 정답 궤적 | Llama2-7B에 궤적 500개로 HotpotQA 77% 향상 | https://arxiv.org/abs/2310.05915 |
| ReST meets ReAct(2023) | ReAct 에이전트의 이전 궤적 | AI feedback 순위 | 2번 반복 후 매개변수가 약 100분의 1인 모델이 비슷한 성능 | https://arxiv.org/abs/2312.10003 |
| SWE-Gym(2024) | 실행 환경이 있는 실제 Python 과제 2,438개 | 단위 시험 통과 | SWE-Bench 해결률 최대 19%p 향상, verifier와 함께 Verified 32.0%, Lite 26.0% | https://arxiv.org/abs/2412.21139 |
| SWE-smith(2025) | 코드베이스의 시험을 깨는 과제를 자동 합성, 128개 저장소에서 5만 개 | 시험 통과 궤적 | SWE-agent-LM-32B가 SWE-bench Verified Pass@1 40.2% | https://arxiv.org/abs/2504.21798 |

에이전트 쪽의 공통점은 실행 가능한 환경과 자동 판정(시험 통과, 정답 일치)입니다. 판정이 있으면 궤적을 대량으로 만들고 거를 수 있습니다.

### 3.4 텍스트-SQL의 합성 데이터와 RL

| 연구 | 방법 | 주요 수치 | 출처 |
|---|---|---|---|
| SENSE(2024) | 강한 모델이 만든 데이터와 약한 모델의 오류 데이터를 합침. 오류 데이터는 선호 학습에 씀 | SPIDER와 BIRD에서 당시 최고 성능 | https://arxiv.org/abs/2408.03256 |
| OmniSQL(2025) | 합성 DB 16,000개 이상에서 250만 개 질문-SQL-CoT 합성(SynSQL-2.5M) | 7B·14B·32B 모델이 9개 데이터셋에서 GPT-4o, DeepSeek-V3와 비슷하거나 높음 | https://arxiv.org/abs/2503.02240 |
| SQL-R1(2025) | NL2SQL 전용 보상으로 RL. 적은 합성 데이터와 cold start 영향 분석 | Spider 88.6%, BIRD 67.1% 실행 정확도 | https://arxiv.org/abs/2504.08600 |
| Reasoning-SQL(2025) | GRPO와 부분 보상(schema linking, AI feedback, n-gram 유사도, 문법 검사) | RL만 쓴 14B 모델이 BIRD에서 o3-mini보다 4%, Gemini-1.5-Pro-002보다 3% 높음. SFT보다 일반화가 좋음 | https://arxiv.org/abs/2503.23157 |

### 3.5 2025~2026년 흐름과 위험

- 검증 가능한 보상으로 RL: DeepSeek-R1은 사람이 쓴 추론 궤적 없이 RL만으로 추론 능력을 키웠다고 보고합니다. 큰 모델의 추론 패턴을 작은 모델에 옮길 수 있다고도 씁니다. 텍스트-SQL에서는 실행 결과 일치가 이 보상이 됩니다(SQL-R1, Reasoning-SQL). [출처: https://arxiv.org/abs/2501.12948]
- model collapse: 다른 모델이 만든 데이터로 가리지 않고 학습하면, 세대가 지나며 원래 분포의 꼬리부터 사라지고 행동이 한 점으로 모입니다. 분포의 꼬리가 중요한 과제에서는 사람이 만든 실제 데이터가 필요합니다. [출처: https://www.nature.com/articles/s41586-024-07566-y]
- 의료 질의에서 드문 질문 유형, 드문 코드, 드문 기록 형태가 이 꼬리에 해당합니다. self-training 데이터에는 실제 질문과 실제 DB 실행 결과를 계속 섞어야 합니다.

## 4. Stream of Search(SoS)

### 4.1 무엇을 학습시키나

논문은 Gandhi et al., "Stream of Search (SoS): Learning to Search in Language"(2024)입니다. 언어 모델은 학습 때 쓸모 있는 실수를 거의 보지 못하고, 그래서 오류가 눈덩이처럼 커진다는 문제에서 시작합니다. 저자들은 탐색 과정 전체를 한 줄의 글로 펼쳐 학습시킵니다. [출처: https://arxiv.org/abs/2404.03683]

- 과제: Countdown입니다. 입력 숫자들을 사칙연산으로 묶어 목표 숫자를 만듭니다. 24 게임을 넓힌 문제입니다.
- 직렬화: 탐색, 되돌아가기(backtracking), 목표 확인을 글로 명시합니다. heuristic 값, 상태 값, 가지치기 전략은 글에 쓰지 않습니다. [출처: https://arxiv.org/html/2404.03683]
- 데이터: BFS와 DFS를 바탕으로, 간단한 heuristic 함수 2개를 쓰는 탐색 전략 12개로 궤적을 만듭니다. 문제는 50만 개입니다. SoS 데이터에서 정답에 이른 궤적은 28만 5천 개이고, 최적 경로(OP) 데이터는 50만 개 모두 정답입니다. [출처: https://arxiv.org/html/2404.03683]
- 모델: GPT-Neo 250M, 문맥 4,096 token, 처음부터 사전학습합니다.

### 4.2 결과

| 조건 | 결과 | 출처 |
|---|---|---|
| 최적 경로만 학습(OP) | 보지 못한 입력에서 25.73% | https://arxiv.org/html/2404.03683 |
| 탐색 과정 학습(SoS) | 51.27% | https://arxiv.org/html/2404.03683 |
| SoS + STaR(expert iteration) | 3번 반복 후 수렴. 보지 못한 입력에서 SoS보다 약 5% 더 풂. 반복마다 정답 궤적 10만 개 생성 | https://arxiv.org/html/2404.03683 |
| SoS + APA | reference policy를 3번 재설정, SoS보다 약 6% 향상 | https://arxiv.org/html/2404.03683 |
| 처음에 못 풀던 문제 | 파인튜닝한 SoS 모델이 36%를 풂. 어느 heuristic solver도 못 푸는 문제도 포함 | https://arxiv.org/abs/2404.03683 |

- 정답 궤적 수가 더 적은 SoS 데이터가 더 좋은 모델을 만듭니다. 실수와 되돌아가기를 보여 준 것이 효과를 냅니다.
- 정책 개선 뒤에는 궤적당 산술 오류가 줄고, 맞은 풀이에서 방문한 상태 수도 줄었습니다. [출처: https://arxiv.org/html/2404.03683]

### 4.3 관련 연구

- Searchformer(Lehnert et al., 2024)는 A* 탐색의 진행(상태를 탐색 트리에 넣고 빼는 순서)을 token 열로 학습시킵니다. 보지 못한 Sokoban 문제의 93.7%를 최적으로 풀고, 학습에 쓴 A* 구현보다 탐색 단계를 최대 26.8% 적게 씁니다. [출처: https://arxiv.org/abs/2402.14083]

### 4.4 텍스트-SQL 에이전트 궤적과의 대응

| SoS | 텍스트-SQL·EHR 질의 에이전트 |
|---|---|
| 상태: 남은 숫자 | 지금까지 확인한 테이블, 열, 값, 중간 결과 |
| 행동: 두 숫자에 연산 적용 | 스키마 조회, 값 탐색 SQL, 최종 SQL 실행 |
| 목표 확인 | 결과가 질문 조건을 만족하는지 확인 |
| 되돌아가기 | SQL 오류나 빈 결과 뒤에 다른 테이블·조건으로 다시 시도 |
| 최적 경로만 학습(OP) | 최종 SQL만 학습 |
| 탐색 과정 학습(SoS) | 탐색·오류·수정이 담긴 궤적 전체 학습 |
| 정답 판정 | 실행 결과가 정답 결과와 같음 |

SoS의 결과에 따르면, 탐색과 복구가 담긴 궤적 전체를 학습한 모델이 최종 SQL만 학습한 모델보다 나을 것으로 예상합니다. 다만 SoS 궤적은 4,096 token 안에 들어가고, 에이전트 궤적은 도구 결과 때문에 훨씬 깁니다. 궤적을 학습 데이터로 쓰려면 긴 도구 결과를 줄이는 규칙(5절)이 함께 필요합니다.

## 5. 모델이 직접 문맥을 관리하는 방식(NVIDIA, 2026)

### 5.1 무엇을 비교했나

논문 제목은 "Letting Models Manage Their Own Context: Where We Stand"입니다. arXiv 2611.34147이고, 2026년 11월 25일에 제출되었습니다. 저자는 Alessio Devoto 외 NVIDIA 연구진입니다. [출처: https://arxiv.org/abs/2611.34147]

| 방식 | 언제 줄이나 | 무엇을 줄이나 | 원래 기록 |
|---|---|---|---|
| 하네스 주도 | 문맥 사용량이 예산의 80%에 이를 때 | 첫 지시와 최근 사건 10개를 빼고 모두 요약 | 남지 않음 |
| 모델 주도 | 모델이 정함. 85%부터 고려하라는 지시, 사용량 표시, 한계 근처 경고를 줌 | 모델이 고른 사건 범위를 모델이 쓴 요약으로 바꿈(collapse) | 보관함. 모델이 원래 tag로 다시 꺼냄 |

값은 논문 2~3절에서 가져왔습니다. [출처: https://arxiv.org/html/2611.34147v1]

시험 과제는 OfficeQA Pro v2(문서 조사 90문항)와 MLE-bench Lite(Kaggle 대회 22개)입니다. 문맥 예산은 8K~512K token입니다. 모델은 GPT-6.1 Sol, Kimi K3, DeepSeek V4 Pro, Claude Opus 5.5입니다. 문맥 관리용 추가 학습은 하지 않았습니다.

### 5.2 주요 결과

- OfficeQA Pro v2, 32K 예산에서 GPT-6.1 Sol의 점수는 하네스 주도 21%에서 모델 주도 56%로 올랐습니다. [출처: https://arxiv.org/abs/2611.34147]
- 효과는 예산이 작을수록 크고, 예산이 커지면 두 방식이 비슷해집니다. MLE-bench Lite에서는 가장 작은 예산에서만 효과가 보입니다. [출처: https://arxiv.org/html/2611.34147v1]
- 문맥 API를 한 번 이상 쓴 과제 비율은 GPT, Kimi, DeepSeek이 42~53%이고 Opus 5.5는 4%입니다. 경고를 받으면 Opus는 대개 바로 답을 내고 끝냅니다. [출처: https://arxiv.org/html/2611.34147v1]
- 보관한 원래 기록을 다시 꺼낸 비율은 compaction 호출 기준으로 GPT 19%, Kimi 7%, DeepSeek 3%입니다(하한값). GPT는 한 번에 요청 크기를 중앙값 3.7배 줄여 가장 많이 줄이고, 가장 자주 다시 꺼냅니다. [출처: https://arxiv.org/html/2611.34147v1]
- 85% 시점 지시를 빼면 Kimi와 DeepSeek은 훨씬 일찍 줄입니다. 128K 이상 예산에서 두 모델의 점수는 하네스 기준보다 약 8점 낮아졌습니다. 저자들은 이 현상을 context anxiety라고 부릅니다. [출처: https://arxiv.org/html/2611.34147v1]
- 32K 예산에서 Kimi K3의 모델 주도 방식은 누적 입력 token이 41% 적었고(3,600만 대 6,200만), 점수는 43% 대 41%였습니다. [출처: https://arxiv.org/html/2611.34147v1]
- 문맥을 고치면 고친 지점 뒤의 KV cache가 무효가 됩니다. 저자들은 바뀌지 않은 뒷부분의 KV cache를 다시 쓰는 SGLang 시제품으로 요청당 prefill 계산을 4~15% 줄였습니다. 정답률 변화는 측정 범위 안에서 보이지 않았습니다(Qwen3.6-27B, 32K). [출처: https://arxiv.org/html/2611.34147v1]

### 5.3 시사점

- 원래 기록을 지우지 않고 보관하고 tag로 다시 꺼내게 하면, 요약에서 빠진 정보를 모델이 되찾을 수 있습니다. GPT의 다시 꺼낸 비율 19%는 공격적으로 줄일수록 이 통로가 필요하다는 근거입니다.
- 도구를 준다고 모든 모델이 쓰지는 않습니다. 같은 도구와 지시에서 사용률이 4%에서 53%까지 다릅니다. 도구를 붙인 실험에서는 정답률과 함께 도구 사용률과 다시 꺼낸 비율을 잽니다.
- 언제 줄일지에 대한 지시 한 줄이 결과를 바꿉니다. 지시 문장도 실험 변수로 다룹니다.
- 저자들은 GPT의 좋은 결과에 학습이 기여했을 수 있다고 추정하고, 문맥 관리를 학습으로 가르치는 연구가 필요하다고 씁니다. 3절의 self-training을 문맥 관리 행동에도 적용할 수 있습니다. [출처: https://arxiv.org/html/2611.34147v1]

## 6. 받은 의료 LLM 문헌 4편의 수치 확인

| 문헌 | 받은 요약 | 원문 확인 결과 | 판정 |
|---|---|---|---|
| Devoto et al., arXiv 2611.34147 | 모델이 줄일 범위를 고르고, 원래 기록은 보관했다가 다시 꺼냄 | collapse로 범위를 요약하고, 원래 사건은 보관해 tag로 다시 꺼냄. 2026년 11월 25일 제출 | 맞음 |
| Bedi et al., JAMA | 519편 중 실제 환자 데이터로 평가한 연구는 5%. 대부분 정확도만 봄 | 519편 중 5%가 실제 환자 진료 데이터를 씀. 95.4%가 accuracy를 주 평가 차원으로 씀 | 맞음 |
| Soroush et al., NEJM AI 2024 | GPT-4도 ICD·CPT 코드를 정확히 맞힌 비율이 50% 미만 | GPT-4 exact match: ICD-9-CM 45.9%, ICD-10-CM 33.9%, CPT 49.8%. 시험한 4개 모델 중 가장 높음 | 맞음 |
| Ferber et al., Nature Cancer 2025 | 도구를 쓰는 에이전트로 정확도가 크게 오름 | 완전성 기준 정답률이 GPT-4 단독 30.3%에서 에이전트 87.2%로 오름 | 맞음 |

출처: [출처: https://arxiv.org/abs/2611.34147] [출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC11480901/] [출처: https://ai.nejm.org/doi/full/10.1056/AIdbp2300040] [출처: https://www.nature.com/articles/s43018-025-00991-6]

Bedi et al.(JAMA)의 세부 수치는 다음과 같습니다. [출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC11480901/]
- 대상은 2022년 1월 1일부터 2024년 2월 19일까지 나온 연구 519편입니다.
- 의료 과제는 의학 지식 평가(면허 시험 문제 등) 44.5%, 진단 19.5%가 많았습니다. 청구 코드 부여와 처방 작성은 각각 0.2%였습니다.
- NLP 과제는 질의응답이 84.2%였고, 요약 8.9%, 대화 3.3%였습니다.
- 평가 차원은 accuracy 95.4%, fairness·bias·toxicity 15.8%, 배포 고려 4.6%, calibration·uncertainty 1.2%였습니다.
- 온라인 게재는 2024년 10월 15일이고, 권호는 JAMA 2025;333(4):319-328입니다. 받은 요약의 "JAMA 2024"는 온라인 게재 연도입니다.

Soroush et al.(NEJM AI)의 세부 수치는 다음과 같습니다. 학술지 페이지는 이 조사 환경에서 본문이 열리지 않아, 같은 DOI의 Europe PMC 초록으로 확인했습니다. [출처: https://europepmc.org/search?query=10.1056%2FAIdbp2300040]
- GPT-3.5, GPT-4, Gemini Pro, Llama2-70b Chat에 코드 설명을 주고 코드를 만들게 했습니다. 한 의료 기관의 EHR에서 12개월 동안 쓰인 코드를 뽑았습니다. ICD-9-CM 7,697개, ICD-10-CM 15,950개, CPT 3,673개입니다.
- 틀린 코드 중 GPT-4는 같은 뜻의 다른 코드를 가장 많이 냈습니다(ICD-9-CM 7.0%, ICD-10-CM 10.9%).
- 저자들은 모든 모델이 부정확하거나 지어낸 정보를 담은 코드를 자주 만들었고, 추가 연구 없이 의료 코딩에 쓰기에 적절하지 않다고 결론 내렸습니다.

Ferber et al.(Nature Cancer)의 세부 수치는 다음과 같습니다. [출처: https://www.nature.com/articles/s43018-025-00991-6]
- GPT-4에 병리 슬라이드용 vision transformer(MSI, KRAS, BRAF 예측), 영상 분할용 MedSAM, OncoKB·PubMed·Google 검색을 도구로 붙였습니다.
- 현실적인 다중 모달 환자 사례 20개, 완전성 평가 문장 109개로 평가했습니다. 사람 전문가 4명이 눈가림 평가를 했습니다.
- 필요한 도구 호출 64번 중 56번을 맞게 써서 도구 사용 정확도가 87.5%입니다. 맞는 임상 결론은 91.0%, 관련 지침 인용은 75.5%입니다.

## 7. 텍스트-SQL·EHR 질의 에이전트에 주는 시사점

### 7.1 도구 결과가 잘리는 문제

EHR 질의 에이전트는 긴 결과를 자주 받습니다. 행이 많은 검사 결과, 긴 서술형 기록이 그 예입니다. 하네스가 결과를 일정 행이나 글자 수로 자르면, 모델은 뒷부분에 있던 기록을 못 보고 "기록 없음"이라고 답할 수 있습니다. 5절의 연구는 하네스가 대신 줄이면 필요한 정보가 빠질 수 있다는 같은 문제를 다룹니다.

권하는 설계는 다음과 같습니다.
1. 잘린 결과에는 잘렸다는 표시, 전체 행 수, 전체 길이를 함께 보여 줍니다.
2. 원래 결과는 지우지 않고 보관합니다. 결과마다 id를 붙이고, 모델이 id와 범위(행 번호, 글자 위치)로 잘린 부분을 다시 꺼내는 도구를 줍니다. NVIDIA 연구의 보관과 tag 조회와 같은 구조입니다.
3. SQL 에이전트에서는 다시 꺼내기 대신 같은 질의에 LIMIT, OFFSET, WHERE 조건을 붙여 다시 실행하게 할 수도 있습니다.
4. 잘린 결과만 보고 "없음"이라는 부정 결론을 내지 말라는 규칙을 시스템 지시에 넣습니다.
5. 도구 사용률을 잽니다. NVIDIA 연구에서 같은 도구를 Opus 5.5는 4%만 썼습니다. 모델이 도구를 잘 쓰지 않으면, 잘림 표시를 더 눈에 띄게 하거나 부정 결론 전에 하네스가 확인을 요구합니다.
6. 평가 지표에 잘린 결과 뒤의 부정 답 비율과 다시 꺼낸 비율을 넣습니다.

### 7.2 답 못 함 판단과 "기록 없음"

- EHRSQL 2024의 RS처럼 틀린 답에 벌점을 주는 지표로 평가하면, 답 못 함 판단의 가치가 점수에 드러납니다(2.1절).
- 상위 팀은 모두 불확실성 신호(token entropy, log-probability, 여러 샘플이나 여러 모델의 합의)로 답을 걸렀습니다. token 확률을 주지 않는 API 모델에서는 여러 번 샘플링한 SQL 결과의 합의가 쓸 수 있는 신호입니다(2.4절).
- "DB로 답할 수 없는 질문"과 "답할 수 있고 정답이 빈 결과인 질문"을 구분합니다. PLUQ의 실행 필터는 빈 결과를 답 못 함으로 바꿉니다. 실제 EHR에서 "해당 환자에게 그 검사 기록이 없음"은 맞는 답일 수 있습니다. 평가 세트에도 두 종류를 따로 넣습니다.

### 7.3 코드와 용어는 사전과 뷰에서 찾게 하기

GPT-4도 코드 설명에서 ICD-9-CM, ICD-10-CM, CPT 코드를 정확히 만든 비율이 50% 미만입니다(6절). 에이전트가 코드를 기억으로 만들지 않고, 코드 사전 테이블이나 뷰를 조회해 찾게 합니다. 사전 조회 결과가 없으면 코드를 지어내지 말고 그 사실을 답에 적게 합니다.

### 7.4 평가 설계

- 실제 환자 데이터(또는 실제 EHR 구조의 DB)로 평가합니다. Bedi et al.이 본 519편 중 5%만 실제 진료 데이터를 썼습니다.
- 정답률 밖의 차원을 잽니다. calibration·uncertainty를 잰 연구는 1.2%뿐입니다. 답 못 함 판단, 확신도와 정답의 관계, 도구 사용 정확도를 함께 잽니다.
- Ferber et al.처럼 도구 호출의 정확도(필요한 도구를 맞게 불렀는지)와 최종 결론의 정확도를 따로 잽니다.

### 7.5 self-training을 적용한다면

1. 학습 질문: 평가 문항으로 학습하지 않습니다. 평가와 분리한 합성 질문을 템플릿이나 강한 모델로 만듭니다(KU-DMIS, OmniSQL). 실제 운영 질문을 쓸 때는 평가 세트와 겹치지 않게 분리합니다.
2. 궤적 생성: 에이전트가 각 질문을 여러 번 풉니다. 스키마 탐색, SQL 오류, 수정이 담긴 궤적 전체를 남깁니다(SoS).
3. 거르기: 최종 SQL의 실행 결과가 정답 SQL의 실행 결과와 같은 궤적만 남깁니다(STaR, RFT, ReST-EM). 답 못 하는 질문은 null 라벨로 따로 늘려 class 불균형을 줄입니다(PLUQ).
4. 오답 궤적: 버리지 않고 verifier나 선호 학습에 씁니다(V-STaR, SENSE).
5. 학습: LoRA나 QLoRA 같은 parameter-efficient 파인튜닝으로 합니다. 반복은 2~3회로 두고, 매 반복 처음 모델에서 다시 학습합니다(STaR, ReST-EM). 생성 데이터만 되풀이하지 않고 실제 질문과 실제 실행 결과를 섞습니다(model collapse).
6. 문맥 관리 행동: 긴 결과를 줄이고 다시 꺼낸 궤적 중 정답에 이른 것을 학습 데이터에 넣으면, 5절에서 저자들이 말한 문맥 관리 학습이 됩니다.

LoRA와 QLoRA의 원 논문은 다음과 같습니다. [출처: https://arxiv.org/abs/2106.09685] [출처: https://arxiv.org/abs/2305.14314]

## 8. 확인 못 한 것

- PLUQ의 K 값과, self-training 단계만의 효과는 논문에서 찾지 못했습니다.
- NEJM AI와 JAMA의 학술지 페이지는 이 조사 환경에서 본문이 열리지 않았습니다. 같은 논문을 Europe PMC 초록과 PMC 본문으로 확인했습니다.
- SENSE의 구체적 점수는 초록에 없어 적지 않았습니다.
