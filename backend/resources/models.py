import os
import uuid

from django.db import models


def get_file_path(instance, filepath):
    return os.path.join("files/", f"{instance.path}")


class Presentation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    path = models.FileField(upload_to=get_file_path, blank=True)
    uploaded_on = models.DateField()
    fk_pres_id = models.ForeignKey(Presentation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
