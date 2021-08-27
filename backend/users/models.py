import os
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


def get_file_path(instance, filename):
    filename = f"avatar_image_{instance.user.id}.jpeg"
    os.remove(os.path.join(settings.MEDIA_ROOT, "images/", filename))

    return os.path.join("images/", filename)


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True, name="id"
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
        primary_key=True,
        related_name="profile",
        editable=False,
    )

    def __str__(self):
        return self.user.username
