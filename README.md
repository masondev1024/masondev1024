# 정성헌

금융·유통 고객사의 BI를 2년 5개월 운영하면서 보고서 숫자가 맞지 않으면 SQL과 원본 데이터부터 살폈습니다. 이후 개인 프로젝트에서는 AWS에 센서 수집 환경을 만들고, 원본에서 로봇별 하루 통계가 나오기까지 단계별로 건수를 대조했습니다.

[포트폴리오](https://jungseongheon.org/) · [이력서 PDF](https://jungseongheon.org/documents/jung-seongheon-data-engineer-v2.pdf) · [기술 블로그](https://velog.io/@mason_dev/posts)

## 대표 프로젝트

### [ASK Seoul](https://github.com/masondev1024/seoul-weather-platform)

팀에서 기상청 예보와 서울 교통 돌발 정보의 수집·게시 전 검사를 맡아 한국 시간과 행정동 기준을 맞췄습니다. 이후 개인 수집기의 첫 예약 실행에서 **빠진 예보 2회분**을 다시 받았고, 두 발표에 각각 80개 격자가 들어왔는지 원본과 대조했습니다. [예보 복구 기록](https://jungseongheon.org/portfolio/#ask-seoul-recovery)

### [Robot Data Platform](https://github.com/masondev1024/robot-data-pipeline)

합성 센서 기록을 로봇별 하루 통계로 만드는 개인 프로젝트입니다. Terraform으로 AWS 환경을 구성하고 Docker 이미지를 EKS에 배포했습니다. Kinesis로 받은 센서 데이터는 Firehose가 S3에 시간별 Parquet로 쌓습니다.

- **수집 시험** · 8월 24일 Kinesis 수신 41,000건, S3 Parquet 파일 생성 확인. [AWS 수집 기록](https://github.com/masondev1024/robot-data-pipeline/blob/cf49fe4284e9f7a035c063fb973c5cfe68772554/docs/public/RELIABILITY.md?plain=1#L50-L64)
- **배치 시험** · 8월 25일 Airflow 일배치와 같은 조건의 SQL을 Athena에서 직접 실행. 센서 원본 2,965행을 로봇 10대의 일별 통계 10행으로 집계. [배치 실행 결과](https://jungseongheon.org/portfolio/evidence/robot-batch-20260825.json)

### [Agentic Marketing Data Pipeline](https://github.com/masondev1024/agentic-marketing-data-pipeline)

주문·계약을 SQL로 조회하는 조사 API를 EC2에 배포했습니다. 모델 응답을 받기 전에 워커가 멈추면 같은 요청의 자동 재전송을 보류합니다. 워커 강제 종료 후 같은 요청을 다시 보냈을 때 **추가 호출 예약 0건**. [모델 호출 기록](https://jungseongheon.org/portfolio/#agentic-marketing)

### [GitOps 배포·복구](https://github.com/masondev1024/aws-data-platform-gitops)

래플 팀 프로젝트의 개인 후속 작업입니다. 두 버전이 동시에 뜰 때 CPU가 부족해 멈춘 EKS 배포를 할당량 조정과 수동 재동기화로 복구했습니다. **복구 후 응모 요청 10건 모두 성공**. 다음 배포부터는 두 버전의 CPU 요청량을 미리 합산해 한도와 대조합니다. [EKS 배포 복구 기록](https://jungseongheon.org/portfolio/#gitops)

---

[청년 법률 상담 AI](https://jungseongheon.org/portfolio/#youth-law) · [이어짐 삭제·복구 기록](https://github.com/masondev1024/ieojim/blob/main/docs/engineering/deletion-safe-restore.md) · [추가 프로젝트](https://jungseongheon.org/portfolio/#other-projects) · [이메일](mailto:masondev1024@gmail.com)
