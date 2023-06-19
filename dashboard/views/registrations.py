from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from dashboard.serializers.registrations import *
from dashboard.models import *


class Registration(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = RegistrationsSerializer

    @staticmethod
    def create(request):
        serializer = RegistrationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        request_data = serializer.data
        user = CustomUser.objects.create(
            username=request_data['name'],
            email=request_data['email_id'])
        password = request_data['password']
        user.set_password(password)
        user.save()

        Societies.objects.create(
            state=request_data['state'],
            district=request_data['district'],
            type=request_data['type'],
            name=request_data['name'],
            address=request_data['address'],
            pan=request_data['pan'],
            tan=request_data['tan'],
            name_of_md=request_data['name_of_md'],
            designation=request_data['designation'],
            mobile_no=request_data['mobile_no'],
            email_id=request_data['email_id'],
            service_tax_no=request_data['service_tax_no'],
            user=user)

        email = request_data['email_id']
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
            return Response({'message': 'Registration is not Valid'}, status=status.HTTP_404_NOT_FOUND)


class RegistrationsRetrieveAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        registrations = Societies.objects.all()
        serializer = RegistrationsRetrieveSerializer(registrations, many=True)
        return Response(serializer.data)
