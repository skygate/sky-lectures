from rest_framework import viewsets

from resources.serializers import ResourceSerializer, PresentationSerializer
from resources.models import Resource, Presentation
from resources.permissions import IsAdminOrOwner, IsAdminOrReadOnly


class ResourceViewSet(viewsets.ModelViewSet):

    queryset = Resource.objects.all()
    serializer = ResourceSerializer
    permission_classes = [IsAdminOrOwner, IsAdminOrReadOnly]
    http_method_names = ("POST", "GET", "PATCH", "PUT")


class PresentationViewSet(viewsets.ModelViewSet):

    queryset = Presentation.objects.all()
    serializer = PresentationSerializer
    permission_classes = [IsAdminOrOwner, IsAdminOrReadOnly]
    http_method_names = ("POST", "GET")
