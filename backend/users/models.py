import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


def get_file_path(instance, filename):
    return os.path.join("images/", f"avatar_image_{instance.user.id}.jpeg")


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    favourite_presentations = models.ManyToManyField(
        "presentation.Presentation", related_name="favourite_presentations", blank=True
    )
    favourite_tags = models.ManyToManyField(
        "presentation.Tag", related_name="favourite_tags", blank=True
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    description = models.CharField(max_length=200, blank=True)
    file = models.ImageField(upload_to=get_file_path, blank=True)
    upload_date = models.DateTimeField(auto_now=True, editable=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        primary_key=True,
    )

    def __str__(self):
        return f"Profile of user {self.user.username}"
