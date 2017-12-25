import grpc
from google.protobuf import json_format

from user_service import authentication_pb2_grpc, authentication_pb2


class AuthenticationClient(object):
    def __init__(self, host):
        self.channel = grpc.insecure_channel(host)
        stub = authentication_pb2_grpc.AuthenticationStub(self.channel)
        self._stub = stub

    def login(self, username, password):
        request = authentication_pb2.LoginRequest(username=username, password=password)
        response = self._stub.Login(request)
        return json_format.MessageToDict(response, including_default_value_fields=True,
                                         preserving_proto_field_name=True)

    def signup(self, username, password, email, is_admin=False):
        request = authentication_pb2.SignUpRequest(username=username, password=password, email=email, is_admin=is_admin)
        response = self._stub.SignUp(request)
        return json_format.MessageToDict(response, including_default_value_fields=True,
                                         preserving_proto_field_name=True)
