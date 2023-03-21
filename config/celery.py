import os
import environ
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
  'postcreator-task-crontab': {
    'task': 'project.tasks.post_creator',
    'schedule': crontab(hour=15, minute=20, day_of_week='*'),
    'args': (),
  },
  'alert-sender-task-crontab': {
    'task': 'alerts.tasks.alert_sender',
    'schedule': crontab(hour='*', minute='*', day_of_week='*'),
    'args': (),
  },
  'calculate-summary-vector': {
    'task': 'ml_components.tasks.calculate_summary_vector',
    'schedule': crontab(hour=15, minute=20, day_of_week='*'),
    'args': (),
  },
}
