FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN python -m pip install --upgrade pip

RUN mkdir app
RUN mkdir src
COPY ./app /app
COPY ./src /src
WORKDIR /app

# create the user for security purposes
# so it wont run in root/admin
RUN adduser -D user
USER user