import grpc
from google.protobuf import json_format

from kensho_service import kensho_pb2, kensho_pb2_grpc


class KenshoClient(object):
    def __init__(self, host, session_token, access_token):
        self.channel = grpc.insecure_channel(host)
        stub = kensho_pb2_grpc.KenshoStub(self.channel)
        self._stub = stub
        self._auth = [
            ('session_token', session_token),
            ('access_token', access_token)
        ]

    def do_kensho(self):
        request = kensho_pb2.KenshoRequest()
        response = self._stub.DoKensho(request, metadata=self._auth)
        for record in response:
            yield json_format.MessageToDict(record, including_default_value_fields=True,
                                            preserving_proto_field_name=True)

    def do_admin_kensho(self):
        request = kensho_pb2.KenshoAdminRequest()
        response = self._stub.DoAdminKensho(request, metadata=self._auth)
        return json_format.MessageToDict(response, including_default_value_fields=True,
                                         preserving_proto_field_name=True)
