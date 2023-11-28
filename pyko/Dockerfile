# 기본 이미지 설정
FROM python:3.10.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFRED 1

RUN apt-get update

# 작업 디렉토리 설정
WORKDIR /pyko
COPY . /pyko/
RUN mkdir -p /pyko/logs

RUN pip install --upgrade pip
COPY ./requirements.txt  /pyko/
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn으로 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]