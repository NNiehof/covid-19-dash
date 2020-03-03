FROM python:3.7.6-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8050

CMD python app.py