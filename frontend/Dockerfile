FROM node:alpine
LABEL maintainer="github@opensorcery.io"
RUN mkdir /code
COPY package*.json /code/
WORKDIR /code
RUN npm install
COPY . /code
ENV PATH /code/node_modules/.bin:$PATH
EXPOSE 8080/tcp
