FROM gcr.io/google_appengine/python
# init
RUN mkdir /northpole
WORKDIR /northpole
COPY requirements.txt /northpole/
## setup
#RUN apk update
#RUN apk upgrade
#
#RUN apk --no-cache add \
#    python3 \
#    python3-dev \
#    postgresql-client \
#    postgresql-dev \
#    libffi-dev \
#    build-base \
#    gettext \
#    zsh
#
#RUN apk add libgit2-dev --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main


RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt
# clean
#RUN apk del -r python3-dev postgresql
# prep
ENV PYTHONUNBUFFERED 1
COPY . /northpole/