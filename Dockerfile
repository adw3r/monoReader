FROM python:3.11-alpine

WORKDIR app

RUN pip install poetry

COPY . .

RUN poetry install
