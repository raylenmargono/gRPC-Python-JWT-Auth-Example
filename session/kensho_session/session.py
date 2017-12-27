import grpc
import jwt

_ACCESS_TOKEN_ERROR_MSG = 'Invalid access_token'
_SESSION_TOKEN_ERROR_MSG = 'Invalid session_token'
_SESSION_TOKEN_EXPIRED_MSG = 'Expired session_token'
_PERMISSION_EXPIRED_MSG = 'Endpoint is restricted access'


def get_user_info_from_context(context, jwt_key):
    metadata = dict(context.invocation_metadata())
    session_token = metadata['session_token']
    user_info = jwt.decode(session_token, key=jwt_key).get('user_info')
    return user_info


class KenshoSession(object):

    def __init__(self, response_class, access_token=None, jwt_key=None, permission_admin=False):
        self.access_token = access_token
        self.jwt_key = jwt_key
        self.response_class = response_class
        self.permission_admin = permission_admin

    def __call__(self, func):
        def _kensho_session(instance, request, context):
            success, error_handler = self.do_authentication(context)
            if not success:
                return error_handler
            return func(instance, request, context)
        return _kensho_session

    def do_authentication(self, context):
        metadata = dict(context.invocation_metadata())
        access_token = metadata['access_token']
        session_token = metadata['session_token']
        if self.has_access_token_error(access_token):
            return False, self.invalidate(context, _ACCESS_TOKEN_ERROR_MSG)
        has_error, details = self.has_jwt_error(session_token)
        if has_error:
            return False, self.invalidate(context, details)
        return True, None

    def has_access_token_error(self, access_token):
        return self.access_token and access_token != self.access_token

    def has_jwt_error(self, session_token):
        if self.jwt_key:
            try:
                user_info = jwt.decode(session_token, key=self.jwt_key).get('user_info')
            except jwt.DecodeError:
                return True, _SESSION_TOKEN_ERROR_MSG
            except jwt.ExpiredSignatureError:
                return True, _SESSION_TOKEN_EXPIRED_MSG
            if self.permission_admin and not user_info.get('is_admin'):
                return True, _PERMISSION_EXPIRED_MSG
        return False, None

    def invalidate(self, context, details):
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details(details)
        return self.response_class()
