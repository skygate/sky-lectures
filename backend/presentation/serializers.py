from rest_framework import serializers

from presentation.models import Comment


class RecursiveSerializer(serializers.RelatedField):
    def to_representation(self, value):
        serializer = CommentSerializer(value)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
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


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text"]
