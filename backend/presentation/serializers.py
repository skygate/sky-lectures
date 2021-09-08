from rest_framework import serializers

from presentation.models import Comment


class RecursiveSerializer(serializers.RelatedField):
    def to_representation(self, value):
        serializer = CommentListSerializer(value)
        return serializer.data


class CommentListSerializer(serializers.ModelSerializer):
    replies = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "created_at",
            "user",
            "presentation_id",
            "reply_to",
            "replies",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text"]
