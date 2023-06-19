from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from dashboard.models import State, District
from dashboard.serializers.states_districts import StateSerializer, DistrictSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class DistrictList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        state_name = request.query_params.get('state')

        try:
            state = State.objects.get(name=state_name)
        except State.DoesNotExist:
            return Response({"error": f"State '{state_name}' does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        districts = District.objects.filter(state=state)
        serializer = DistrictSerializer(districts, many=True)

        return Response(serializer.data)
