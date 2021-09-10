from typing import OrderedDict

from django.contrib.auth import get_user_model

from presentation.models import Comment
from presentation.serializers import CommentSerializer


User = get_user_model()


class CommentService:
    def update_comment(self, comment: Comment, validated_data: OrderedDict) -> Comment:
        comment.text = validated_data.get("text", comment.text)
        comment.save(update_fields=["text"])
        return comment

    def set_comment_user(self, serializer: CommentSerializer, user: User) -> None:
        serializer.save(user=user)
