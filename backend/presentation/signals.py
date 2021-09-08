from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from presentation.models import Presentation, Notification, Comment
from users.models import Profile


@receiver(post_save, sender=Presentation)
def create_notification_about_new_presentation_with_favourite_tag(
    sender, instance, created, **kwargs
):
    presentation_tags = instance.tags.all().values_list("name", flat=True)
    if presentation_tags:
        profiles_with_specific_favourite_tags = Profile.objects.distinct().filter(
            favourite_tags__name__in=set(presentation_tags)
        )
        notification = Notification.objects.create(
            message=f"New presentation - {instance.title} - with your favourite tags has been added!",
        )
        notification.profiles.add(*profiles_with_specific_favourite_tags)
        notification.save()


@receiver(post_save, sender=Comment)
def create_notification_about_reply_to_comment(sender, instance, **kwargs):
    comment_parent = instance.reply_to
    if comment_parent:
        notification = Notification.objects.create(
            message=f"{instance.user} replies to your comment! Check this out!"
        )
        notification.profiles.add(comment_parent.user.profile)
        notification.save()


@receiver(post_save, sender=Notification)
def send_email_with_new_notification(sender, instance, created, **kwargs):
    if not created:
        subject = "Notification!"
        message = instance.message
        users_email = [profile.user.email for profile in instance.profiles.all()]
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=users_email,
            fail_silently=False,
        )
