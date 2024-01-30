FROM python:latest

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml poetry.lock /src/
COPY requirements.txt requirements.txt 

# # Установка netcat
# RUN apt-get update \
#     && apt-get install -y netcat \
#     && rm -rf /var/lib/apt/lists/*
# Установка wait-for-it
RUN apt-get update \
    && apt-get install -y wait-for-it \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Установка SQLAlchemy
RUN poetry add sqlalchemy

COPY ./app /src/app
COPY ./database /src/database