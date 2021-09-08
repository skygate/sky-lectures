import uuid

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Presentation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    reply_to = models.ForeignKey(
        "self", on_delete=models.SET_NULL, related_name="replies", blank=True, null=True
    )
    presentation_id = models.ForeignKey(
        Presentation, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return f"Comment: {self.text}"
