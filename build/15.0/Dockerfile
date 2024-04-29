FROM python:3.10-slim

ADD ./requirements.txt .
RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential libssl-dev libffi-dev python3-dev cargo gcc libxslt1-dev libxml2-dev python-dev-is-python3 libfreetype6-dev libsasl2-dev libldap2-dev libssl-dev libjpeg-dev zlib1g-dev python3-lxml libtool make python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev g++
RUN pip install -r requirements.txt
WORKDIR /opt/odoo