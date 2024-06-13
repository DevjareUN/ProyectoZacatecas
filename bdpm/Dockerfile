FROM ubuntu:22.04

RUN mkdir /bdpm

COPY . ./bdpm
WORKDIR ./bdpm

RUN apt-get -y update && apt-get -y install python3 python3-pip
RUN pip install -r requirements.txt
RUN python3 manage.py migrate

EXPOSE 4022

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:4022" ]
