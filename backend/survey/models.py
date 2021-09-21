import uuid

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Question(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField(max_length=500)
    allow_answers = models.BooleanField()
    ends_on = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question text: {self.text}"


class Choice(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.ManyToManyField(User, related_name="choice_for_question")

    def __str__(self):
        return f"Choice text: {self.text}"
