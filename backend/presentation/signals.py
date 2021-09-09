from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from presentation.models import Presentation, Notification, Comment
from presentation.tasks import send_email_task


User = get_user_model()


@receiver(post_save, sender=Presentation)
def create_notification_about_new_presentation_with_favourite_tag(
    sender, instance, created, **kwargs
):
    presentation_tags = instance.tags.all().values_list("name", flat=True)
    if presentation_tags:
        users_with_specific_favourite_tags = User.objects.distinct().filter(
            favourite_tags__name__in=set(presentation_tags)
        )
        Notification.objects.bulk_create(
            Notification(
                message=f"New presentation - {instance.title} - with your favourite tags has been added!",
                user=user,
            )
            for user in users_with_specific_favourite_tags
            if user != instance.user
        )


@receiver(post_save, sender=Comment)
def create_notification_about_reply_to_comment(sender, instance, **kwargs):
    comment_parent = instance.reply_to
    if comment_parent:
        if comment_parent.user != instance.user:
            Notification.objects.create(
                message=f"{instance.user} replies to your comment! Check this out!",
                user=comment_parent.user,
            )


@receiver(post_save, sender=Notification)
def send_email_with_new_notification(sender, instance, created, **kwargs):
    if created:
        send_email_task.delay(
            subject="Notification!",
            message=instance.message,
            email=[instance.user.email],
        )
