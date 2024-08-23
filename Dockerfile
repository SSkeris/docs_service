FROM python:3.12

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY /requirements.txt /

RUN pip install --upgrade pip && pip install -r /requirements.txt --no-cache-dir

COPY . .