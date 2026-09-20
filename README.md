## 안녕하세요, Mason입니다

BI 운영 경험을 바탕으로, 수집부터 검증·제공까지 연결하는 데이터 엔지니어가 되고 싶습니다.

재실행해도 중복이 쌓이지 않고, 잘못된 데이터가 사용자에게 닿기 전에 멈추는 파이프라인을 구축하고 있습니다.

## 지금 집중하는 것

- **복구 가능한 수집**: Cloudflare R2에 원본과 수집 이력을 보존해 재처리 기준점 확보. Airflow로 작업 의존성·재시도·과거 구간 재처리 관리.
- **중복 없는 재실행**: 8만 행 이상 적재 시 SQL 크기 제한에 대응해 Iceberg의 삭제·추가를 단일 트랜잭션으로 구성. 같은 실행 구간을 안전하게 교체.
- **자원 한계에 맞춘 처리**: Trino 메모리 한계에 맞춰 전체 이력 중복 제거를 변경 키 중심의 증분 MERGE로 전환. 다시 읽고 계산할 범위 축소.
- **검증 후 제공**: dbt/Trino에서 키·행 수·최신성을 검증한 결과만 D1/Workers로 게시. 이력 분석과 사용자 조회 경로를 분리해 불필요한 전체 이력 조회 방지.

## 핵심 기술

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white)
![Trino](https://img.shields.io/badge/Trino-DD00A1?style=flat-square&logo=trino&logoColor=white)
![Apache Iceberg](https://img.shields.io/badge/Apache%20Iceberg-261D2F?style=flat-square&logo=apache&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![Amazon Kinesis](https://img.shields.io/badge/Amazon%20Kinesis-FF9900?style=flat-square&logo=amazonwebservices&logoColor=white)
![Cloudflare R2](https://img.shields.io/badge/Cloudflare%20R2-F38020?style=flat-square&logo=cloudflare&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-4B32C3?style=flat-square&logoColor=white)
![MicroStrategy](https://img.shields.io/badge/MicroStrategy-EC1C24?style=flat-square&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

## GitHub 활동

<p align="center">
  <img height="165" src="https://github-stats-extended.vercel.app/api?username=masondev1024&show_icons=true&theme=transparent&hide_rank=true&include_all_commits=true&disable_animations=true&locale=en" alt="GitHub 활동 통계" />
</p>

<p align="center">
  <a href="https://github.com/masondev1024">
    <img height="165" src="./assets/github-streak.svg" alt="masondev1024의 GitHub 연속 기여 기록" />
  </a>
</p>

## 연락처

[블로그](https://velog.io/@mason_dev) · [이메일](mailto:masondev1024@gmail.com)
