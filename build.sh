#!/usr/bin/env bash

python -m grpc_tools.protoc -I ./  --python_out=./ --grpc_python_out=./ ./user_service/authentication.proto
python -m grpc_tools.protoc -I ./  --python_out=./ ./session/session.proto
python -m grpc_tools.protoc -I ./  --python_out=./ --grpc_python_out=./ ./kensho_service/kensho.proto
