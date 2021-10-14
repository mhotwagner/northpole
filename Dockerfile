FROM python:3

ARG DJANGO_SETTINGS_MODULE

RUN mkdir /northpole
WORKDIR /northpole
COPY requirements.txt /northpole/

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

#RUN apk del -r python3-dev postgresql \

# Enable bash on heroku exec
RUN apk add bash curl openssh iproute2
COPY deploy/.profile.d/heroku-exec.sh /app/.profile.d/
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV PYTHONUNBUFFERED 1
COPY . /northpole/
