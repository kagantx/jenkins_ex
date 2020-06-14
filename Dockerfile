FROM python:3.6-jessie

WORKDIR /opt
ADD / /opt
ENTRYPOINT ["python","-u","/opt/main.py","echo $MYVAR"]

