#!/usr/bin/env bash

python -m grpc_tools.protoc -I ./user_service  --python_out=./user_service/ --grpc_python_out=./user_service/ ./user_service/proto/authentication.proto
python -m grpc_tools.protoc -I ./kensho_service  --python_out=./kensho_service/ --grpc_python_out=./kensho_service/ ./kensho_service/proto/kensho.proto
