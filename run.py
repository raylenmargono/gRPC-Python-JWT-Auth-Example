from user_service.client import AuthenticationClient
from kensho_service.client import KenshoClient

c = AuthenticationClient('localhost:8000')

token = c.login('test2@test.com', 'test').get('token')
k = KenshoClient('localhost:5000', token, 'access_token')
k.do_admin_kensho()
