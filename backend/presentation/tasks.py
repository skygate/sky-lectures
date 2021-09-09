from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

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
