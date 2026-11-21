# 정성헌

금융·유통 고객사의 BI 보고서를 2년 5개월 동안 개발하고 운영했습니다. 보고서 숫자가 맞지 않을 때는 SQL로 원본을 조회해 어디서 값이 달라졌는지 따라갔습니다. 최근에는 AWS에 센서 데이터를 쌓고 SQL로 로봇별 하루 통계를 내는 파이프라인을 만들었습니다.

[포트폴리오](https://jungseongheon.org/) · [이력서 PDF](https://jungseongheon.org/documents/jung-seongheon-data-engineer-v2.pdf) · [기술 블로그](https://velog.io/@mason_dev/posts)

## 대표 프로젝트

### [ASK Seoul](https://github.com/masondev1024/seoul-weather-platform)

기업 연계 팀 프로젝트에서 기상청 예보와 서울 교통 돌발 정보 수집을 맡았습니다. 두 자료를 같은 시간대와 지역으로 조회할 수 있도록 한국 시간과 행정동을 기준으로 정리했습니다. 프로젝트가 끝난 뒤에는 예보가 빠지면 다음 수집 때 다시 받도록 수집기를 고쳤습니다. 수정 후 첫 예약 실행에서 빠졌던 예보 두 회분이 들어왔고, 각각 서울 80개 격자의 자료가 있는지 원본을 대조했습니다. [예보 복구 기록](https://jungseongheon.org/portfolio/#ask-seoul-recovery)

### [Robot Data Platform](https://github.com/masondev1024/robot-data-pipeline)

가상의 로봇 센서 데이터를 보내는 프로그램을 Docker 이미지로 만들어 EKS에 배포하고, AWS 환경은 Terraform으로 구성했습니다. Kinesis에는 로봇 ID를 기준으로 나눠 보내지만, S3에는 시간대별로 묶어 저장합니다. 로봇마다 작은 파일이 쌓이는 걸 줄이기 위해서입니다.

8월 24일에는 Kinesis가 센서 기록 41,000건을 받았고 Firehose가 S3에 Parquet 파일을 쓰는지 확인했습니다. 다음 날에는 별도 데이터 2,965행으로 Athena에서 일별 집계 SQL을 직접 실행했습니다. 로봇 10대의 하루 통계가 한 줄씩 나왔습니다. [AWS 수집 기록](https://github.com/masondev1024/robot-data-pipeline/blob/cf49fe4284e9f7a035c063fb973c5cfe68772554/docs/public/RELIABILITY.md?plain=1#L50-L64) · [배치 실행 결과](https://jungseongheon.org/portfolio/evidence/robot-batch-20260825.json)

### [Agentic Marketing Data Pipeline](https://github.com/masondev1024/agentic-marketing-data-pipeline)

주문·계약 데이터를 SQL로 조회해 마케팅 질문에 답하는 API를 EC2에 올렸습니다. 모델에 요청을 보낸 직후 워커가 멈추면 같은 요청에 비용이 두 번 들 수 있어, 호출 상태를 따로 기록합니다. 워커를 중간에 끄고 같은 요청을 다시 넣어 봐도 추가 호출은 예약되지 않았습니다. [모델 호출 기록](https://jungseongheon.org/portfolio/#agentic-marketing)

### [GitOps 배포·복구](https://github.com/masondev1024/aws-data-platform-gitops)

팀 프로젝트가 끝난 뒤 응모 서비스의 새 버전을 EKS에 올리다가 배포가 멈춘 적이 있습니다. 기존 버전과 새 버전을 함께 띄울 만큼 CPU가 남지 않은 게 원인이었습니다. 할당량을 6코어에서 8코어로 늘리고 수동으로 다시 동기화한 뒤 응모 10건이 모두 접수됐습니다. 이후에는 두 버전의 CPU 요청량을 배포 전에 검사합니다. [EKS 배포 복구 기록](https://jungseongheon.org/portfolio/#gitops)

---

[청년 법률 상담 AI](https://jungseongheon.org/portfolio/#youth-law) · [이어짐 삭제·복구 기록](https://github.com/masondev1024/ieojim/blob/main/docs/engineering/deletion-safe-restore.md) · [추가 프로젝트](https://jungseongheon.org/portfolio/#other-projects) · [이메일](mailto:masondev1024@gmail.com)
