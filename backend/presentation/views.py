from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from presentation.models import Presentation, Tag
from presentation.permissions import IsAdminOrOwner, IsAdminOrReadOnly
from presentation.serializers import (
    InputPresentationSerializer,
    OutputPresentationSerializer,
    TagSerializer,
)
from presentation.services import PresentationService


class PresentationViewSet(ModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = OutputPresentationSerializer
    permission_classes = [IsAdminOrOwner]
    services = PresentationService()

    def create(self, request, *args, **kwargs):
        serializer = InputPresentationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.services.create_presentation(
            validated_data=serializer.validated_data
        )
        serializer = InputPresentationSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = InputPresentationSerializer(
            instance=instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)

        instance = self.services.update_presentation(
            instance=instance, validated_data=serializer.validated_data, partial=partial
        )
        serializer = InputPresentationSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]
