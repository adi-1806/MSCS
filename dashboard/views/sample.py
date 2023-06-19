from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView

from dashboard.serializers.registrations import *
from dashboard.models import *


class Sample(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        name = "adithya"
        return Response(name)
