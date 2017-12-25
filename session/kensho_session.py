import grpc
import jwt

_ACCESS_TOKEN_ERROR_MSG = 'Invalid access_token'
_SESSION_TOKEN_ERROR_MSG = 'Invalid session_token'
_SESSION_TOKEN_EXPIRED_MSG = 'Expired session_token'
_PERMISSION_EXPIRED_MSG = 'Endpoint is restricted access'


class KenshoSession(object):

    def __init__(self, response_class, access_token=None, jwt_key=None, permission_admin=False):
        self.access_token = access_token
        self.jwt_key = jwt_key
        self.response_class = response_class
        self.permission_admin = permission_admin

    def __call__(self, func):
        def _kensho_session(instance, request, context):
            user_info, error_handler = self.do_authentication(context)
            if not user_info:
                return error_handler
            return func(instance, request, context, user_info)
        return _kensho_session

    def do_authentication(self, context):
        metadata = dict(context.invocation_metadata())
        access_token = metadata['access_token']
        session_token = metadata['session_token']
        if self.has_access_token_error(access_token):
            return None, self.invalidate(context, _ACCESS_TOKEN_ERROR_MSG)
        user_info, error_details = self.get_user_info(session_token)
        if error_details:
            return False, self.invalidate(context, error_details)
        return user_info, None

    def has_access_token_error(self, access_token):
        return self.access_token and access_token != self.access_token

    def get_user_info(self, session_token):
        user_info = None
        if self.jwt_key:
            try:
                user_info = jwt.decode(session_token, key=self.jwt_key).get('user_info')
            except jwt.DecodeError:
                return None, _SESSION_TOKEN_ERROR_MSG
            except jwt.ExpiredSignatureError:
                return None, _SESSION_TOKEN_EXPIRED_MSG
            if self.permission_admin and not user_info.get('is_admin'):
                return None, _PERMISSION_EXPIRED_MSG
        return user_info, None

    def invalidate(self, context, details):
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details(details)
        return self.response_class()
