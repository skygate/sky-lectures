import uuid

from django.contrib.auth import get_user_model
from django.db import models

from presentation.managers import NotificationManager

User = get_user_model()


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Presentation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="presentations",
        null=True,
    )
    scheduled_on = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="presentations")
    notification_sent = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    message = models.CharField(max_length=200)
    user = models.ForeignKey(
        User,
        related_name="notifications",
        on_delete=models.CASCADE,
    )
    reviewed = models.BooleanField(default=False)

    objects = NotificationManager()

    def __str__(self):
        return self.message


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