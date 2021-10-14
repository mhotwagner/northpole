FROM python:3

ARG DJANGO_SETTINGS_MODULE

RUN mkdir /northpole
WORKDIR /northpole
COPY requirements.txt /northpole/

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

#RUN apk del -r python3-dev postgresql

<<<<<<< Updated upstream
#Enable bash on heroku exec
#RUN rm /bin/sh && ln -s /bin/bash /bin/sh
=======
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
>>>>>>> Stashed changes

ENV PYTHONUNBUFFERED 1
COPY . /northpole/
