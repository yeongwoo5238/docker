# base image 설정
FROM python:3.12-alpine

# 작업디렉토리 
WORKDIR /code

# 환경변수
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# gcc 및 기타 종속성 패키지 설치
RUN apk add --no-cache gcc musl-dev linux-headers

# python 종속성 파일 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 이미지의 작업 디렉토리(.)에 현재 프로젝트 디렉토리 복사                 	
COPY . .

# 컨테이너 대기 포트 5000
EXPOSE 5000

# 컨테이너 실행 기본 명령 설정
CMD ["flask", "run", "--debug"]
