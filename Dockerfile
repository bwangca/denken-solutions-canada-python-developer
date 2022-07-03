FROM python:3.10.4

RUN mkdir /opt/sample/
WORKDIR /opt/sample/

COPY requirements.txt .
COPY dist/sample /opt/sample/

EXPOSE 80

CMD [ "./sample" ]