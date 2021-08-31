from rest_framework.viewsets import ModelViewSet

from presentation.models import Presentation, Tag
from presentation.permissions import IsAdminOrOwner, IsAdminOrCanOnlyGetPost
from presentation.serializers import PresentationSerializer, TagSerializer


class PresentationViewSet(ModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer
    permission_classes = [IsAdminOrOwner]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrCanOnlyGetPost]
