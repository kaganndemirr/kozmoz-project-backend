# Future
from __future__ import absolute_import, unicode_literals

# Standart Library
import os

# Third-Party
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kozmoz.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('kozmoz')


# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
