FROM debian:bullseye


RUN apt-get update
RUN apt-get install -y python3 python-is-python3 python3-pip libpq-dev
RUN pip3 install poetry

COPY pyproject.toml poetry.lock /code/
WORKDIR /code/
RUN poetry install
COPY . /code/
