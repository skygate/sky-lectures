from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from presentation.models import Comment
from presentation.permissions import IsAdminOrOwner
from presentation.serializers import CommentSerializer, CommentUpdateSerializer
from presentation.services import CommentService


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAdminOrOwner,
    ]
    http_method_names = ["get", "post", "put", "patch"]

    def perform_create(self, serializer):
        CommentService().set_comment_user(serializer=serializer, user=self.request.user)

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = CommentUpdateSerializer(comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        comment = CommentService().update_comment(
            comment=comment, validated_data=serializer.validated_data
        )

        return Response(
            data=self.get_serializer(comment).data, status=status.HTTP_200_OK
        )
