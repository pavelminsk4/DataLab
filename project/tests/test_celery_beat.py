from django.test import TestCase
from config.celery import app


class CeleryBeatTestCase(TestCase):
    def test_celery_beat_has_tasks(self):
        """Celery has a specific set of periodic tasks"""
        tasks = list(app.conf.beat_schedule.keys())

        self.assertEqual(len(tasks), 9)
        self.assertListEqual(tasks, [
            'postcreator-task-crontab',
            'alert-sender-task-crontab',
            'calculate-summary-vector',
            'calculate-imp-sentiment',
            'update-live-reports',
            'get-new-tweets-by-basic-searches',
            'reset-talkwalker-collectors',
            'run-talkwalker-livesearch',
            'run-rss-livesearch'
        ])
