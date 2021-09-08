import uuid

from django.contrib.auth import get_user_model
from django.db import models

from users.models import Profile

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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    message = models.CharField(max_length=200)
    profiles = models.ManyToManyField(
        Profile,
        related_name="notifications",
    )
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.message
