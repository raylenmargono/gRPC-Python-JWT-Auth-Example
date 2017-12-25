Example of using application defined Access Token
and Session Token (JWT) retrieved from user authentication
to access gRPC endpoint.

Demo:

1. docker-compose up
2. use AuthenticationClient to create/login user and retrieve token
3. use ACCESS_TOKEN and token in step 2. to access kensho_service
   using KenshoClient
