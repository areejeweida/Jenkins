FROM python:3.6-jessie

ADD . /jenkins
WORKDIR /jenkins
RUN pip install -r requirements.txt


