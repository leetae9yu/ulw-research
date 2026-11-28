---
title: 에이전트 self-training과 모델 주도 문맥 관리 문헌 조사
subtitle: 텍스트-SQL·EHR 질의 에이전트
summary: EHRSQL 2024 1위 self-training, STaR·ReST 계열, Stream of Search, NVIDIA 모델 주도 문맥 관리를 논문 본문·표·appendix 기준으로 정리하고 의료 LLM 문헌 4편의 수치를 대조했습니다.
created: 2026-11-28
updated: 2026-11-28
---

# 에이전트 self-training과 모델 주도 문맥 관리 문헌 조사

조사 기준일: 2026년 11월 28일. 공개 논문과 공개 페이지만 사용했습니다. 수치는 초록 대신 논문 본문, 표, 그림, appendix와 대조했습니다. 수치마다 출처 뒤에 본 위치(절, 표, 그림 번호)를 적었습니다. 본문을 열지 못한 논문은 1.2절과 8절에 어디까지 봤는지 적었습니다.

## 0. 요약

- EHRSQL 2024 공유 과제 1위는 LG AI Research & KAIST의 PLUQ입니다. 이 팀은 GPT-3.5-Turbo를 파인튜닝했습니다. 그다음 라벨 없는 질문 중 모델이 "답 못 함"으로 예측한 것만 null 라벨로 더해 한 번 더 학습했습니다. 시험 세트 RS(10)은 81.32로, 2위보다 6.43점 높습니다(2절).
- PLUQ 점수의 큰 부분은 필터에서 나옵니다. 검증 세트에서 필터가 없으면 RS(10)은 -69.94이고, 실행 필터와 최대 token entropy 필터를 더하면 88.65입니다. 더한 null 질문의 수 K와 self-training 단계만의 효과는 arXiv판과 ACL Anthology판 본문 어디에도 없습니다. 두 판 모두 appendix가 없습니다(2.3절, 2.5절).
- 대회 학습 세트의 답 못 하는 질문 비율은 8.8%(5,124개 중 450개)이고, 20%보다 훨씬 낮습니다. 검증과 시험 세트만 약 20%입니다. PLUQ가 self-training으로 줄이려 한 class 불균형은 이 차이에서 나옵니다(2.1절).
- 일반 self-training 문헌(STaR, ReST, ReST-EM, RFT, V-STaR, SPIN 등)은 "스스로 만든 답 중 맞은 것만 골라 다시 학습"이라는 같은 틀을 씁니다. 공통 조건은 자동으로 잴 수 있는 정답 신호입니다. 본문 표에서 확인한 공통 실패는 세 가지입니다. 반복할수록 향상이 줄어듭니다(SPIN +2.66에서 +0.19). 강한 모델에서는 효과가 없습니다(RFT 33B). 생성 데이터만 되풀이하면 분포 꼬리가 사라집니다(3절).
- Stream of Search는 탐색 과정 전체(탐색, 막힘, 되돌아가기)를 글로 펼쳐 학습시킵니다. Countdown에서 최적 경로만 학습한 모델은 25.73%, 탐색 과정을 학습한 모델은 51.27%를 풀었습니다. STaR와 APA로 더 학습하면 55.59%와 56.52%입니다(4절).
- NVIDIA 연구(2026년 11월)는 하네스의 자동 요약 대신 모델이 직접 줄일 범위를 고르고, 원래 기록은 보관해 다시 꺼내게 했습니다. 32K 예산에서 GPT-6.1 Sol의 점수가 21%에서 56%로 올랐습니다. 그러나 같은 도구를 Claude Opus 5.5는 과제의 4%에서만 썼습니다. 경고를 받은 Opus는 88%의 경우 바로 답을 냈습니다(5절).
- 받은 의료 LLM 문헌 4편의 요약 수치는 원문과 맞습니다. Ferber 논문의 91.0%는 평가 문장 245개 중 223개가 맞았다는 뜻이고, 사례 비율이 아닙니다. Soroush 논문(NEJM AI)은 학술지 본문을 열지 못해 최종판 초록으로만 확인했습니다(6절).
- 텍스트-SQL·EHR 질의 에이전트에는 다섯 가지를 권합니다. 잘린 결과에 잘림 표시와 다시 꺼내는 도구를 붙입니다. 빈 결과와 "기록 없음"을 구분합니다. 코드는 사전과 뷰에서 찾게 합니다. 정답률 밖에 답 못 함 판단과 calibration을 잽니다. self-training은 평가 문항과 분리한 합성 질문과 실행 결과 일치 필터로 합니다(7절).

## 1. 조사 범위와 방법

### 1.1 주제별 문헌

| 주제 | 본 문헌 |
|---|---|
| 텍스트-SQL self-training | EHRSQL 2024 1위 논문, 대회 개요 논문, SENSE, OmniSQL, SQL-R1, Reasoning-SQL |
| 일반 self-training | STaR, ReST, ReST-EM, RFT, V-STaR, Quiet-STaR, SPIN, Self-Rewarding |
| 에이전트 self-training | FireAct, ReST meets ReAct, SWE-Gym, SWE-smith |
| 최근 흐름 | DeepSeek-R1, model collapse(Nature 2024) |
| 탐색 학습 | Stream of Search, Searchformer |
| 문맥 관리 | NVIDIA, Letting Models Manage Their Own Context |
| 의료 LLM 평가·응용 | Bedi(JAMA), Soroush(NEJM AI), Ferber(Nature Cancer) |

### 1.2 논문별로 읽은 범위

arXiv 논문은 PDF를 내려받아 텍스트로 바꾼 뒤 본문, 표, 그림 설명, appendix를 읽었습니다. 표의 "appendix"는 PDF에 appendix가 있을 때 그 부분까지 읽었다는 뜻입니다.

| 논문 | 읽은 판 | 읽은 범위 |
|---|---|---|
| PLUQ | arXiv 2405.11162 PDF, ACL Anthology 2024.clinicalnlp-1.61 PDF | 본문 전체. 두 판 모두 appendix 없음 |
| EHRSQL 2024 개요 | arXiv 2405.06673 PDF | 본문, Appendix A |
| SENSE | arXiv 2408.03256 PDF | 본문, Table 1~6 |
| OmniSQL | arXiv 2503.02240 PDF | 본문, Table 1~6, 각주 |
| SQL-R1 | arXiv 2504.08600 PDF | 본문, Appendix B(Table 7~10) |
| Reasoning-SQL | arXiv 2503.23157 PDF | 본문, Table 1~5 |
| STaR, ReST, ReST-EM, RFT, V-STaR, Quiet-STaR, SPIN, Self-Rewarding | arXiv PDF | 본문, 그림, appendix |
| FireAct, ReST meets ReAct, SWE-Gym, SWE-smith | arXiv PDF | 본문, appendix |
| DeepSeek-R1 | arXiv 2501.12948 PDF | 본문, 부록 |
| model collapse | arXiv 2305.17493 PDF(Nature 게재 전 프리프린트) | 프리프린트 본문. Nature 게재판 본문은 따로 대조하지 않음 |
| Stream of Search | arXiv 2404.03683 PDF | 본문, Appendix C, Table 1~2 |
| Searchformer | arXiv 2402.14083 PDF | 본문 |
| NVIDIA 문맥 관리 | arXiv 2611.34147 PDF | 본문 전체, 8절 한계 |
| Bedi(JAMA) | PMC 본문 | 본문, Table 1~2. Supplement(eTable)는 내려받기가 막혀 못 봄 |
| Soroush(NEJM AI) | Europe PMC 최종판 초록, medRxiv 2023 프리프린트 본문 | 최종판 본문은 못 봄. 프리프린트는 GPT-3.5·GPT-4와 ICD만 다룬 이전 판이라 수치 근거로 쓰지 않음 |
| Ferber(Nature Cancer) | Nature 본문(Open Access), Supplementary Information PDF | 본문, 그림, 보충 자료 |

## 2. EHRSQL 2024 1위 팀의 self-training(PLUQ)

### 2.1 대회 과제와 평가 지표

