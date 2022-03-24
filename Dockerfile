FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
