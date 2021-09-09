from sky_lectures.celery import app as celery_app


default_app_config = 'users.apps.UserConfig'

__all__ = ["celery_app"]
