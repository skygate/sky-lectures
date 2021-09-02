from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import Profile
from users.permissions import IsAdminOrOwner
from users.serializers import ProfileSerializer
from users.services import UserService


class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrOwner]

    def update(self, request, *args, **kwargs):
        service = UserService()
        profile = self.get_object()
        serializer = ProfileSerializer(
            profile, data=request.data, partial=kwargs.pop("partial", False)
        )
        serializer.is_valid(raise_exception=True)
        profile = service.update_user_profile(profile, serializer.validated_data)
        return Response(data=ProfileSerializer(profile).data, status=status.HTTP_200_OK)
