FROM gcr.io/google_appengine/python
# init
RUN mkdir /northpole
WORKDIR /northpole
COPY requirements.txt /northpole/

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt
# clean
#RUN apk del -r python3-dev postgresql
# prep
ENV PYTHONUNBUFFERED 1
COPY . /northpole/

CMD /northpole/start.sh
