from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from presentation.models import Notification, Presentation, Comment
from sky_lectures.celery import app

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
User = get_user_model()


@app.task
def send_email_task(subject: str, message: str, email: list[str]) -> None:
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=email,
        fail_silently=False,
    )


@app.task
def create_notifications(users: list[int], instance_id: int, notification_type: str):
    users = User.objects.filter(id__in=users)
    if notification_type == "Presentation":
        instance = Presentation.objects.get(id=instance_id)
        message = f"New presentation - {instance.title} - with your favourite tags has been added!"
    elif notification_type == "Comment":
        instance = Comment.objects.get(id=instance_id)
        message = f"{instance.user} replies to your comment! Check this out!"
    Notification.objects.bulk_create(
        Notification(
            message=message,
            user=user,
        )
        for user in users
        if user != instance.user
    )
