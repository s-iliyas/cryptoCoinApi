FROM ubuntu:22.04
ARG BASE_DIR=/var/www
ARG WEBSITE_NAME=backend
ENV WEBSITE_NAME=${WEBSITE_NAME}
RUN apt-get update && apt-get install -y apache2 libgeos-dev\
    libapache2-mod-wsgi-py3 \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3\
    python3-pip \
    vim \
    sudo \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update \
    && apt-get -y install libpq-dev gcc  ca-certificates openssl\
    && pip3 install psycopg2
RUN echo "ServerName 0.0.0.0" >> /etc/apache2/apache2.conf
COPY ./modules.txt .
RUN pip3 install -r modules.txt
COPY ./ .
RUN a2enmod headers
RUN  service apache2 restart
EXPOSE 8000
RUN mkdir ${BASE_DIR}/${WEBSITE_NAME}
ENTRYPOINT ["/bin/bash", "/var/www/start.sh"]
