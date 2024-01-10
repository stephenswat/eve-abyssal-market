FROM debian:bookworm

RUN apt-get update
RUN apt-get install -y nginx npm

COPY package-lock.json package.json /code/

WORKDIR /code/

RUN npm install
