FROM alpine
# init
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
# setup
RUN apk update
RUN apk upgrade

RUN apk --no-cache add \
    python3 \
    python3-dev \
    postgresql-client \
    postgresql-dev \
    libffi-dev \
    build-base \
    gettext

RUN apk add libgit2-dev --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# clean
RUN apk del -r python3-dev postgresql
# prep
ENV PYTHONUNBUFFERED 1
COPY . /app/