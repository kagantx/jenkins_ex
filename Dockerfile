FROM python:3.6-jessie

WORKDIR /opt
ADD / /opt
RUN pip install requirements.txt
ENTRYPOINT ["python","-u","/opt/main.py","500"]


