import os
import environ
from celery import Celery
from celery.schedules import crontab
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_always_eager = len(sys.argv) > 1 and sys.argv[1] == 'test'

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'postcreator-task-crontab': {
        'task': 'project.tasks.post_creator',
        'schedule': crontab(hour=15, minute=20, day_of_week='*'),
        'args': ()
    },
    'alert-sender-task-crontab': {
        'task': 'alerts.tasks.alert_sender',
        'schedule': crontab(hour='*', minute='*', day_of_week='*'),
        'args': ()
    },
    'calculate-summary-vector': {
        'task': 'ml_components.tasks.calculate_summary_vector',
        'schedule': crontab(hour='*/3', minute='0', day_of_week='*'),
        'args': ()
    },
    'calculate-imp-sentiment': {
        'task': 'project.tasks.imp_sentiment',
        'schedule': crontab(hour='*/3', minute='0', day_of_week='*'),
        'args': ()
    },
    'update-live-reports': {
        'task': 'tweet_binder.models.get_new_tweets_from_live_reports',
        'schedule': crontab(hour='*/1', minute='0', day_of_week='*'),
        'args': ()
    },
    'get-new-tweets-by-basic-searches': {
        'task': 'tweet_binder.models.get_new_tweets_by_basic_search',
        'schedule': crontab(hour=3, minute=0, day_of_week='*'),
        'args': ()
    },
    'run-livesearch': {
        'task': 'project.tasks.run_livesearch.run_livesearch',
        'schedule': crontab(hour='*', minute='*/20', day_of_week='*'),
        'args': ()
    }
}
