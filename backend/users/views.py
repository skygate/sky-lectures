from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import Profile
from users.permissions import IsAdminOrOwner
from users.serializers import ProfileSerializer


class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrOwner]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProfileSerializer(
            instance, data=request.data, partial=kwargs.pop("partial", False)
        )
        serializer.is_valid()
        instance.file = serializer.validated_data.get("file", instance.file)
        instance.description = serializer.validated_data.get(
            "description", instance.description
        )
        instance.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
