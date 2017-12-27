from datetime import datetime, timedelta

import jwt

import unittest

from kensho_session import get_user_info_from_context

MOCK_ACCESS_TOKEN = 'MOCK_ACCESS_TOKEN'
MOCK_INVALID_ACCESS_TOKEN = 'MOCK_INVALID_ACCESS_TOKEN'
MOCK_JWT_KEY = 'MOCK_JWT_KEY'
MOCK_INVALID_JWT_KEY = 'MOCK_JWT_KEY'

MOCK_USER_NON_ADMIN_INFO = {
    'username': 'fake_username',
    'is_admin': False
}
MOCK_USER_ADMIN_INFO = {
    'username': 'fake_admin_username',
    'is_admin': True
}


def gen_jwt_token(user_info, exp, secret):
    return jwt.encode({
        'user_info': user_info,
        'exp': exp
    }, secret, algorithm='HS256')


class MockContext(object):

    def __init__(self, session_token, access_token):
        self.session_token = session_token
        self.access_token = access_token

    def invocation_metadata(self):
        return (
            ('session_token', self.session_token),
            ('access_token', self.access_token)
        )


class KenshoSessionTest(unittest.TestCase):

    def test_get_user_info_from_context(self):
        exp = datetime.utcnow() + timedelta(days=1)
        session_token = gen_jwt_token(MOCK_USER_ADMIN_INFO,
                                      exp,
                                      MOCK_JWT_KEY)
        valid_context = MockContext(session_token, MOCK_ACCESS_TOKEN)
        user_info = get_user_info_from_context(valid_context, MOCK_JWT_KEY)
        self.assertDictEqual(user_info, MOCK_USER_ADMIN_INFO)

    def test_as_decorator(self):
        pass

    def test_access_token_error(self):
        pass

    def test_has_jwt_error(self):
        pass

    def test_do_authentication(self):
        pass
