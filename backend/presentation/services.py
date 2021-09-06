class CommentService:
    def update_comment(self, comment, validated_data):
        comment.text = validated_data.get("text", comment.text)
        comment.save()
        return comment
