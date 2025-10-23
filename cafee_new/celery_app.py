import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafee_new.settings.prod")

app = Celery("cafee_new")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
