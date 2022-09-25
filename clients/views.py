from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from clients.serializers import ClientSerializer
from clients.models import Client


# API Client view
class APIClientsViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    # Only authenticated users
    permission_classes = (IsAuthenticated,)
