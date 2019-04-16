FROM python:3-slim
LABEL maintainer="github@opensorcery.io"
ENV PYTHONUNBUFFERED 1
COPY . /code/
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 8000/tcp
