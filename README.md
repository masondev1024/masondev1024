## Hi, I'm Mason

Data Engineer designing reliable pipelines from public APIs to validated data products.

I started in enterprise BI and moved upstream to make data systems replayable, testable, and easy to operate.

## Current Focus

- Designing ASK Seoul's path as Airflow -> R2/Parquet -> Iceberg -> dbt/Trino -> D1/Workers, with one clear responsibility per layer
- Using Airflow for dependency scheduling, retries, quality gates, and backfills; using dbt/Trino so transformations and checks stay queryable
- Keeping raw inputs replayable in R2/Parquet; using Iceberg for transactional delete-and-append and incremental MERGE; publishing only verified products through D1/Workers
- Using failure data to narrow the design: 80k+ row loads caused 20 scheduled failures, while full-history dedup hit Trino's 3.71 GB per-node limit

## Core Stack

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

## GitHub Activity

<p align="center">
  <img height="165" src="https://github-stats-extended.vercel.app/api?username=masondev1024&show_icons=true&theme=transparent&hide_rank=true&include_all_commits=true&disable_animations=true&locale=en" alt="GitHub Stats" />
</p>

<p align="center">
  <a href="https://github.com/masondev1024">
    <img height="165" src="./assets/github-streak.svg" alt="GitHub contribution streak for masondev1024" />
  </a>
</p>

## Contact

[Velog](https://velog.io/@mason_dev) · [Email](mailto:masondev1024@gmail.com)