EHRSQL 2024는 NAACL 2024 ClinicalNLP 워크숍의 공유 과제입니다. 참가자는 자연어 질문을 MIMIC-IV demo DB의 SQL로 바꿉니다. demo DB에는 환자 100명의 기록이 있고, 스키마는 전체 MIMIC-IV와 같습니다. DB로 답할 수 없는 질문에는 SQL 대신 null을 냅니다. 100명 이상이 신청했고, 8개 팀이 코드와 fact sheet까지 제출했습니다. [출처: https://arxiv.org/pdf/2405.06673, 3.2절, 5.1절]

질문 템플릿은 국내 한 대학병원 의료진 200명 이상에게 받은 질문에서 나왔습니다. 원래 EHRSQL의 답 못 하는 질문은 쉽게 걸러졌기 때문에, 대회는 TrustSQL의 적대적인 답 못 하는 질문을 더했습니다. 이 새 질문은 검증과 시험 세트에만 넣었습니다. [출처: https://arxiv.org/pdf/2405.06673, 3.1절, 3.4절]

| 구분 | 학습 | 검증 | 시험 |
|---|---|---|---|
| 답할 수 있는 질문 템플릿 | 100(모두 학습에 있음) | 134(100 + 학습에 없는 34) | 134(100 + 학습에 없는 34) |
| 답할 수 있는 질문 | 4,674 | 931 | 934 |
| 답할 수 없는 질문 | 450 | 232 | 233 |
| 합계 | 5,124 | 1,163 | 1,167 |
| 답할 수 없는 비율(계산값) | 8.8% | 19.9% | 20.0% |

값은 대회 개요 논문 Table 1에서 가져왔고, 마지막 줄은 그 값으로 계산했습니다. [출처: https://arxiv.org/pdf/2405.06673, Table 1]

개요 논문 3.5절은 "각 분할에 답할 수 없는 질문이 20%"라고 씁니다. 그러나 같은 논문 Table 1에서 학습 세트의 비율은 8.8%입니다. 이 보고서는 Table 1의 값을 따릅니다.

주 지표는 Reliability Score RS(c)입니다. 문항마다 아래 점수를 매기고 평균합니다. [출처: https://arxiv.org/pdf/2405.06673, 4.1절 식 (1)] [출처: https://arxiv.org/pdf/2405.11162, Figure 2]

| 경우 | 점수 |
|---|---|
| 답할 수 있는 질문에 맞는 SQL을 냄 | 1 |
| 답할 수 있는 질문에 null을 냄 | 0 |
| 답할 수 있는 질문에 틀린 SQL을 냄 | -c |
| 답할 수 없는 질문에 SQL을 냄 | -c |
| 답할 수 없는 질문에 null을 냄 | 1 |

c는 0, 5, 10, N(문항 수)입니다. 순위는 RS(10)으로 정합니다. RS(10)에서는 틀린 답 하나가 맞는 답 10개를 지웁니다. 모든 질문에 답하지 않으면 답 못 하는 질문 비율만큼인 20점을 받습니다. 대회는 이 ABSTAIN-ALL을 기준선으로 씁니다. 가능한 최저점은 RS(10)에서 -1000점, RS(N)에서 -100N점입니다. [출처: https://arxiv.org/pdf/2405.06673, 4.1절, 4.3절, Table 3]

### 2.2 방법

논문 제목은 "LG AI Research & KAIST at EHRSQL 2024: Self-Training Large Language Models with Pseudo-Labeled Unanswerable Questions for a Reliable Text-to-SQL System on EHRs"입니다. 저자는 Yongrae Jo, Seongyun Lee, Minju Seo, Sung Ju Hwang, Moontae Lee입니다. ClinicalNLP 2024 논문집 635~643쪽에 실렸습니다. [출처: https://aclanthology.org/2024.clinicalnlp-1.61/]

방법은 두 단계 self-training과 두 단계 필터입니다. [출처: https://arxiv.org/pdf/2405.11162, 3절, Figure 1]

1. 시드 모델 학습: GPT-3.5-Turbo-0125를 OpenAI 파인튜닝 API로 학습 세트 전체에 학습합니다. 입력에는 글로 바꾼 DB 스키마와 답 못 하는 질문의 기준을 넣습니다(Figure 3).
2. 의사 라벨: 시드 모델이 라벨 없는 검증·시험 질문마다 SQL 또는 null을 예측합니다. null로 예측한 질문 K개만 null 라벨로 학습 세트에 더합니다. 정답 SQL을 모르는 답할 수 있는 질문은 더하지 않습니다.
3. 재학습: 늘린 학습 세트로 모델을 다시 학습합니다. 반복은 한 번입니다.
4. 최대 token entropy 필터: 예측 안에서 entropy가 가장 큰 token의 값을 예측의 entropy로 정합니다. entropy 상위 7%를 null로 바꿉니다. 이 비율은 예측할 세트의 답 못 하는 질문 비율에 맞춘 hyperparameter입니다(Table 4 설명).
5. 실행 필터: 남은 SQL을 sqlite3로 실행합니다. 오류가 나거나, 결과가 비었거나, None이면 null로 바꿉니다.

저자들은 self-training의 이유를 두 가지로 듭니다. 첫째, 학습 세트에 답 못 하는 질문이 적어 class 불균형이 있습니다. 둘째, OpenAI text-embedding-3-large로 잰 학습 질문과 검증·시험 질문의 embedding cosine 유사도 평균이 0.36과 0.34로 낮습니다. [출처: https://arxiv.org/pdf/2405.11162, 3.2절]

### 2.3 점수와 ablation

| 팀 | 검증 RS(0) | 검증 RS(10) | 시험 RS(0) | 시험 RS(5) | 시험 RS(10) | 시험 RS(N) |
|---|---|---|---|---|---|---|
| PLUQ(LG AI Research & KAIST) | 90.37 | 88.65 | 88.17 | 84.75 | 81.32 | -711.83 |
| PromptMind | 66.38 | 52.62 | 82.6 | 78.75 | 74.89 | -817.4 |
| ProbGate | 84.18 | 74.72 | 81.92 | 78.06 | 74.21 | -818.08 |
| KU-DMIS | 91.57 | 74.38 | 72.07 | 65.64 | 59.21 | -1427.93 |

값은 PLUQ 논문 Table 1에서 가져왔습니다. PLUQ의 검증 점수는 공식 순위표에 올리지 않은 값입니다. [출처: https://arxiv.org/pdf/2405.11162, Table 1]

- 검증 세트에서는 KU-DMIS의 RS(0)이 91.57로 PLUQ보다 높았습니다. 그러나 RS(10)은 74.38이고, 시험 세트에서는 RS(10)이 59.21로 떨어졌습니다. 맞힌 수보다 틀린 답의 수가 순위를 정합니다.
- 개요 논문도 RS(0)과 RS(10)의 차이가 작은 팀이 높은 순위에 있다고 정리합니다. [출처: https://arxiv.org/pdf/2405.06673, 5.2절]

| 검증 세트 조건 | RS(0) | RS(5) | RS(10) | RS(N) | 표 |
|---|---|---|---|---|---|
| 파인튜닝만 | 83.23 | 78.5 | 73.77 | -1016.7 | Table 3 |
| + 스키마 입력 | 89.85 | 83.83 | 77.82 | -1310.1 | Table 3 |
| + 답 못 함 기준 입력(최종) | 90.37 | 89.51 | 88.65 | -109.6 | Table 3 |
| 필터 없음 | 80.82 | 5.58 | -69.94 | -17419.1 | Table 4 |
| + 실행 필터 | 93.98 | 89.68 | 85.38 | -906.01 | Table 4 |
| + entropy 필터(최종) | 90.37 | 89.51 | 88.65 | -109.6 | Table 4 |
| Flan-T5-base 파인튜닝 | 82.11 | 76.53 | 70.94 | -1217.8 | Table 2 |
| Tulu-7b 파인튜닝 | 10.23 | -38.77 | -87.9 | -11389.7 | Table 2 |
| GPT-4-Turbo-Preview in-context learning(4-shot) | 63.52 | -118.85 | -301.22 | -186836.4 | Table 2 |

[출처: https://arxiv.org/pdf/2405.11162, Table 2, Table 3, Table 4]

- 필터가 없으면 RS(10)이 음수입니다. 실행 필터 하나로 RS(10)이 85.38까지 오릅니다.
- 실행 필터만 쓰면 RS(0)은 가장 높지만 RS(10)은 entropy 필터를 더한 쪽이 높습니다. 불확실한 답을 더 버리면 맞는 답 일부를 잃는 대신 벌점이 줄어듭니다. RS(N)은 -906.01에서 -109.6으로 줄어듭니다.
- 파인튜닝 없이 GPT-4-Turbo를 4-shot으로 쓰면 RS(10)이 -301.22입니다. 파인튜닝한 Flan-T5-base보다 낮습니다. 매개변수가 더 많은 Tulu-7b는 파인튜닝해도 Flan-T5-base보다 낮습니다.
- 우승 팀도 RS(N)은 음수입니다. 저자들은 한계 절에서 실제 적용에 주의가 필요하다고 적었습니다. 개요 논문도 RS(N)이 양수인 팀은 없다고 씁니다. [출처: https://arxiv.org/pdf/2405.11162, Limitations] [출처: https://arxiv.org/pdf/2405.06673, 5.2절]

### 2.4 다른 상위 팀의 방법

| 팀 | SQL 생성 | 답 못 함 판단 |
|---|---|---|
| PromptMind | 파인튜닝한 ChatGPT, GPT-4, Claude Opus의 앙상블. 일반·의료 retriever 2개로 비슷한 질문-SQL 예시를 가져옴 | 세 모델의 SQL이 모두 같을 때만 답함 |
| ProbGate | 파인튜닝한 ChatGPT | log-probability 임계값과 오류 처리. 임계값은 검증 세트의 답 못 함 비율로 정함 |
| KU-DMIS | 의사 질문-SQL 쌍을 만들어 시험 분포에 맞춘 뒤 ChatGPT 파인튜닝 | SQL을 여러 번 뽑아 서로 다르면 답하지 않음 |
| AIRI NLP | logistic regression 분류기, T5-3B 파인튜닝 | 분류기와 SQL 실행 가능 여부 |
| LTRC-IIITH | SQLCoder-7b-2 2개(분류용, 생성용) | log-probability와 실행 가능 여부 |

값은 대회 개요 논문 5.2절과 Table 3에서 가져왔습니다. [출처: https://arxiv.org/pdf/2405.06673, 5.2절, Table 3]

상위 4팀은 모두 파인튜닝한 모델 하나로 SQL 생성과 답 못 함 판단을 같이 하는 unified 방식입니다. 5~7위 팀은 분류기, 생성기, 오류 검출기를 잇는 pipeline 방식입니다. 상위 팀은 모두 불확실성 신호(entropy, log-probability, 모델 사이 합의)로 답을 거릅니다.

### 2.5 읽을 때 주의할 점

- self-training 단계만 뺀 ablation은 논문에 없습니다. Table 2는 모델, Table 3은 입력, Table 4는 필터의 효과만 보여 줍니다. 그래서 RS 향상 중 의사 라벨 재학습의 몫은 확인할 수 없습니다. 더한 null 질문의 수 K는 Figure 1과 그 설명에 기호로만 나오고 값이 없습니다. arXiv판과 ACL Anthology판 모두 같으며, 두 판에 appendix가 없습니다. [출처: https://arxiv.org/pdf/2405.11162, Figure 1, Table 2~4] [출처: https://aclanthology.org/2024.clinicalnlp-1.61.pdf, Figure 1]
- 의사 라벨은 라벨 없는 검증·시험 질문 자체에 붙입니다. 정답은 쓰지 않지만 시험 입력 분포를 학습에 씁니다(transductive). 저자들은 실제 서비스에서는 사용자 질문을 쉽게 모을 수 있다는 점을 이유로 듭니다. [출처: https://arxiv.org/pdf/2405.11162, 1절, 3.2절] 대회 주최 측은 시험 시점 의사 라벨 파인튜닝이 고정된 벤치마크에서는 효과적이지만 실시간 배포에 바로 적용하기는 어려울 수 있다고 평가했습니다. [출처: https://arxiv.org/pdf/2405.06673, 5.2절 관찰 5]
- 실행 필터는 결과가 빈 SQL을 답 못 함으로 바꿉니다. 실제 EHR에는 "해당 기록 없음"이 맞는 답인 질문이 있습니다. 이런 질문에서는 빈 결과가 정답입니다(7.2절). OmniSQL도 EHRSQL로 평가할 때 답 못 하는 질문과 결과가 빈 질문을 빼고 평가했습니다(3.4절).
- PLUQ 논문 안에서 학습 세트 크기의 표기가 다릅니다. 3.1절과 4.1절은 두 종류 질문을 합쳐 5,124개라고 쓰고, 3.2절은 답할 수 있는 질문이 5,124개이고 답 못 하는 질문이 450개라고 씁니다. 개요 논문 Table 1에 따르면 답할 수 있는 질문 4,674개와 답 못 하는 질문 450개를 합쳐 5,124개입니다. 3.2절의 5,124는 합계를 잘못 옮긴 값입니다. [출처: https://arxiv.org/pdf/2405.11162, 3.1절, 3.2절, 4.1절] [출처: https://arxiv.org/pdf/2405.06673, Table 1]
- Table 2 설명은 "모델 3개"라고 쓰지만 표에는 4개가 있습니다. [출처: https://arxiv.org/pdf/2405.11162, 4.3절]

## 3. 일반 self-training 문헌

### 3.1 공통 틀

대부분의 방법은 같은 순환을 씁니다. 모델이 답을 여러 개 만듭니다. 자동 신호로 답을 거릅니다. 남은 답으로 모델을 다시 학습합니다. 이 순환을 몇 번 되풀이합니다. 방법마다 다른 곳은 거르는 신호, 오답의 사용 여부, 학습 시작점입니다.

| 방법 | 거르는 신호 | 오답 사용 | 학습 시작점 |
|---|---|---|---|
| STaR | 최종 답 일치 | 정답을 힌트로 주고 다시 생성(rationalization) | 매번 처음 모델 |
| ReST | 보상 모델 점수 임계값(점점 높임) | 쓰지 않음 | 이전 반복 모델 |
| ReST-EM | 이진 정답 신호 | 쓰지 않음 | 매번 처음 모델 |
| RFT | 최종 답 일치, 서로 다른 추론 경로만 남김 | 쓰지 않음 | SFT 모델 |
| V-STaR | 최종 답 일치 | 정답·오답 쌍으로 DPO verifier 학습 | 매번 처음 모델 |
| SPIN | 사람이 쓴 SFT 데이터와 자기 답의 구분 | 자기 이전 답을 음성 예로 씀 | 이전 반복 모델 |
| Self-Rewarding | 모델 자신의 LLM-as-a-Judge 점수 | 선호 쌍으로 씀 | 이전 반복 모델(반복 DPO) |
| PLUQ | 모델의 null 예측 | 쓰지 않음 | 시드 모델 학습 후 한 번 재학습 |

[출처: https://arxiv.org/pdf/2203.14465, 3절 Algorithm 1] [출처: https://arxiv.org/pdf/2308.08998, 2절] [출처: https://arxiv.org/pdf/2312.06585, 3절] [출처: https://arxiv.org/pdf/2308.01825, 3.3절] [출처: https://arxiv.org/pdf/2402.06457, Table 1, Figure 1] [출처: https://arxiv.org/pdf/2401.01335, 4절] [출처: https://arxiv.org/pdf/2401.10020, 2절]

### 3.2 방법별 정리

STaR(Zelikman et al., 2022).
- 몇 개의 예시로 rationale과 답을 만들고, 답이 맞은 rationale만 모아 학습합니다. 틀린 문제는 정답을 힌트로 주고 rationale을 다시 만듭니다(rationalization).
- 새 데이터를 모을 때마다 처음 사전학습 모델에서 다시 학습합니다. 저자들은 과적합을 피하려는 선택이라고 씁니다. [출처: https://arxiv.org/pdf/2203.14465, 3.1절]

| CommonsenseQA 검증 세트 | 정확도(%) | 사용한 학습 데이터(%) |
|---|---|---|
| GPT-3 직접 파인튜닝 | 73.0 | 100 |
| GPT-J few-shot CoT | 36.6 | 약 0 |
| LaMDA 137B few-shot CoT | 55.6 | 약 0 |
| GPT-J 직접 파인튜닝 | 60.0 | 100 |
| STaR, rationalization 없음 | 68.8 | 69.7 |
| STaR, rationalization 있음 | 72.5 | 86.7 |

[출처: https://arxiv.org/pdf/2203.14465, Table 1]

- 한계: 첫 반복이 되려면 few-shot 성능이 우연보다 높아야 합니다. GPT-2는 산술에서도 시작하지 못했습니다. 이진 선택처럼 우연히 맞힐 확률이 높은 과제에서는 나쁜 rationale이 많이 섞입니다. rationale 자체의 정확성은 따로 확인하지 않습니다. [출처: https://arxiv.org/pdf/2203.14465, 6절 한계 단락]

ReST(Gulcehre et al., 2023).
- Grow 단계에서 정책 모델로 샘플을 만들고, Improve 단계에서 보상으로 거른 데이터에 offline RL을 합니다. Grow 단계의 데이터를 여러 Improve 단계에서 다시 쓰므로 online RLHF보다 계산이 적다고 씁니다. [출처: https://arxiv.org/pdf/2308.08998, 1절, 2절]
- 기계 번역(IWSLT 2014, WMT 2020, 내부 Web Domain)에서 보상 모델 점수와 사람 평가가 모두 지도 학습 기준보다 좋았습니다. 보고서에 옮긴 수치는 없습니다. [출처: https://arxiv.org/pdf/2308.08998, 4절]

ReST-EM(Singh et al., 2023, Beyond Human Data).
- 샘플 생성, 이진 정답 신호로 거르기, 학습을 몇 번 되풀이합니다. 매 반복 처음 사전학습 모델을 학습해 과제 과적합을 줄입니다. [출처: https://arxiv.org/pdf/2312.06585, 3절]
- PaLM 2로 MATH(학습 문제 7,500개)와 APPS Introductory(2,342개)에서 사람 데이터로 파인튜닝한 것보다 좋았고, 큰 모델(PaLM 2-L)에서 차이가 컸습니다. 결과는 그림으로만 나옵니다. [출처: https://arxiv.org/pdf/2312.06585, 4절, Figure 2, Figure 3]
- 이전 반복 모델에서 이어 학습하는 ReST와 비교하면, APPS 점수는 비슷하지만 HumanEval 전이는 ReST-EM이 훨씬 좋았습니다. 처음 모델에서 다시 학습하는 선택의 근거입니다. [출처: https://arxiv.org/pdf/2312.06585, Figure 7]
- 사람이 쓴 풀이 7천 개로 한 SFT보다 생성 풀이 5천 개로 한 ReST-EM이 MATH에서 높았습니다. [출처: https://arxiv.org/pdf/2312.06585, Figure 6]
- 한계: 반복을 몇 번 넘기면 향상이 줄어듭니다. 학습 세트 점수와 시험 세트 점수의 차이가 반복마다 벌어지며, 저자들은 적은 학습 문제에 대한 과적합을 원인으로 듭니다. 새 과제마다 문제 세트와 자동 보상 함수가 필요합니다. [출처: https://arxiv.org/pdf/2312.06585, Figure 4, 6절]
- Big-Bench Hard에서는 큰 성능 저하가 없었습니다. [출처: https://arxiv.org/pdf/2312.06585, Figure 9]

RFT(Yuan et al., 2023).
- SFT 모델로 추론 경로를 100번 샘플링하고, 맞은 경로 중 서로 다른 것만 학습 데이터에 더합니다. 서로 다른 추론 경로가 많을수록 효과가 큽니다. 약한 모델일수록 더 많이 오릅니다.

| GSM8K 정확도(%) | LLaMA-7B | LLaMA2-7B | LLaMA-13B | LLaMA2-13B | LLaMA-33B |
|---|---|---|---|---|---|
| SFT | 35.9 | 41.6 | 43.0 | 50.0 | 54.6 |
| RFT(k=100, 단일 모델 표본) | 41.7 | 47.5 | 49.1 | 54.8 | 54.5 |
| RFT(여러 모델 표본 결합, U13B) | 49.3 | 50.3 | 52.1 | 55.4 | - |

[출처: https://arxiv.org/pdf/2308.01825, Table 1, Table 3]

- 49.3%는 여러 모델의 rejection sample을 합친 결과입니다. 단일 모델 표본만 쓰면 41.7%입니다.
- 가장 강한 33B 모델에서는 RFT(54.5%)가 SFT(54.6%)보다 높지 않습니다. 33B 모델은 질문당 서로 다른 경로가 2.78개로 적습니다. 저자들은 서로 다른 경로를 늘리려면 샘플 수를 지수적으로 늘려야 한다고 씁니다. [출처: https://arxiv.org/pdf/2308.01825, Table 1, 5절]

V-STaR(Hosseini et al., 2024).
- STaR가 버리는 오답도 씁니다. 정답과 오답으로 DPO verifier를 학습하고, 추론 때 여러 후보 중 하나를 verifier로 고릅니다.
- LLaMA2 7B·13B로 수학에서 기존 self-improvement·검증 방법보다 시험 정답률이 6~17%p, 코드 생성에서 4~12%p 높습니다. 초록의 "4~17%"는 두 범위를 합친 값입니다. [출처: https://arxiv.org/pdf/2402.06457, 1절, Figure 2, Figure 8]
- 비교 조건이 다릅니다. verifier를 쓰는 방법은 후보 64개 중 고른 Best-of-64로, 나머지는 Pass@1로 쟀습니다. [출처: https://arxiv.org/pdf/2402.06457, Figure 2 설명]
- generator를 반복 학습하는 것보다 verifier를 반복 학습하는 쪽의 향상이 큽니다. [출처: https://arxiv.org/pdf/2402.06457, Figure 7]

Quiet-STaR(Zelikman et al., 2024).
- 질문-답 대신 일반 글의 token마다 생각을 만들고, 다음 글 예측에 도움이 된 생각을 REINFORCE로 학습합니다.
- Mistral 7B를 OpenWebMath로 계속 사전학습한 뒤, 과제별 파인튜닝 없이 GSM8K 5.9%에서 10.9%, CommonsenseQA 36.3%에서 47.2%로 올랐습니다. [출처: https://arxiv.org/pdf/2403.09629, 5절, Figure 2]
- 시퀀스당 생각을 2개 넘게 늘리면 두 과제 모두 0.1~0.3%p만 더 오릅니다. [출처: https://arxiv.org/pdf/2403.09629, Figure 6]
- 한계: 7B 모델 하나에만 적용했고, 처음부터 학습하는 경우는 확인하지 않았습니다. [출처: https://arxiv.org/pdf/2403.09629, 6절]

SPIN(Chen et al., 2024).
- SFT 모델(zephyr-7b-sft-full)에서 시작해, 이전 반복의 자기 답과 사람이 쓴 SFT 답을 구분하도록 학습합니다.
- 목적 함수의 최적점은 모델 분포가 목표 데이터 분포와 같을 때뿐이라고 증명합니다. 따라서 상한은 사람이 쓴 SFT 데이터의 분포입니다. [출처: https://arxiv.org/pdf/2401.01335, Theorem 5.2]

| Open LLM Leaderboard 6개 과제 평균 | 점수 | 직전 대비 |
|---|---|---|
| zephyr-7b-sft-full | 58.14 | - |
| SPIN 반복 0 | 60.80 | +2.66 |
| SPIN 반복 1 | 62.12 | +1.32 |
| SPIN 반복 2 | 62.97 | +0.85 |
| SPIN 반복 3 | 63.16 | +0.19 |
| 같은 SFT 데이터로 1 epoch 더 SFT | 57.23 | -0.91 |

[출처: https://arxiv.org/pdf/2401.01335, Table 3, Table 5]

- 반복마다 향상이 줄어 반복 3에서는 +0.19입니다. 같은 데이터로 SFT를 더 하면 오히려 낮아집니다.

Self-Rewarding Language Models(Yuan et al., 2024).
- 모델이 LLM-as-a-Judge로 자기 답에 보상을 매기고 반복 DPO를 합니다.
- Llama 2 70B의 AlpacaEval 2.0 win rate(GPT-4 Turbo 대비)는 반복 1에서 9.94%, 반복 2에서 15.38%, 반복 3에서 20.44%입니다. 반복 3은 Claude 2(17.19%), Gemini Pro(16.85%), GPT-4 0613(15.76%)보다 높고, GPT-4 0314(22.07%)보다 낮습니다. [출처: https://arxiv.org/pdf/2401.10020, Table 1]
- MT-Bench에서 수학·코드·추론 점수는 SFT 3.93에서 반복 3의 4.17로 조금만 오릅니다. 저자들은 시드 데이터의 구성을 원인으로 추정합니다. [출처: https://arxiv.org/pdf/2401.10020, Table 2]

### 3.3 에이전트 self-training

| 연구 | 궤적 생성 | 거르는 신호 | 주요 수치(본 위치) |
|---|---|---|---|
| FireAct(2023) | GPT-4가 검색 API로 만든 QA 궤적 | 정답 궤적 | Llama-2-7B에 궤적 500개로 HotpotQA EM 14.8에서 26.2(상대 77% 향상, Table 2). GPT-3.5는 31.4에서 39.2 |
| ReST meets ReAct(2023) | ReAct 에이전트의 이전 궤적 | AI feedback 순위 | 2번 반복 후 Bamboogle 사람 평가: 처음 PaLM 2-L 68.8%, 2세대 PaLM 2-XS 67.2%, 2세대 PaLM 2-L 74.4%(Table 2) |
| SWE-Gym(2024) | 실행 환경이 있는 실제 Python 과제 2,438개(저장소 11개) | 단위 시험 통과 | SWE-Bench 해결률 최대 19%p 향상. verifier로 후보를 고르면 Verified 32.0%(+11.4%p), Lite 26.0%(1절, 5.1절) |
| SWE-smith(2025) | 코드베이스의 시험을 깨는 과제를 자동 합성, 128개 저장소에서 5만 개 | 시험 통과 궤적 | 궤적 5,016개로 학습한 SWE-agent-LM-32B가 SWE-bench Verified Pass@1 40.2%(Figure 1, Table 3) |

[출처: https://arxiv.org/pdf/2310.05915, Table 2] [출처: https://arxiv.org/pdf/2312.10003, Table 2] [출처: https://arxiv.org/pdf/2412.21139, 1절, 5.1절] [출처: https://arxiv.org/pdf/2504.21798, Figure 1, Table 3, 4절]

에이전트 쪽의 공통점은 실행 가능한 환경과 자동 판정(시험 통과, 정답 일치)입니다. 판정이 있으면 궤적을 대량으로 만들고 거를 수 있습니다. 본문과 ablation에서 확인한 주의점은 다음과 같습니다.

- 데이터의 질이 양보다 중요합니다. ReST meets ReAct에서 데이터 크기를 비슷하게 두고 1세대 궤적을 2세대로 바꾸면 9%p 오릅니다. 질문당 궤적을 1개에서 2개로 늘리면 2.2%p 오르지만, 그 이상은 큰 차이가 없습니다. [출처: https://arxiv.org/pdf/2312.10003, Table 3]
- 쉬운 과제의 궤적을 반복해 넣으면 성능이 떨어집니다. SWE-smith는 같은 과제의 궤적을 3개까지만 학습에 넣었습니다. [출처: https://arxiv.org/pdf/2504.21798, 4절, F.3절]
- 평가 기준을 문제 설명에 넣으면 행동이 바뀝니다. SWE-smith에서 이슈 설명 대신 Fail-to-Pass 시험을 주고 학습한 모델은 버그 재현 스크립트를 건너뛰었습니다. SWE-bench Verified 500개 중 재현을 시도한 경우가 379번에서 127번으로 66% 줄었습니다. [출처: https://arxiv.org/pdf/2504.21798, Table 5, 4.1절]
- 파인튜닝은 잡음이 섞인 도구 출력에 대한 강건성도 높입니다. FireAct는 방해되는 도구 출력에서 성능이 64% 높다고 보고합니다. [출처: https://arxiv.org/pdf/2310.05915, 1절, Table 3]

### 3.4 텍스트-SQL의 합성 데이터와 RL

SENSE(2024). 강한 모델(GPT-4)이 만든 데이터로 SFT를 하고, 약한 모델(DeepSeek-Coder-1.3B)이 만든 SQL을 실행 결과로 정답과 오답으로 나눠 DPO를 합니다. [출처: https://arxiv.org/pdf/2408.03256, 3절, 4.4절]

| 모델 | Spider dev EX | Spider dev TS | Spider test | BIRD dev | BIRD test |
|---|---|---|---|---|---|
| DAIL-SQL + GPT-4 | 83.5 | 76.2 | 86.6 | 54.8 | 57.4 |
| CodeLLaMA-13B(기반 모델) | 61.7 | 53.5 | - | 22.9 | - |
| SENSE-7B | 83.2 | 81.7 | 83.5 | 51.8 | 59.3 |
| SENSE-13B | 84.1 | 83.5 | 86.6 | 55.5 | 63.4 |
| SENSE-13B에서 약한 모델 데이터 제외 | 83.9 | 82.9 | - | 52.9 | - |

[출처: https://arxiv.org/pdf/2408.03256, Table 2, Table 5]

- SENSE-13B는 Spider test에서 DAIL-SQL + GPT-4와 같은 86.6이고, BIRD test에서는 63.4로 더 높습니다.
- 향상의 대부분은 강한 모델 데이터에서 나옵니다. 강한 데이터를 빼면 BIRD dev가 22.9로 기반 모델 수준입니다. 약한 모델의 오답 데이터는 BIRD dev를 52.9에서 55.5로 2.6점 더 올립니다. [출처: https://arxiv.org/pdf/2408.03256, Table 5]

OmniSQL(2025). 웹 표에서 합성 DB 16,583개를 만들고, 이 DB로 질문-SQL-CoT 2,544,390개(SynSQL-2.5M)를 합성해 7B·14B·32B 모델을 학습했습니다. [출처: https://arxiv.org/pdf/2503.02240, 4절, Table 1]

| 모델(greedy / majority) | 9개 데이터셋 평균 | EHRSQL | Spider2.0-SQLite |
|---|---|---|---|
| GPT-4o | 58.9 / 59.9 | 44.9 / 45.5 | 14.8 / 15.6 |
| GPT-4-Turbo | 59.4 / 60.0 | 43.1 / 44.8 | 11.9 / 11.9 |
| DeepSeek-V3 | 59.9 / 60.7 | 43.2 / 43.5 | 12.6 / 15.6 |
| Qwen2.5-Coder-7B-Instruct(기반 모델) | 52.8 / 58.4 | 24.3 / 36.9 | 1.5 / 2.2 |
| OmniSQL-7B | 61.2 / 63.1 | 34.9 / 40.0 | 10.4 / 10.4 |
| OmniSQL-32B | 63.2 / 64.8 | 42.4 / 46.8 | 11.9 / 13.3 |

[출처: https://arxiv.org/pdf/2503.02240, Table 4]

- 9개 평균에서는 OmniSQL이 GPT-4o와 DeepSeek-V3보다 높습니다. 그러나 EHRSQL에서는 OmniSQL-7B(34.9)와 32B(42.4)가 greedy 기준으로 GPT-4o(44.9)보다 낮습니다. "닫힌 모델과 비슷하거나 높음"은 평균 기준이고, 의료 DB에는 그대로 적용되지 않습니다.
- OmniSQL은 EHRSQL에서 답 못 하는 질문과 실행 결과가 빈 질문을 빼고 평가했습니다. 즉 이 EHRSQL 점수는 답 못 함 판단을 재지 않습니다. [출처: https://arxiv.org/pdf/2503.02240, 각주 12]
- 7B ablation에서 EHRSQL 점수는 SynSQL-2.5M만으로 학습했을 때 37.2이고, Spider·BIRD CoT 데이터를 더한 최종 OmniSQL-7B는 34.9입니다. 데이터를 더해 평균이 올라도 특정 도메인 점수는 내려갈 수 있습니다. [출처: https://arxiv.org/pdf/2503.02240, Table 5]

SQL-R1(2025). 형식, 실행, 결과, 길이 보상을 합친 NL2SQL 전용 보상으로 GRPO를 합니다. 추론 때는 후보 8개로 self-consistency를 씁니다. [출처: https://arxiv.org/pdf/2504.08600, 3절, 4절]

| 조건 | Spider dev | Spider test | BIRD dev |
|---|---|---|---|
| Qwen2.5-Coder-7B(RL 전) | 77.4 | 79.4 | 58.2 |
| Qwen2.5-Coder-7B에서 바로 RL | 84.5 | 86.1 | 63.1 |
| SynSQL-200K로 SFT cold start 후 RL | 84.7 | 86.4 | 59.2 |
| OmniSQL-7B에서 RL | 87.6 | 88.7 | 66.6 |
| Qwen2.5-Coder-14B에서 바로 RL | 86.7 | 88.1 | 67.1 |

[출처: https://arxiv.org/pdf/2504.08600, Table 1, Table 4, Table 7]

- 초록의 "Spider 88.6%, BIRD 67.1%"는 서로 다른 모델 크기의 값입니다. Table 1 기준으로 Spider test 최고값 88.7은 OmniSQL-7B에서 시작한 7B 모델이고, BIRD dev 최고값 67.1은 14B 모델입니다. 초록의 88.6은 표에 없는 값입니다.
- 7B 최고값은 OmniSQL-7B(SynSQL-2.5M으로 이미 학습한 모델)에서 시작한 결과입니다. 일반 기반 모델에서 바로 RL을 하면 BIRD dev 63.1입니다.
- 합성 데이터 20만 개로 cold start를 하면 BIRD dev가 63.1에서 59.2로 낮아집니다. 저자들은 cold start가 늘 필요하지는 않고 데이터의 출처와 양에 달려 있다고 결론 냅니다. [출처: https://arxiv.org/pdf/2504.08600, Table 4, 4.3절]
- 보상 항목을 하나씩 빼면 BIRD dev가 63.1에서 형식 점수 제외 60.4, 실행 점수 제외 60.7, 길이 점수 제외 61.0, 결과 점수 제외 62.4로 낮아집니다. [출처: https://arxiv.org/pdf/2504.08600, Table 5]
- Spider2.0-SQLite에서 SQL-R1-7B는 20.0%로 GPT-4o(15.6%)보다 높지만 절대값은 낮습니다. [출처: https://arxiv.org/pdf/2504.08600, Table 6]

Reasoning-SQL(2025). GRPO에 부분 보상(실행 정확도, AI feedback, schema linking, n-gram 유사도, 문법 검사)을 씁니다. 스키마는 Gemini-1.5-Pro로 먼저 거릅니다. [출처: https://arxiv.org/pdf/2503.23157, 3절, 4절]

| BIRD dev 실행 정확도(%) | 값 | 표 |
|---|---|---|
| Qwen2.5-Coder-7B(학습 전) | 58.73 | Table 1 |
| 7B SFT | 61.53 | Table 1 |
| 7B STaR-SFT | 62.84 | Table 1 |
| 7B GRPO, 실행 정확도 보상만 | 62.32 | Table 1 |
| 7B GRPO, 모든 보상, 추론 과정 없이 SQL만 | 62.25 | Table 1 |
| 7B GRPO, 모든 보상 | 64.01 | Table 1 |
| 14B GRPO, 모든 보상 | 65.31 | Table 2 |
| o3-mini | 61.34 | Table 2 |
| Gemini-1.5-Pro-002 | 62.25 | Table 2 |
| Gemini-2.0-Flash | 66.49 | Table 2 |
| 14B를 CHASE-SQL pipeline에 넣음(dev / test) | 72.29 / 72.78 | Table 3 |

[출처: https://arxiv.org/pdf/2503.23157, Table 1, Table 2, Table 3]

- 14B 모델은 o3-mini보다 약 4%p, Gemini-1.5-Pro-002보다 약 3%p 높습니다. Gemini-2.0-Flash는 14B 모델보다 1.18%p 높습니다.
- 부분 보상을 모두 쓰면 실행 정확도 보상만 쓸 때보다 1.69%p 높습니다. 정답 SQL을 힌트로 주는 STaR-SFT(62.84)는 SFT보다 높지만 GRPO보다 낮습니다.

### 3.5 2025~2026년 흐름과 위험

- 검증 가능한 보상으로 RL: DeepSeek-R1-Zero는 사람이 쓴 추론 궤적 없이 규칙 기반 보상의 RL만으로 AIME 2024 pass@1이 15.6%에서 77.9%로 올랐습니다. 그러나 가독성이 낮고 한 답 안에서 영어와 중국어를 섞는 문제가 있었고, 추론 밖 과제에서는 성능이 제한되었습니다. 큰 모델의 추론을 Qwen2.5·Llama-3 계열 작은 모델에 증류할 수 있다고도 보고합니다. 텍스트-SQL에서는 실행 결과 일치가 이 보상이 됩니다(SQL-R1, Reasoning-SQL). [출처: https://arxiv.org/pdf/2501.12948, 2절, Figure 1(a), Table 6]
- model collapse: 다른 모델이 만든 데이터로 가리지 않고 학습하면, 세대가 지나며 원래 분포의 꼬리부터 사라지고 행동이 분산이 작은 한 점으로 모입니다. OPT-125m 실험에서 원래 데이터를 남기지 않으면 원래 시험 세트의 perplexity가 20에서 28로 나빠졌습니다. 세대마다 원래 데이터의 10%를 섞으면 성능 저하가 작았습니다. 이 수치는 Nature 게재 전 arXiv 프리프린트에서 확인했습니다. [출처: https://arxiv.org/pdf/2305.17493, 5.1절, Figure 10] [출처: https://www.nature.com/articles/s41586-024-07566-y]
- 의료 질의에서 드문 질문 유형, 드문 코드, 드문 기록 형태가 이 꼬리에 해당합니다. self-training 데이터에는 실제 질문과 실제 DB 실행 결과를 계속 섞어야 합니다.

## 4. Stream of Search(SoS)

### 4.1 무엇을 학습시키나

논문은 Gandhi et al., "Stream of Search (SoS): Learning to Search in Language"(2024)입니다. 언어 모델은 학습 때 쓸모 있는 실수를 거의 보지 못하고, 그래서 오류가 눈덩이처럼 커진다는 문제에서 시작합니다. 저자들은 탐색 과정 전체를 한 줄의 글로 펼쳐 학습시킵니다. [출처: https://arxiv.org/pdf/2404.03683, 1절]

- 과제: Countdown입니다. 입력 숫자들을 사칙연산으로 묶어 목표 숫자를 만듭니다. 24 게임을 넓힌 문제입니다. 목표 숫자의 10%는 분포 밖 평가용으로 남겼습니다. [출처: https://arxiv.org/pdf/2404.03683, 3절]
- 직렬화: 탐색, 되돌아가기(backtracking), 목표 확인을 글로 명시합니다. heuristic 값, 상태 값, 가지치기 전략은 글에 쓰지 않습니다. [출처: https://arxiv.org/pdf/2404.03683, 2절, Figure 2]
- 데이터: BFS와 DFS를 바탕으로, 간단한 heuristic 함수 2개를 쓰는 탐색 전략 12개로 궤적을 만듭니다. 문제는 50만 개입니다. SoS 데이터에서 정답에 이른 궤적은 285,501개(57.1%)이고, 최적 경로(OP) 데이터는 50만 개 모두 정답입니다. [출처: https://arxiv.org/pdf/2404.03683, 4절, Appendix B]
- 모델: GPT-Neo 250M(16층, hidden 1,024), 문맥 4,096 token, 처음부터 사전학습합니다. 두 조건은 같은 gradient step 수만큼 학습합니다. [출처: https://arxiv.org/pdf/2404.03683, 4절, Appendix C.1]

### 4.2 결과

| 조건 | 정확도(본 적 있는 목표) | 정확도(본 적 없는 목표) | 맞은 풀이에서 방문한 상태 수 | 궤적당 산술 오류 |
|---|---|---|---|---|
| 최적 경로만 학습(OP) | 25.73%(보지 못한 입력) | - | - | - |
| 탐색 과정 학습(SoS) | 51.27% | 49.00% | 75.0 | 2.247 |
| SoS + STaR | 55.59% | 53.34% | 66.2 | 1.927 |
| SoS + APA | 56.52% | 54.23% | 64.7 | 0.668 |

OP와 SoS의 비교는 본문 4절과 Figure 3(a), 나머지는 Appendix의 Table 1과 Table 2에서 가져왔습니다. [출처: https://arxiv.org/pdf/2404.03683, 4절, Figure 3(a), Table 1, Table 2]

- 정답 궤적 수가 더 적은 SoS 데이터가 더 좋은 모델을 만듭니다. 실수와 되돌아가기를 보여 준 것이 효과를 냅니다. 다만 SoS 모델의 정확도는 데이터를 만든 탐색 전략들의 평균보다 조금 낮습니다. [출처: https://arxiv.org/pdf/2404.03683, 4절, Figure 3(a)]
- STaR는 반복마다 정답 궤적 10만 개를 만들고, 3번 반복 후 수렴했습니다. 매 반복 기본 SoS 모델에서 다시 학습합니다. APA는 reference policy를 3번 재설정한 뒤 향상이 멈췄습니다. 본문은 향상 폭을 STaR 약 5%, APA 약 6%로 적습니다. [출처: https://arxiv.org/pdf/2404.03683, 5절, Figure 4, Appendix C.4]
- 정책 개선 뒤에는 궤적당 산술 오류가 줄고, 맞은 풀이에서 방문한 상태 수도 줄었습니다. 다만 STaR 모델은 탐색 오류(0.008에서 0.024)와 기타 오류(0.018에서 0.069)가 늘었습니다. [출처: https://arxiv.org/pdf/2404.03683, Figure 6, Table 2]
- 데이터를 만들 때 탐색 전략들이 못 푼 학습 문제 1만 개 중 약 36%를 정책 개선 모델이 풀었습니다. 학습에 쓴 어떤 전략도 풀지 못하는 어려운 문제 1만 개에서는 약 4%를 풀었습니다. [출처: https://arxiv.org/pdf/2404.03683, 5절, Figure 5(b), Figure 5(c)]

### 4.3 관련 연구

- Searchformer(Lehnert et al., 2024)는 A* 탐색의 진행(상태를 탐색 트리에 넣고 빼는 순서)을 token 열로 학습시킨 뒤, 더 짧은 탐색 열을 내도록 파인튜닝합니다. 보지 못한 Sokoban 문제의 93.7%를 최적으로 풉니다. 탐색 단계 감소 폭 26.8%는 초록에서는 "최대", 본문 1절에서는 "평균"으로 적혀 있어 논문 안에서 표현이 다릅니다. [출처: https://arxiv.org/pdf/2402.14083, 초록, 1절]

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

SoS의 결과에 따르면, 탐색과 복구가 담긴 궤적 전체를 학습한 모델이 최종 SQL만 학습한 모델보다 나을 것으로 예상합니다. 다만 SoS 궤적은 4,096 token 안에 들어가고, 에이전트 궤적은 도구 결과 때문에 훨씬 깁니다. 궤적을 학습 데이터로 쓰려면 긴 도구 결과를 줄이는 규칙(5절)이 함께 필요합니다. 또 STaR로 정답 궤적만 다시 학습하면 탐색 오류가 늘 수 있으므로(4.2절), 궤적 단위의 오류 종류도 함께 잽니다.

## 5. 모델이 직접 문맥을 관리하는 방식(NVIDIA, 2026)

### 5.1 무엇을 비교했나

논문 제목은 "Letting Models Manage Their Own Context: Where We Stand"입니다. arXiv 2611.34147이고, 2026년 11월 25일에 제출되었습니다. 저자는 Alessio Devoto 외 NVIDIA 연구진입니다. 실험은 NVIDIA의 공개 에이전트 하네스 NOOA에서 했습니다. [출처: https://arxiv.org/pdf/2611.34147, 1절]

| 방식 | 언제 줄이나 | 무엇을 줄이나 | 원래 기록 |
|---|---|---|---|
| 하네스 주도 | 문맥 사용량이 예산의 80%에 이를 때 | 첫 지시와 최근 사건 10개를 빼고 모두 요약 | 남지 않음 |
| 모델 주도 | 모델이 정함. 85%부터 고려하라는 지시, 사용량 표시, 한계 근처 경고를 줌 | 모델이 고른 사건 범위를 모델이 쓴 요약으로 바꿈(collapse) | 보관함. 모델이 원래 tag로 다시 꺼냄 |

[출처: https://arxiv.org/pdf/2611.34147, 2절, 3절, Figure 1, Listing 2]

시험 과제는 OfficeQA Pro v2(문서 조사 90문항)와 MLE-bench Lite(Kaggle 대회 22개)입니다. 문맥 예산은 8K~512K token입니다. 요청이 예산을 넘으면 가장 오래된 사건을 지우고 다시 시도하며, 3번 실패하면 오답으로 셉니다. 모델은 GPT-6.1 Sol, Kimi K3, DeepSeek V4 Pro, Claude Opus 5.5입니다. 문맥 관리용 추가 학습은 하지 않았습니다. [출처: https://arxiv.org/pdf/2611.34147, 3절]

### 5.2 주요 결과

- OfficeQA Pro v2, 32K 예산에서 GPT-6.1 Sol의 점수는 하네스 주도 21%에서 모델 주도 56%로 올랐습니다. [출처: https://arxiv.org/pdf/2611.34147, 4절, Figure 3]
- 효과는 예산이 작을수록 크고, 예산이 커지면 두 방식이 비슷해집니다. Opus는 예산이 충분히 커질 때까지 하네스 기준보다 낮습니다. MLE-bench Lite에서는 가장 작은 예산에서만 효과가 보입니다. [출처: https://arxiv.org/pdf/2611.34147, 4절, Figure 3, Figure 4]
- 문맥 API를 한 번 이상 쓴 과제 비율은 DeepSeek 53%, Kimi 45%, GPT 42%, Opus 4%입니다. [출처: https://arxiv.org/pdf/2611.34147, Figure 5]
- 한 번 줄일 때 요청 크기는 중앙값 기준 GPT 3.7배, Kimi 2.1배, DeepSeek 1.8배, Opus 1.5배 작아집니다. 보관한 원래 기록을 다시 꺼낸 비율은 compaction 호출 기준으로 GPT 18.6%, Kimi 6.9%, DeepSeek 3.5%, Opus 14.1%입니다. Opus 값은 호출이 적어 잡음이 큽니다. 이 비율은 하한값입니다. [출처: https://arxiv.org/pdf/2611.34147, 5절, Figure 6]
- 64K 예산에서 첫 문맥 경고를 받은 뒤의 행동이 다릅니다. Opus는 88%의 경우 바로 답을 내고 끝냅니다. GPT는 69%의 경우 API 문서를 읽고 줄이고, DeepSeek은 46%의 경우 사건 기록을 먼저 살핀 뒤 줄이고, Kimi는 49%의 경우 바로 줄입니다. [출처: https://arxiv.org/pdf/2611.34147, 5절, Figure 7]
- 85% 시점 지시를 빼면 Kimi와 DeepSeek은 훨씬 일찍 줄입니다. 첫 compaction 시점의 중앙값이 Kimi는 128K에서 약 84%에서 29%로, DeepSeek은 256K에서 83%에서 40%로 당겨졌습니다. Opus는 지시가 없으면 128K에서 16% 시점부터 자주 줄입니다. 128K 이상 예산에서 Kimi와 DeepSeek의 점수는 하네스 기준보다 약 8점 낮아졌습니다. 저자들은 이 현상을 context anxiety라고 부릅니다. [출처: https://arxiv.org/pdf/2611.34147, 6절, Figure 8]
- 32K 예산에서 Kimi K3의 모델 주도 방식은 누적 입력 token이 41% 적었고(3,600만 대 6,200만), 점수는 43% 대 41%였습니다. 64K 예산에서는 누적 입력 token이 약 11% 적고 점수는 57% 대 52%였습니다. GPT는 비슷한 token 절감이 없었습니다. [출처: https://arxiv.org/pdf/2611.34147, 6절, 7절, Figure 9, Figure 10]
- 문맥을 고치면 고친 지점 뒤의 KV cache가 무효가 됩니다. 저자들은 바뀌지 않은 뒷부분의 KV cache를 다시 쓰는 SGLang 시제품을 Qwen3.6-27B, 32K 문맥으로 시험했습니다. 모델 주도 방식에서 요청당 prefill token이 OfficeQA Pro 15.1%, MLE-bench Lite 5.6%, DeepSWE 4.3% 줄었고, 하네스 주도 방식에서도 12.6%, 5.3%, 1.0% 줄었습니다. 과제 점수 변화는 오차 범위 안이었습니다. OfficeQA Pro에서 절감이 큰 이유는 편집 뒤에 남는 뒷부분이 평균 약 1만 token, 프롬프트의 약 60%로 길기 때문입니다. [출처: https://arxiv.org/pdf/2611.34147, 7절, Figure 13]

### 5.3 한계

저자들이 적은 한계는 다음과 같습니다. [출처: https://arxiv.org/pdf/2611.34147, 8절]

- 벤치마크가 작습니다(90문항, 22개 대회). 전략이나 모델 사이의 작은 차이는 유의하지 않을 수 있습니다.
- 문맥 압박은 예산을 줄여 흉내 낸 것입니다. 실제 긴 작업의 성질을 모두 담지 못하고, 한계에서 오래된 사건을 지우는 fallback 자체가 점수에 영향을 줄 수 있습니다.
- 네 모델의 학습 방식은 모릅니다. GPT의 좋은 결과에 대한 설명은 검증하지 않은 추정입니다.
- KV 재사용은 공개 모델 하나와 serving 엔진 하나로만 쟀습니다. 잰 값은 prefill 계산뿐이고, 전체 지연 시간과 비용은 재지 않았습니다.

### 5.4 시사점

- 원래 기록을 지우지 않고 보관하고 tag로 다시 꺼내게 하면, 요약에서 빠진 정보를 모델이 되찾을 수 있습니다. 가장 많이 줄이는 GPT가 가장 자주 다시 꺼냅니다(18.6%). 공격적으로 줄일수록 이 통로가 필요하다는 근거입니다.
- 도구를 준다고 모든 모델이 쓰지는 않습니다. 같은 도구와 지시에서 사용률이 4%에서 53%까지 다릅니다. 도구를 붙인 실험에서는 정답률과 함께 도구 사용률과 다시 꺼낸 비율을 잽니다.
- 언제 줄일지에 대한 지시 한 줄이 결과를 바꿉니다. 지시 문장도 실험 변수로 다룹니다.
- 저자들은 GPT의 좋은 결과에 학습이 기여했을 수 있다고 추정하고, 문맥 관리를 학습으로 가르치는 연구가 필요하다고 씁니다. 3절의 self-training을 문맥 관리 행동에도 적용할 수 있습니다. [출처: https://arxiv.org/pdf/2611.34147, 5절, 10절]

## 6. 받은 의료 LLM 문헌 4편의 수치 확인

| 문헌 | 받은 요약 | 원문 확인 결과 | 판정 | 본 범위 |
|---|---|---|---|---|
| Devoto et al., arXiv 2611.34147 | 모델이 줄일 범위를 고르고, 원래 기록은 보관했다가 다시 꺼냄 | collapse로 범위를 요약하고, 원래 사건은 보관해 tag로 다시 꺼냄(2절, Listing 2). 2026년 11월 25일 제출 | 맞음 | 본문 전체 |
| Bedi et al., JAMA | 519편 중 실제 환자 데이터로 평가한 연구는 5%. 대부분 정확도만 봄 | 519편 중 5%가 실제 환자 진료 데이터를 씀. 95.4%가 accuracy를 주 평가 차원으로 씀(Results) | 맞음 | PMC 본문. supplement 못 봄 |
| Soroush et al., NEJM AI 2024 | GPT-4도 ICD·CPT 코드를 정확히 맞힌 비율이 50% 미만 | GPT-4 exact match: ICD-9-CM 45.9%, ICD-10-CM 33.9%, CPT 49.8%. 시험한 4개 모델 중 가장 높음 | 맞음 | 최종판 초록만 |
| Ferber et al., Nature Cancer 2025 | 도구를 쓰는 에이전트로 정확도가 크게 오름 | 완전성 기준 정답률이 GPT-4 단독 30.3%에서 에이전트 87.2%(95/109)로 오름(Results, Fig. 2b) | 맞음 | 본문, 보충 자료 |

[출처: https://arxiv.org/pdf/2611.34147, 2절] [출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC11480901/, Results] [출처: https://europepmc.org/search?query=10.1056%2FAIdbp2300040, 초록 Results] [출처: https://www.nature.com/articles/s43018-025-00991-6, Results, Fig. 2b]

Bedi et al.(JAMA)의 세부 수치는 다음과 같습니다. 모두 PMC 본문의 Results 절과 Table 1·2에서 확인했습니다. [출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC11480901/, Results, Table 1, Table 2]
- 대상은 2022년 1월 1일부터 2024년 2월 19일까지 나온 연구 519편입니다.
- 의료 과제는 의학 지식 평가(면허 시험 문제 등) 44.5%, 진단 19.5%가 많았습니다. 청구 코드 부여와 처방 작성은 각각 0.2%였습니다.
- NLP 과제는 질의응답이 84.2%였고, 요약 8.9%, 대화 3.3%였습니다.
- 평가 차원은 accuracy 95.4%, fairness·bias·toxicity 15.8%, robustness 14.8%, 배포 고려 4.6%, calibration·uncertainty 1.2%였습니다.
- 전문 분야는 일반 의료 응용 25.6%, 내과 16.4%, 외과 11.4% 순이었습니다.
- 온라인 게재는 2024년 10월 15일이고, 권호는 JAMA 2025;333(4):319-328입니다. 받은 요약의 "JAMA 2024"는 온라인 게재 연도입니다.
- 평가 지표 예시를 담은 supplement(eTable)는 내려받기가 막혀 보지 못했습니다.

Soroush et al.(NEJM AI)의 세부 수치는 다음과 같습니다. 학술지 본문과 PDF는 이 조사 환경에서 접근이 막혀(Cloudflare 확인 페이지) 열지 못했습니다. 아래 수치는 모두 같은 DOI의 Europe PMC 최종판 초록에서 확인했습니다. 저자들의 2023년 medRxiv 프리프린트 본문도 읽었지만, GPT-3.5·GPT-4와 ICD 코드만 다룬 이전 판이고 최종판과 수치가 달라 근거로 쓰지 않았습니다. [출처: https://europepmc.org/search?query=10.1056%2FAIdbp2300040, 초록] [출처: https://www.medrxiv.org/content/10.1101/2023.07.07.23292391v1]
- GPT-3.5, GPT-4, Gemini Pro, Llama2-70b Chat에 코드 설명을 주고 코드를 만들게 했습니다. 한 의료 기관의 EHR에서 12개월 동안 쓰인 코드를 뽑았습니다. ICD-9-CM 7,697개, ICD-10-CM 15,950개, CPT 3,673개입니다.
- 틀린 코드 중 GPT-4는 같은 뜻의 다른 코드를 가장 많이 냈습니다(ICD-9-CM 7.0%, ICD-10-CM 10.9%). GPT-3.5는 더 일반적이지만 맞는 코드를 가장 많이 냈습니다(ICD-9-CM 29.9%, ICD-10-CM 18.5%).
- 저자들은 모든 모델이 부정확하거나 지어낸 정보를 담은 코드를 자주 만들었고, 추가 연구 없이 의료 코딩에 쓰기에 적절하지 않다고 결론 내렸습니다.

Ferber et al.(Nature Cancer)의 세부 수치는 다음과 같습니다. [출처: https://www.nature.com/articles/s43018-025-00991-6, Results, Fig. 2, Fig. 4, Fig. 5]
- GPT-4에 병리 슬라이드용 vision transformer(MSI, KRAS, BRAF 예측), 영상 분할용 MedSAM, OncoKB·PubMed·Google 검색을 도구로 붙였습니다.
- 소화기 종양 중심의 현실적인 다중 모달 환자 사례 20개, 완전성 평가 문장 109개로 평가했습니다. 의료 전문가 4명이 눈가림 평가를 했고, 의견이 갈리면 다수결과 가장 불리한 판정을 택했습니다.
- 필요한 도구 호출 64번 중 56번을 맞게 써서 도구 사용 정확도가 87.5%입니다. 필요했지만 쓰지 않은 도구가 8번(12.5%), 필요 없는 도구 호출이 2번이었습니다(Fig. 4).
- 91.0%는 평가 가능한 문장 245개 중 223개가 사실로 맞았다는 뜻입니다. 사례 단위 비율이 아닙니다. 16개(6.5%)는 틀렸고, 6개(2.4%)는 해로울 수 있다고 판정되었습니다.
- 인용 257개 중 194개(75.5%)가 주장과 맞았고, 59개(23.0%)는 관련이 없었으며, 4개(1.6%)는 주장과 충돌했습니다.
- 같은 도구 호출을 Llama-3 70B와 Mixtral 8x7B로도 시험했지만, 두 공개 모델은 도구 호출 성능이 매우 낮아 이후 분석에서 뺐습니다(Fig. 5). 사례별 결과는 보충 자료 Supplementary Table 2·3에 있습니다.

## 7. 텍스트-SQL·EHR 질의 에이전트에 주는 시사점

### 7.1 도구 결과가 잘리는 문제

EHR 질의 에이전트는 긴 결과를 자주 받습니다. 행이 많은 검사 결과, 긴 서술형 기록이 그 예입니다. 하네스가 결과를 일정 행이나 글자 수로 자르면, 모델은 뒷부분에 있던 기록을 못 보고 "기록 없음"이라고 답할 수 있습니다. 5절의 연구는 하네스가 대신 줄이면 필요한 정보가 빠질 수 있다는 같은 문제를 다룹니다.

권하는 설계는 다음과 같습니다.
1. 잘린 결과에는 잘렸다는 표시, 전체 행 수, 전체 길이를 함께 보여 줍니다.
2. 원래 결과는 지우지 않고 보관합니다. 결과마다 id를 붙이고, 모델이 id와 범위(행 번호, 글자 위치)로 잘린 부분을 다시 꺼내는 도구를 줍니다. NVIDIA 연구의 보관과 tag 조회와 같은 구조입니다.
3. SQL 에이전트에서는 다시 꺼내기 대신 같은 질의에 LIMIT, OFFSET, WHERE 조건을 붙여 다시 실행하게 할 수도 있습니다.
4. 잘린 결과만 보고 "없음"이라는 부정 결론을 내지 말라는 규칙을 시스템 지시에 넣습니다.
5. 도구 사용률을 잽니다. NVIDIA 연구에서 같은 도구를 Opus 5.5는 4%만 썼고, 경고를 받으면 88%의 경우 바로 답을 냈습니다. 모델이 도구를 잘 쓰지 않으면, 잘림 표시를 더 눈에 띄게 하거나 부정 결론 전에 하네스가 확인을 요구합니다.
6. 평가 지표에 잘린 결과 뒤의 부정 답 비율과 다시 꺼낸 비율을 넣습니다.

### 7.2 답 못 함 판단과 "기록 없음"

- EHRSQL 2024의 RS처럼 틀린 답에 벌점을 주는 지표로 평가하면, 답 못 함 판단의 가치가 점수에 드러납니다. 모두 답하지 않는 기준선(20점)도 함께 보고합니다(2.1절).
- 상위 팀은 모두 불확실성 신호(token entropy, log-probability, 여러 샘플이나 여러 모델의 합의)로 답을 걸렀습니다. token 확률을 주지 않는 API 모델에서는 여러 번 샘플링한 SQL 결과의 합의가 쓸 수 있는 신호입니다(2.4절).
- "DB로 답할 수 없는 질문"과 "답할 수 있고 정답이 빈 결과인 질문"을 구분합니다. PLUQ의 실행 필터는 빈 결과를 답 못 함으로 바꾸고, OmniSQL은 이런 질문을 평가에서 뺐습니다. 실제 EHR에서 "해당 환자에게 그 검사 기록이 없음"은 맞는 답일 수 있습니다. 평가 세트에도 두 종류를 따로 넣습니다.

### 7.3 코드와 용어는 사전과 뷰에서 찾게 하기

GPT-4도 코드 설명에서 ICD-9-CM, ICD-10-CM, CPT 코드를 정확히 만든 비율이 50% 미만입니다(6절). 에이전트가 코드를 기억으로 만들지 않고, 코드 사전 테이블이나 뷰를 조회해 찾게 합니다. 사전 조회 결과가 없으면 코드를 지어내지 말고 그 사실을 답에 적게 합니다.

### 7.4 평가 설계

- 실제 환자 데이터(또는 실제 EHR 구조의 DB)로 평가합니다. Bedi et al.이 본 519편 중 5%만 실제 진료 데이터를 썼습니다.
- 정답률 밖의 차원을 잽니다. calibration·uncertainty를 잰 연구는 1.2%뿐입니다. 답 못 함 판단, 확신도와 정답의 관계, 도구 사용 정확도를 함께 잽니다.
- Ferber et al.처럼 도구 호출의 정확도(필요한 도구를 맞게 불렀는지, 빠뜨린 도구와 필요 없는 호출)와 최종 결론의 정확도, 해로울 수 있는 답의 비율을 따로 잽니다.
- 평균 점수만 보지 않습니다. OmniSQL은 9개 데이터셋 평균에서 GPT-4o보다 높지만 EHRSQL에서는 낮습니다(3.4절). 의료 DB 점수는 따로 보고합니다.

### 7.5 self-training을 적용한다면

1. 학습 질문: 평가 문항으로 학습하지 않습니다. 평가와 분리한 합성 질문을 템플릿이나 강한 모델로 만듭니다(KU-DMIS, OmniSQL). 실제 운영 질문을 쓸 때는 평가 세트와 겹치지 않게 분리합니다. PLUQ처럼 시험 입력에 의사 라벨을 붙이는 방식은 고정 벤치마크에서만 쓸 수 있다는 주최 측 평가가 있습니다(2.5절).
2. 궤적 생성: 에이전트가 각 질문을 여러 번 풉니다. 스키마 탐색, SQL 오류, 수정이 담긴 궤적 전체를 남깁니다(SoS).
3. 거르기: 최종 SQL의 실행 결과가 정답 SQL의 실행 결과와 같은 궤적만 남깁니다(STaR, RFT, ReST-EM). 답 못 하는 질문은 null 라벨로 따로 늘려 class 불균형을 줄입니다(PLUQ). 쉬운 질문의 궤적이 몰리지 않게 질문당 궤적 수에 상한을 둡니다(SWE-smith).
4. 오답 궤적: 버리지 않고 verifier나 선호 학습에 씁니다(V-STaR, SENSE). 다만 SENSE에서 오답 데이터의 몫은 BIRD dev 2.6점으로, 강한 정답 데이터의 몫보다 훨씬 작습니다.
5. 학습: LoRA나 QLoRA 같은 parameter-efficient 파인튜닝으로 합니다. 반복은 2~3회로 두고, 매 반복 처음 모델에서 다시 학습합니다(STaR, ReST-EM Figure 7). SPIN에서 반복 3의 향상은 +0.19뿐이었습니다. 생성 데이터만 되풀이하지 않고 실제 질문과 실제 실행 결과를 섞습니다(model collapse).
6. 문맥 관리 행동: 긴 결과를 줄이고 다시 꺼낸 궤적 중 정답에 이른 것을 학습 데이터에 넣으면, 5절에서 저자들이 말한 문맥 관리 학습이 됩니다.

LoRA와 QLoRA의 원 논문은 다음과 같습니다. 이 두 논문의 수치는 이 보고서에 쓰지 않았습니다. [출처: https://arxiv.org/abs/2106.09685] [출처: https://arxiv.org/abs/2305.14314]

## 8. 확인 못 한 것

- PLUQ의 K 값과 self-training 단계만의 효과는 arXiv판과 ACL Anthology판 본문 전체에 없습니다. 두 판 모두 appendix가 없어 더 찾을 곳이 없습니다. 저자 코드나 추가 자료는 확인하지 않았습니다.
- Soroush et al.(NEJM AI)의 학술지 본문과 PDF는 접근이 막혀 열지 못했습니다. 이 논문의 수치는 최종판 초록만 근거입니다.
- Bedi et al.(JAMA)의 supplement(eTable)는 내려받기가 막혀 보지 못했습니다. 본문 수치는 PMC 본문으로 확인했습니다.
- model collapse 논문은 Nature 게재판 본문 대신 arXiv 프리프린트 본문으로 확인했습니다. 게재판에서 수치나 실험이 바뀌었는지는 대조하지 않았습니다.
- ReST-EM과 V-STaR의 주요 결과는 그림으로만 나와, 정확한 수치 대신 그림 번호와 본문 서술을 적었습니다.
