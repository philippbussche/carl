FROM python:3.6.4-alpine3.6
MAINTAINER Philipp von dem Bussche <philipp.bussche@gmail.com>

COPY requirements.txt /

RUN pip install -r requirements.txt && \
    mkdir /carl

COPY src /carl

COPY docker/entrypoint.sh /entrypoint.sh

ENV PATH ${PATH}:/carl

ENTRYPOINT ["/entrypoint.sh"]
