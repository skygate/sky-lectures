from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from presentation.models import Comment
from presentation.permissions import IsAdminOrOwner
from presentation.serializers import CommentListSerializer, CommentSerializer
from presentation.services import CommentService


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [
        IsAdminOrOwner,
    ]
    http_method_names = ["get", "post", "put", "patch"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        service = CommentService()
        comment = self.get_object()
        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = service.update_comment(comment, serializer.validated_data)
        return Response(
            data=CommentListSerializer(comment).data, status=status.HTTP_200_OK
        )
