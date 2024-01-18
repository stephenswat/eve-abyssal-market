FROM debian:bookworm

ARG DEBIAN_FRONTEND=noninteractive

ENV POETRY_HOME="/opt/poetry/"

RUN apt-get update
RUN apt-get install -y python3 python-is-python3 python3-pip libpq-dev curl ca-certificates
RUN curl -sSL https://install.python-poetry.org > install_poetry.py
RUN python3 install_poetry.py --version 1.7.1

ENV PATH="${PATH}:${POETRY_HOME}/bin"

COPY pyproject.toml poetry.lock /code/
WORKDIR /code/
RUN poetry install
