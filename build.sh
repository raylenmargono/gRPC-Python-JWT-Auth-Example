#!/usr/bin/env bash

python -m grpc_tools.protoc -I ./pkgs/kensho_service_client/  \
--python_out=./pkgs/kensho_service_client/ \
--grpc_python_out=./pkgs/kensho_service_client/ \
./pkgs/kensho_service_client/kensho_service_client/proto/kensho.proto

python -m grpc_tools.protoc -I ./pkgs/user_service_client/  \
--python_out=./pkgs/user_service_client/ \
--grpc_python_out=./pkgs/user_service_client/ \
./pkgs/user_service_client/user_service_client/proto/authentication.proto
