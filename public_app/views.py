from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


class UserLoginV(APIView):
    permisssion_class = []

    def post(self, request):
        context = {'username': 'Guest', 'login_state': False}
        post_data = request.data
        username = post_data.get('username')
        password = post_data.get('password')
        user_authenticated = authenticate(username=username, password=password)
        if user_authenticated is not None:
            auth_login(request, user_authenticated)
            context = {'username': username, 'login_state': True}
        return Response(context)


class UserLogoutV(APIView):
    permission_class = []

    def post(self, request):
        auth_logout(request)
        return Response(None, status=status.HTTP_200_OK)


class UserInfoV(APIView):
    permission_class = []

    def get(self, request):
        if not request.user.is_authenticatd:
            raise exceptions.NotAuthenticated('This user is not authenticated!')
        else:
            return Response({'username': request.user.username, 'login_state': True})