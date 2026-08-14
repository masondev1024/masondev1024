# 정성헌 | Data Engineer

> 실패해도 다시 실행할 수 있게, 다시 실행해도 중복되지 않게.

3년 3개월간 BI 엔지니어로 데이터 모델과 리포팅 시스템을 설계·운영했습니다. 현재는 Airflow, dbt, Trino/Iceberg 기반으로 재실행 가능한 데이터 파이프라인과 서빙 검증 흐름을 구축하고 있습니다.

## Current Focus

### ASK Seoul — 서울 도시데이터 통합 시계열 레이크하우스

**팀 프로젝트 · Weather/Traffic 파이프라인 담당 및 공통 플랫폼 기여**

Weather/Traffic 담당 범위에서 서울시 공공데이터를 KST 시간축과 행정동 공간축으로 표준화하고, D1/API 게시 검증까지 이어지는 공통 경로 개선에 기여했습니다.

`Airflow → Cloudflare R2 → Trino/Iceberg → dbt Silver/Gold → D1/API → External AI Agent`

- **공공 날씨 예보 8만+ 행/run** Bronze 적재를 PyIceberg `delete(dag_run_id) + append` 단일 트랜잭션으로 전환해, 재실행 시 중복·부분 적재가 남지 않는 경계를 만들었습니다.
- 대형 SQL 크기 제한으로 발생한 **자동 적재 실패 20건의 근본 원인을 제거**하고, 이후 **동일 오류 재발 0건·1 commit/run**을 운영 로그로 확인했습니다.
- 전이력 window dedup의 메모리 초과를 incremental MERGE로 전환해, 밀린 **458,720행을 dev에서 26.5초**에 회복했습니다.
- 프로젝트 산출물을 일회성 데모로 끝내지 않고 Weather 정기 수집을 운영하고 있으며, **2026-08-14 기준 scheduled run의 연속 성공**을 확인했습니다.

[Team Project](https://github.com/ASAC-DE-bigkk/ASK-Seoul) · [Airflow Pipelines](https://github.com/ASAC-DE-bigkk/ASAC-DAG) · [dbt Models](https://github.com/ASAC-DE-bigkk/ASAC-DBT) · [Serving & Dashboard](https://github.com/ASAC-DE-bigkk/ASK-Seoul-Serving)

## Open Source

ASK Seoul의 Weather 데이터 상품을 외부 AI Agent가 조회할 수 있도록 [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill)에 데이터·API 계약과 검증 경로를 기여했습니다.

## Selected Work

### [Robot Data Platform + PRISM](https://github.com/masondev1024/robot-data-pipeline)

**교육·시뮬레이션 프로젝트 / MVP 해커톤 본선 진출 프로토타입**

- Kinesis → Firehose → S3 Parquet 스트리밍과 Bronze/Silver/Gold 배치 흐름을 구성했습니다.
- EKS·Karpenter·HPA, Terraform, GitHub Actions OIDC로 확장성과 배포 안전 장치를 설계했습니다.
- SageMaker 예측 결과를 DoWhy 인과 추론과 LLM Multi-Agent 의사결정으로 연결하고, 로컬에서는 deterministic replay로 재현 가능하게 만들었습니다.

### [E-commerce Review Data Pipeline](https://github.com/masondev1024/ecommerce-ai-batch-analyzer)

Kafka 수집, Airflow 배치, FastAPI 분석, Redis·MySQL·MinIO 저장소와 Prometheus·Grafana 관측 환경을 Docker Compose로 재현한 학습 프로젝트입니다.

## Background

**BI Engineer · 3년 3개월**

데이터 모델·리포팅 시스템과 대시보드를 운영하며 SQL 성능 개선, 인증·연동 장애 추적, 중단된 메타데이터 적재 흐름 복구를 경험했습니다.

## Stack

**Data** · Python, SQL, Apache Airflow, dbt, Trino, Apache Iceberg, PyIceberg, Kafka, Flink

**Cloud & Platform** · AWS, Cloudflare R2/D1/Workers, Docker, Kubernetes/EKS, Terraform, GitHub Actions

**Serving & Observability** · FastAPI, Grafana, CloudWatch, Prometheus, OpenLineage

**AI/ML** · Amazon Bedrock, SageMaker, DoWhy, RAG, LLM Agent

## Contact

[Velog](https://velog.io/@mason_dev) · [Email](mailto:masondev1024@gmail.com)
