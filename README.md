# 정성헌

금융·유통 고객사의 BI 리포트와 데이터 모델을 개발·운영하며 2년 5개월 동안 SQL과 로그로 수치 불일치와 적재 오류를 추적했습니다. 지금은 수집·게시 과정과 장애 후 재실행·복구를 설계하고 검증합니다.

[포트폴리오](https://jungseongheon.org/) · [이력서 PDF](https://jungseongheon.org/documents/jung-seongheon-resume-ai-infra-review-20261025.pdf) · [기술 블로그](https://velog.io/@mason_dev/posts) · [이메일](mailto:masondev1024@gmail.com)

## 대표 프로젝트

1. **[ASK Seoul · 기상 데이터 파이프라인](https://github.com/masondev1024/seoul-weather-platform)**  
   팀에서 기상·교통 수집과 게시 전 검사를 맡았습니다. 예보 적재를 PyIceberg 단일 커밋으로 바꾼 뒤 확인한 실행에서 같은 Trino 오류가 재발하지 않았습니다. 별도 교통 작업은 변환 주기를 하루 288회에서 24회로 줄였습니다. 개인 저장소에서는 기상 품질 평가와 장소별 조회를 보강했습니다. [프로젝트 기록](https://jungseongheon.org/portfolio/#ask-seoul)
2. **[Agentic Marketing Data Pipeline](https://github.com/masondev1024/agentic-marketing-data-pipeline)**  
   개인 프로젝트로 분석 마트, 조회 API, 모델 호출 상태·예산 기록을 구현했습니다. AWS 단기 시험에서 같은 RDS 인스턴스의 별도 DB로 복원한 테이블·뷰 14개의 행 수와 내용 해시가 일치했습니다. [검증 기록](https://jungseongheon.org/portfolio/evidence/index.html#marketing)
3. **[GitOps 배포·복구](https://github.com/masondev1024/aws-data-platform-gitops)**  
   팀 프로젝트 이후 HPA가 정한 복제 수를 보존하고 승격에 필요한 CPU 할당량을 검사하는 회귀 테스트를 추가했습니다. AWS 카나리 13분 시험에서 HTTP 15,600건을 처리했고, 최종 승격 단계는 할당량 조정과 수동 조치 후 복구했습니다. [검증 기록](https://jungseongheon.org/portfolio/evidence/index.html#gitops)
4. **[청년 법률 상담 AI](https://github.com/masondev1024/youth_law_team_project)**  
   팀에서 금융 분야 검색·Agent와 질문 분류 흐름을 맡았습니다. 개인 후속 AWS 합성 자료 복구에서 보존 대상 6건의 해시 일치와 철회 기록 제외를 확인했습니다. [검증 기록](https://jungseongheon.org/portfolio/evidence/index.html#youth-recovery)

## 사용한 기술

- 수집·변환·게시 · Python, SQL, Airflow, dbt, Trino, Iceberg, Cloudflare R2·D1
- 배포·복구 · AWS, Kubernetes, Argo CD, Terraform, GitHub Actions
- 조회·모델 호출 · PostgreSQL, LangGraph, RAG

[이어짐의 삭제 이력과 복구 검증](https://github.com/masondev1024/ieojim/blob/main/docs/engineering/deletion-safe-restore.md) · [추가 프로젝트](https://jungseongheon.org/portfolio/#other-projects)
