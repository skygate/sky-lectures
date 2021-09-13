from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from presentation.models import Presentation, Notification, Comment
from presentation.tasks import (
    send_email_task,
    create_notification_for_presentation,
    create_notification_for_comment,
)


User = get_user_model()


@receiver(post_save, sender=Presentation)
def create_notification_about_new_presentation_with_favourite_tag(
    sender, instance, created, **kwargs
):
    if not instance.notification_sended:
        presentation_tags = instance.tags.values_list("name", flat=True)
        if presentation_tags:
            users_with_specific_favourite_tags = (
                User.objects.distinct()
                .filter(favourite_tags__name__in=set(presentation_tags))
                .exclude(username=instance.user)
            )
            create_notification_for_presentation.delay(
                users=list(users_with_specific_favourite_tags.values_list("id", flat=True)),
                presentation_id=instance.id,
            )
            instance.notification_sended = True
            instance.save()


@receiver(post_save, sender=Comment)
def create_notification_about_reply_to_comment(sender, instance, created, **kwargs):
    if created:
        comment_parent = instance.reply_to
        if comment_parent:
            create_notification_for_comment.delay(
                users=[comment_parent.user.id],
                comment_id=instance.id,
            )


@receiver(post_save, sender=Notification)
def send_email_with_new_notification(sender, instance, created, **kwargs):
    if created:
        send_email_task.delay(
            subject="Notification!",
            message=instance.message,
            email=[instance.user.email],
        )
