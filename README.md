# 정성헌 

BI 시스템을 2년 5개월 운영했습니다. 이후 공공데이터와 이벤트 데이터를 대상으로 수집·변환·게시 흐름을 개발하고, 누락·중복과 장애가 생겼을 때 복구하는 과정을 검증했습니다.

[포트폴리오](https://jungseongheon.org/portfolio/) · [기술 블로그](https://velog.io/@mason_dev/posts) · [이메일](mailto:masondev1024@gmail.com)

## 주요 프로젝트

### 1. ASK Seoul · 공공데이터 수집과 품질 검증

팀 프로젝트에서 기상·교통 수집, Iceberg 적재, dbt 변환과 게시 전 검증을 맡았습니다. 대량 입력의 SQL 크기 제한, 게시 요청 충돌, 수집 누락을 다루고 재실행 조건을 정리했습니다. 이후 개인 Seoul Weather Platform에서 실행 슬롯 분리와 예보 품질 분석을 이어갔습니다.

- Python · SQL · Airflow · Iceberg · dbt · Trino · Cloudflare R2
- [개인 후속 개발](https://github.com/masondev1024/seoul-weather-platform)
- [조직 기여: 게시 충돌·재시도](https://github.com/ASAC-DE-bigkk/ASAC-DAG/pull/786)
- [조직 기여: 수집 원본·재실행 검사](https://github.com/ASAC-DE-bigkk/ASAC-DAG/pull/787)

### 2. D2C · 승인 기록과 이벤트의 일관성

승인과 Outbox를 PostgreSQL의 같은 트랜잭션에 저장하고, Kafka로 재전송된 이벤트를 소비자가 event_id로 중복 제거하도록 구현했습니다. 로컬 Docker에서 DB·Kafka·발행기를 중단한 뒤 복구를 확인했으며, 최종 승인·Outbox·고유 적재 각 9건을 대조했습니다.

- Python · PostgreSQL · Kafka · DuckDB · Docker · Prometheus
- [코드](https://github.com/masondev1024/d2c-event-data-platform) · [장애·복구 기록](https://github.com/masondev1024/d2c-event-data-platform/blob/main/RUNBOOK.md)
- 단일 브로커 로컬 검증입니다. D2C의 실제 클러스터 자동 롤백과 대규모 처리 성능은 별도 검증 대상입니다.

### 3. 로봇 데이터 플랫폼 · AWS 스트리밍과 배치 이관

Kinesis·Firehose·S3 Parquet·Glue·Athena로 수집과 조회를 연결했습니다. 별도 Glue→사설 RDS 이관에서는 정상 4건의 재실행 후 중복 없음과, 잘못된 배치의 부분 반영 차단을 확인했습니다.

- Terraform · EKS · Kinesis · Firehose · Glue Spark · RDS · Athena
- [코드와 실행 방법](https://github.com/masondev1024/robot-data-pipeline) · [이관 검증](https://github.com/masondev1024/robot-data-pipeline/blob/main/docs/public/S3-GLUE-RDS-LAB.md)
- AWS 실험 후 전용 인프라를 삭제했으며, 상시 운영 실적으로 표기하지 않습니다.

### 4. 래플 응모 서비스 · 배포와 장애 복구

기존 팀 프로젝트에 배포 분석과 장애 훈련을 추가했습니다. AWS에서 k6 상태 확인 부하를 45분 동안 보내며 RDS Multi-AZ 장애 전환을 실행했습니다. 연속 5회 요청 성공 기준 애플리케이션 복구 시간은 21.1초였습니다.

- Kubernetes · Argo Rollouts · GitHub Actions OIDC · Prometheus · Grafana · k6
- [코드](https://github.com/masondev1024/aws-data-platform-gitops) · [지속 부하·장애 전환 기록](https://github.com/masondev1024/aws-data-platform-gitops/blob/main/docs/soak-and-failover.md)
- 45분 상태 확인 부하는 응모 쓰기 처리량이 아닙니다. 별도 30 VU 응모 API의 p95는 510.9ms입니다.

## 함께 진행한 작업

- [ASK Seoul 에이전트](https://github.com/masondev1024/ask-seoul-agent): 공개 API만 사용하고 모델의 조회 범위를 제한한 데이터 조회 도구
- [청년 생활법률 상담 AI](https://github.com/masondev1024/youth_law_team_project): 법령 수집·검색 계층과 분야별 라우팅을 맡은 팀 프로젝트
