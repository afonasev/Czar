FROM python:3.6.2-alpine3.6

ENV PYTHONUNBUFFERED=1

RUN mkdir /var/db
ADD . /var/src
WORKDIR /var/src

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8000
