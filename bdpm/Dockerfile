FROM ubuntu:22.04

RUN mkdir /bdpm

COPY . ./bdpm
WORKDIR ./bdpm

RUN apt-get -y update && apt-get -y install libpq-dev gcc python3 python3-pip
RUN pip install -r requirements.txt

EXPOSE 8000
