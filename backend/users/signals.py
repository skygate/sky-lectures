import os

from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from users.models import get_file_path, Profile, User


@receiver(post_save, sender=User)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=Profile)
def remove_old_image(sender, instance, **kwargs):
    try:
        current_profile = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    if not current_profile.file == instance.file:
        file_path = get_file_path(instance, instance.file)
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, file_path)):
            os.remove(os.path.join(settings.MEDIA_ROOT, file_path))
