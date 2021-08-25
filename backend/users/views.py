from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import RegisterUserSerializer


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer
