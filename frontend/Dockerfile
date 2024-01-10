FROM debian:bookworm

RUN apt-get update
RUN apt-get install -y nginx npm

COPY . /code/
WORKDIR /code/
