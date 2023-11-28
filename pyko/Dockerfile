# 기본 이미지 설정
FROM python:3.10.12

RUN apt-get update

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# 종속성 파일 복사
COPY requirements.txt ./

# Python 종속성 설치
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# Gunicorn으로 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]