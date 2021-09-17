import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sky_lectures.settings.dev")

app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
