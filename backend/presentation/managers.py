from django.db import models
from django.db.models.signals import post_save


class NotificationManager(models.Manager):
    def bulk_create(self, objs, **kwargs):
        notifications = super(NotificationManager, self).bulk_create(objs, **kwargs)
        for notification in notifications:
            post_save.send(
                sender=notification.__class__, instance=notification, created=True
            )
