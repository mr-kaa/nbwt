# FROM python:3.9.0-alpine3.12
FROM python:3.9.0

ENV USER usr
ENV HOME /home/${USER}

# RUN apk update && \
#     apk upgrade && \
#     apk add --no-cache --virtual .build-deps \
#     gcc \
#     python3-dev \
#     musl-dev \
#     postgresql-dev \
#     build-base py-pip jpeg-dev zlib-dev\
#     && pip install --no-cache-dir psycopg2 Pillow \
#     && apk del --no-cache .build-deps

RUN apt-get update && \
    apt-get upgrade -y


# ENV LIBRARY_PATH=/lib:/usr/lib

WORKDIR ${HOME}

COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

# COPY ./requirements.txt /tmp/
# RUN pip install -r /tmp/requirements.txt

COPY . ${HOME}
