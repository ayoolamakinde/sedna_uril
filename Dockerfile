FROM python:3.9-alpine

COPY . /web

WORKDIR /web/api

RUN pip install flask hashids

CMD ["python", "app.py"]
