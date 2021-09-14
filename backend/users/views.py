from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from users.models import Profile
from users.serializers import (
    FavouritePresentationsSerializer,
    FavouriteTagsSerializer,
    ProfileSerializer,
    RegisterUserSerializer,
    UserSerializer,
)
from users.services import UserService
from users.permissions import IsAdminOrOwner, IsAdminOrProfileOwner


User = get_user_model()


class UserRegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrOwner]
    http_method_names = ["get", "post", "put", "patch"]

    @action(detail=True, methods=["put"], url_name="add_to_favourite_presentations")
    def add_to_favourite_presentations(self, request, pk):
        user = self.get_object()
        serializer = FavouritePresentationsSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserService().add_to_favourite_presentations(
            user=user, validated_data=serializer.validated_data
        )

        return Response(data=self.get_serializer(user).data, status=status.HTTP_200_OK)

    @action(
        detail=True, methods=["put"], url_name="remove_from_favourite_presentations"
    )
    def remove_from_favourite_presentations(self, request, pk):
        user = self.get_object()
        serializer = FavouritePresentationsSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserService().remove_from_favourite_presentations(
            user=user, validated_data=serializer.validated_data
        )

        return Response(data=self.get_serializer(user).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["put"], url_name="add_to_favourite_tags")
    def add_to_favourite_tags(self, request, pk):
        user = self.get_object()
        serializer = FavouriteTagsSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserService().add_to_favourite_tags(
            user=user, validated_data=serializer.validated_data
        )

        return Response(data=self.get_serializer(user).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["put"], url_name="remove_from_favourite_tags")
    def remove_from_favourite_tags(self, request, pk):
        user = self.get_object()
        serializer = FavouriteTagsSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserService().remove_from_favourite_tags(
            user=user, validated_data=serializer.validated_data
        )

        return Response(data=self.get_serializer(user).data, status=status.HTTP_200_OK)


class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrProfileOwner]

    def update(self, request, *args, **kwargs):
        service = UserService()
        profile = self.get_object()
        serializer = ProfileSerializer(
            profile, data=request.data, partial=kwargs.pop("partial", False)
        )
        serializer.is_valid(raise_exception=True)
        profile = service.update_user_profile(
            profile=profile, validated_data=serializer.validated_data
        )
        return Response(data=ProfileSerializer(profile).data, status=status.HTTP_200_OK)
