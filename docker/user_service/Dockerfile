FROM python:3.6.3

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

COPY user_service /src/user_service
ADD docker/user_service/docker-entrypoint.sh /src/
RUN mv user_service/run_grpc.py ./

RUN pip install -r user_service/requirements.txt

ENTRYPOINT './docker-entrypoint.sh'
