from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from users.models import Profile
from users.serializers import ProfileSerializer, RegisterUserSerializer, UserSerializer
from users.services import UserService
from users.permissions import IsAdminOrOwner


User = get_user_model()


class UserRegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrOwner]
    http_method_names = ['get', 'post', 'put', 'patch']


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
