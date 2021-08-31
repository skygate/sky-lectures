from rest_framework.viewsets import ModelViewSet

from users.models import Profile
from users.permissions import IsAdminOrOwner
from users.serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ["put", "get", "patch"]
    permission_classes = [IsAdminOrOwner]
