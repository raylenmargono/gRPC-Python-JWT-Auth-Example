FROM python:3.6.3

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

COPY kensho_service /src/kensho_service
COPY session /src/session
ADD docker/kensho_service/docker-entrypoint.sh /src/

WORKDIR kensho_service
RUN pip install -r requirements.txt
WORKDIR /src

ENTRYPOINT './docker-entrypoint.sh'
