 FROM python:3
 RUN apt update -y
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 COPY requirements.txt /code/
 RUN pip install -r requirements.txt
 COPY . /code/
