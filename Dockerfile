FROM python:3

RUN mkdir /northpole
WORKDIR /northpole
COPY requirements.txt /northpole/

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

#RUN apk del -r python3-dev postgresql

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV PYTHONUNBUFFERED 1
COPY . /northpole/
