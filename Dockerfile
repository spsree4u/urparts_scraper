FROM python:3.9.15-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY Pipfile Pipfile.lock /django/
RUN pip install pipenv && pipenv install -ignore-pipfile
COPY . /django/