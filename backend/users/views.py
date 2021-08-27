from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from users.serializers import RegisterUserSerializer, UserSerializer
from users.permissions import IsAdminOrOwner

User = get_user_model()


class UserRegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrOwner]
    http_method_names = ['get', 'post', 'put', 'patch']
