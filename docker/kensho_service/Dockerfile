FROM python:3.6.3

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

COPY kensho_service /src/kensho_service
COPY session /src/kensho_service/session
ADD docker/kensho_service/docker-entrypoint.sh /src/

RUN pip install -r kensho_service/requirements.txt

ENTRYPOINT './docker-entrypoint.sh'
