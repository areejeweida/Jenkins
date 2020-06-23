FROM python:3.6-jessie

ADD . /jenkins
WORKDIR /jenkins
RUN pip install -r requirements.txt
ENV list_of_urls="https://vsupalov.com/"

ENTRYPOINT python -u urls.py $Arg1
