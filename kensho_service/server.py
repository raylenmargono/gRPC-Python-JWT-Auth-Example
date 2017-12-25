import grpc
import requests

from kensho_service import kensho_pb2, kensho_pb2_grpc
from kensho_service.settings import settings
from session.kensho_session import KenshoSession

# https://www.kensho.com/team
KENSHO_TEAM_API = 'https://www.kensho.com/api/v1/team/member'


class KenshoServicer(kensho_pb2_grpc.KenshoServicer):

    @KenshoSession(
        access_token=settings.ACCESS_TOKEN,
        jwt_key=settings.JWT_SECRET,
        response_class=kensho_pb2.KenshoResponse
    )
    def DoKensho(self, request, context):
        response = requests.get(KENSHO_TEAM_API)
        if response.status_code == 200:
            team_list = response.json()
            for team_blob in team_list:
                payload = {
                    'photo': team_blob['photo'],
                    'display_name': team_blob['displayName'],
                    'first_name': team_blob['firstName'],
                    'last_name': team_blob['lastName'],
                    'education_snippet': team_blob['educationSnippet'],
                    'career_snippet': team_blob['careerSnippet'],
                }
                yield kensho_pb2.KenshoResponse(**payload)
        else:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details('Kensho service unavailable')
            return kensho_pb2.KenshoResponse()

    @KenshoSession(
        access_token=settings.ACCESS_TOKEN,
        jwt_key=settings.JWT_SECRET,
        response_class=kensho_pb2.KenshoResponse,
        permission_admin=True
    )
    def DoAdminKensho(self, request, context):
        return kensho_pb2.KenshoAdminResponse(response='Follow spitz_fluffy on Instagram')
