# 정성헌

수집한 데이터를 검증해 제공하고, 실패한 작업의 재실행과 복구를 다룹니다.
금융·유통 BI 개발·운영 2년 5개월 동안 SQL과 로그로 수치 불일치와 적재 오류를 확인한 경험이 있습니다.

[포트폴리오](https://jungseongheon.org/) · [프로젝트 상세](https://jungseongheon.org/portfolio/) · [이력서 PDF](https://jungseongheon.org/documents/jung-seongheon-resume-ai-infra-review-20261025.pdf) · [기술 블로그](https://velog.io/@mason_dev/posts)

## 대표 프로젝트

### 01. [ASK Seoul](https://github.com/masondev1024/seoul-weather-platform)

기관마다 다른 시간·지역 기준을 맞춰 서울의 기상·교통 데이터를 조회할 수 있게 구성.

- **내 역할** · 팀의 기상·교통 수집과 게시 전 검사. 이후 기상 코드를 개인 저장소로 이관해 품질 평가·장소별 조회 보강.
- **구조·결과** · Airflow → R2·Iceberg → dbt·Trino → D1·Workers. 팀 교통 변환 작업 **하루 288회 → 24회**, 기상 위험 제품 **k-skill PR #552 병합**.

[설계·기여·검증 기록](https://jungseongheon.org/portfolio/#ask-seoul)

### 02. [Agentic Marketing Data Pipeline](https://github.com/masondev1024/agentic-marketing-data-pipeline)

리드·계약·주문의 연결 누락을 구분하고, 확인된 지표만 AI 답변에 사용.

- **내 역할** · 개인 프로젝트의 분석 마트·품질 검사·조사 API, 모델 호출 상태와 예산 관리 구현.
- **구조·결과** · PostgreSQL → 검증된 게시 버전 → LangGraph 조회. AWS 워커 종료 후 같은 요청의 **호출 예약 수 4회 유지**, 같은 RDS의 별도 DB 복원에서 **테이블·뷰 14개 행 수·해시 일치**.

[설계·기여·검증 기록](https://jungseongheon.org/portfolio/#agentic-marketing)

### 03. [GitOps 배포·복구](https://github.com/masondev1024/aws-data-platform-gitops)

새 버전 배포 중 응모 접수와 후속 이벤트가 어긋나는지 함께 확인.

- **내 역할** · 래플 팀 프로젝트 이후 HPA 복제 수 보존, 구·신 버전 동시 실행에 필요한 CPU 검사와 회귀 테스트 추가.
- **구조·결과** · Terraform·EKS → Argo Rollouts → HTTP·DB 정합성 검사. AWS 13분 카나리에서 **HTTP 15,600건 성공**, **응모 API p95 113.5ms**. 최종 승격은 할당량 조정과 수동 재동기화 후 복구.

[설계·기여·검증 기록](https://jungseongheon.org/portfolio/#gitops)

### 04. [청년 법률 상담 AI](https://github.com/masondev1024/youth_law_team_project)

금융 첫 상담에 필요한 자료를 정리하고, 백업 복원 뒤 철회한 기록이 다시 노출되지 않도록 처리.

- **내 역할** · 팀의 금융 법령 검색·Agent와 질문 분류. 개인 후속으로 상담 카드·인증·철회·복구 기능 추가.
- **구조·결과** · 법령 검색·상담 준비 / EC2·SQLite + DynamoDB 삭제 이력·S3 백업. AWS 합성 자료 복구 1회 **234.52초**, **보존 대상 6건 해시 일치·철회 기록 제외**.

[설계·기여·검증 기록](https://jungseongheon.org/portfolio/#youth-law)

---

[이어짐 · 삭제한 기록을 되살리지 않는 백업 복구](https://github.com/masondev1024/ieojim/blob/main/docs/engineering/deletion-safe-restore.md) · [추가 프로젝트](https://jungseongheon.org/portfolio/#other-projects) · [이메일](mailto:masondev1024@gmail.com)
