from django.conf import settings
from django.core.mail import send_mail

from sky_lectures.celery import app


@app.task
def send_email_task(subject: str, message: str, email: list[str]) -> None:
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=email,
        fail_silently=False,
    )
