import grpc

from user_service import authentication_pb2_grpc, authentication_pb2
from user_service.models import User


class AuthenticationServicer(authentication_pb2_grpc.AuthenticationServicer):

    def Login(self, request, context):
        username = request.username
        password = request.password
        token = User.login(username, password)
        if token:
            return authentication_pb2.LoginResponse(token=token)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details('Invalid username or password')
        return authentication_pb2.LoginResponse()

    def SignUp(self, request, context):
        username = request.username
        password = request.password
        email = request.email
        is_admin = request.is_admin
        result, success = User.create(username, password, email, is_admin=is_admin)
        if success:
            return authentication_pb2.SignUpResponse(token=result)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details(result)
        return authentication_pb2.SignUpResponse()
