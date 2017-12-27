FROM python:3.6.3

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

COPY user_service /src/user_service
COPY pkgs /src/pkgs
ADD docker/user_service/docker-entrypoint.sh /src/

WORKDIR /src/user_service
RUN pip install -r requirements.txt
WORKDIR /src

ENTRYPOINT './docker-entrypoint.sh'
