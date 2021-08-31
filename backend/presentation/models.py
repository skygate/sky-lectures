import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Presentation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="presentations",
        null=True,
        blank=True,
    )
    scheduled_on = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
