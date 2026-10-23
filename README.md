# Pleos SDK 제공 정보 범위 조사

현대자동차그룹 차량용 앱 개발 공모전(2026)을 준비하며, Pleos Connect SDK가 제공하는 데이터 범위와 관련 영역의 현실 문제를 공개 자료로 정리한 보고서입니다. 조사 기준일은 2026년 10월 23일입니다.

- 웹 페이지: https://leetae9yu.github.io/pleos-sdk-research/
- 보고서 원문: [report.md](report.md)

## 구성

- report.md: 보고서 원문(Markdown)
- site/: report.md를 정적 웹 페이지로 만드는 생성기(build.py, 템플릿, 스타일)
- docs/: GitHub Pages로 배포되는 생성 결과

## 다시 만들기

```
python3 site/build.py
```

Python 3과 markdown, beautifulsoup4 패키지가 필요합니다. 생성 결과는 site/dist/에 만들어지며, 배포용으로 docs/에 복사합니다.

## 출처와 이용

보고서의 모든 주장 옆에 출처 URL이 있습니다. Pleos 문서의 내용은 요약과 API 이름 인용 수준으로만 담았으며, 원문은 각 링크에서 확인할 수 있습니다. 확인하지 못한 항목은 "확인 못 함"으로 표시했습니다.
