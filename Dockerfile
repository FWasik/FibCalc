#FROM python:3.9.4-slim
FROM python:3.9.6-alpine

WORKDIR /code/app

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY /app /app/code