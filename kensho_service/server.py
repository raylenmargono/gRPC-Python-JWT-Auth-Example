import grpc
import requests

from settings import settings
from kensho_service_client.proto import kensho_pb2, kensho_pb2_grpc
from kensho_session.session import KenshoSession, get_user_info_from_context

# https://www.kensho.com/team

KENSHO_TEAM_API = 'https://www.kensho.com/api/v1/team/member'


class KenshoServicer(kensho_pb2_grpc.KenshoServicer):

    @KenshoSession(
        response_class=kensho_pb2.KenshoResponse,
        access_token=settings.ACCESS_TOKEN,
        jwt_key=settings.JWT_SECRET
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
        response_class=kensho_pb2.KenshoResponse,
        access_token=settings.ACCESS_TOKEN,
        jwt_key=settings.JWT_SECRET,
        permission_admin=True
    )
    def DoAdminKensho(self, request, context):
        user_info = get_user_info_from_context(context, settings.JWT_SECRET)
        username = user_info['username'] if user_info else 'Anon'
        return kensho_pb2.KenshoAdminResponse(response='{}: Follow spitz_fluffy on Instagram'.format(username))
