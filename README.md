## About Me

3년 3개월 동안 BI 엔지니어로 일하며 데이터 모델과 리포팅 시스템을 설계하고 운영했습니다. 데이터를 만드는 것만큼 필요한 사람에게 안정적으로 전달하는 일이 중요하다는 것을 배웠습니다.

현재는 그 경험을 바탕으로 AWS 환경의 데이터 파이프라인과 클라우드 인프라를 설계하고 자동화하는 데이터 엔지니어로 영역을 확장하고 있습니다.

새로운 문제를 만나면 원인을 차분하게 끝까지 파고들고, 해결 과정에서 배운 내용을 기록하며 더 나은 구조로 개선하려고 합니다. 동료와 지식을 나누고 함께 성장하는 과정을 중요하게 생각합니다.

## Experience

### BI Engineer | 3년 3개월

현업 사용자가 필요한 데이터를 안정적으로 활용할 수 있도록 데이터 모델과 대시보드를 설계하고 운영했습니다.

- 비즈니스 요구사항을 SQL과 BI 스키마 객체로 구현했습니다.
- 데이터 모델과 쿼리 구조를 개선하여 리포팅 성능을 최적화했습니다.
- 시스템 Trace를 분석하여 인증 및 연동 장애의 원인을 진단했습니다.
- 장기간 중단된 메타데이터 적재 흐름을 재설계하고 데이터를 복구했습니다.

이 경험을 통해 좋은 데이터 시스템은 데이터를 적재하는 데서 끝나지 않고, 사용자가 신뢰하며 지속적으로 활용할 수 있어야 한다는 점을 배웠습니다.

## Current Projects

### [Robot Data Platform + PRISM](https://github.com/masondev1024/robot-data-pipeline)

1,000대의 로봇에서 발생하는 텔레메트리를 가정하여 데이터 수집부터 실시간 처리, 배치 분석, 예측과 모니터링까지 연결한 데이터 플랫폼 프로젝트입니다.

- Kinesis와 Firehose를 이용해 스트리밍 데이터를 수집하고 S3 Parquet에 적재했습니다.
- Bronze, Silver, Gold 계층으로 데이터를 분리하고 Airflow 기반 배치 처리 흐름을 구성했습니다.
- EKS, HPA, Karpenter로 확장성을 설계하고 Terraform과 GitHub Actions로 인프라와 배포를 자동화했습니다.
- CloudWatch와 Grafana로 데이터 흐름과 플랫폼 상태를 관측할 수 있도록 구성했습니다.
- 운영 중 발견한 장애를 Runbook과 자동화 조건으로 환원했습니다.

기술을 연결하는 데서 끝내지 않고 장애 복구, 데이터 계약, 배포 안전성, 검증 범위와 비용까지 함께 고민하고 있습니다.

[Repository](https://github.com/masondev1024/robot-data-pipeline) · [Project Notes](https://velog.io/@mason_dev)

### [E-commerce Review Data Pipeline](https://github.com/masondev1024/ecommerce-ai-batch-analyzer)

리뷰 데이터를 Kafka로 수집하고 Airflow로 처리한 뒤, 분석 결과를 저장하고 모니터링하는 환경을 구성한 학습 프로젝트입니다.

- FastAPI 기반 분석 서비스를 데이터 처리 흐름과 분리했습니다.
- Redis, MySQL, MinIO를 역할에 따라 분리하여 구성했습니다.
- Prometheus와 Grafana로 서비스 상태를 확인할 수 있도록 구성했습니다.
- Docker Compose로 로컬에서도 전체 흐름을 재현할 수 있도록 했습니다.

서비스별 책임을 나누고, 실패한 구성 요소를 독립적으로 확인할 수 있는 구조를 만드는 데 집중했습니다.

[Repository](https://github.com/masondev1024/ecommerce-ai-batch-analyzer)

## Tech Stack

### Data & Orchestration

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![Apache Flink](https://img.shields.io/badge/Apache%20Flink-E6526F?style=flat-square&logo=apacheflink&logoColor=white)

### Cloud & Platform

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white)

### Automation & Observability

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=flat-square&logo=amazoncloudwatch&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)

### BI & Analytics

![MicroStrategy](https://img.shields.io/badge/MicroStrategy-D9232E?style=flat-square&logoColor=white)
![Data Modeling](https://img.shields.io/badge/Data%20Modeling-0F6CBD?style=flat-square&logoColor=white)
![Dashboard Design](https://img.shields.io/badge/Dashboard%20Design-6F42C1?style=flat-square&logoColor=white)

## Currently Exploring

- 장애 상황에서도 안전하게 복구할 수 있는 데이터 파이프라인
- 스트리밍과 배치 처리를 함께 운영하는 방법
- 데이터 품질과 흐름을 관측할 수 있는 플랫폼
- 반복 작업을 줄이는 인프라 및 배포 자동화
- 성능과 안정성을 유지하면서 클라우드 비용을 최적화하는 방법

## Blog & Contact

프로젝트를 만들며 겪은 문제와 해결 과정을 꾸준히 기록하고 있습니다.

[![Velog](https://img.shields.io/badge/Velog-20C997?style=flat-square&logo=velog&logoColor=white)](https://velog.io/@mason_dev)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:masondev1024@gmail.com)

## GitHub Activity

<p>
  <img height="165" src="https://github-stats-extended.vercel.app/api?username=masondev1024&show_icons=true&theme=transparent&hide_rank=true&include_all_commits=true&disable_animations=true&locale=kr" alt="GitHub Stats" />
  <img height="165" src="https://streak-stats.demolab.com?user=masondev1024&theme=transparent&hide_border=true&locale=ko&disable_animations=true" alt="GitHub Streak" />
</p>
