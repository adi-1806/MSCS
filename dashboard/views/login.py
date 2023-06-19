from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from dashboard.serializers.login import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from dashboard.models import *


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.data

        email = request_data['email']
        password = request_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_info = Societies.objects.get(email_id=email)

            return Response(
                {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'user_id': user_info.id,
                    'email': user_info.email_id,
                    'name': user_info.name,
                    'message': 'Login Success',
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'message': 'Email or Password is not Valid'},
                status=status.HTTP_404_NOT_FOUND
            )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        request_data = request.data
        try:
            refresh_token = request_data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logged Out Successfully'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
