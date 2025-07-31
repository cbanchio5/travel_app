# yourproject/celery.py

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')

app = Celery('yourproject')

# Read celery config from Django settings, e.g. CELERY_BROKER_URL
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks from all installed apps
app.autodiscover_tasks()
