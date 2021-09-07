from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from presentation.filters import PresentationFilter
from presentation.models import Presentation, Tag
from presentation.paginations import StandardResultsSetPagination
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
    filterset_class = PresentationFilter
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        service = PresentationService()
        serializer = InputPresentationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        presentation = service.create_presentation(
            presentation_data=serializer.validated_data,
            user=request.user
        )

        return Response(data=self.get_serializer(presentation).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        service = PresentationService()
        partial = kwargs.pop("partial", False)
        presentation = self.get_object()
        serializer = InputPresentationSerializer(
            instance=presentation, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        presentation = service.update_presentation(
            presentation=presentation, presentation_data=serializer.validated_data, partial=partial
        )

        return Response(data=self.get_serializer(presentation).data, status=status.HTTP_200_OK)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = StandardResultsSetPagination
