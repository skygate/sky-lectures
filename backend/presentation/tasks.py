from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from presentation.models import Notification, Presentation, Comment
from sky_lectures.celery import app


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
def create_notification_for_presentation(users: list[int], presentation_id: int):
    users = User.objects.filter(id__in=users)
    presentation = Presentation.objects.get(id=presentation_id)
    message = f"New presentation - {presentation.title} - with your favourite tags has been added!"
    Notification.objects.bulk_create(
        Notification(
            message=message,
            user=user,
        )
        for user in users
    )


@app.task
def create_notification_for_comment(users: list[int], comment_id: int):
    users = User.objects.filter(id__in=users)
    comment = Comment.objects.get(id=comment_id)
    message = f"{comment.user} replies to your comment! Check this out!"
    Notification.objects.bulk_create(
        Notification(
            message=message,
            user=user,
        )
        for user in users
    )
