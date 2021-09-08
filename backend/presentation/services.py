class CommentService:
    def update_comment(self, comment, validated_data):
        comment.text = validated_data.get("text", comment.text)
        comment.save(update_fields=["text"])
        return comment

    def set_comment_user(self, serializer, request):
        serializer.save(user=request.user)
