FROM python:3.6-jessie

ADD . /jenkins
WORKDIR /jenkins
ENTRYPOINT python -u urls.py $Arg1