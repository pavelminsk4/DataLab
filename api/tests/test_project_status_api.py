from django_celery_beat.models import PeriodicTask, CrontabSchedule
from common.factories.project import ProjectFactory
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from project.models import Project
from django.urls import reverse
import json


class ProjectSatusTests(APITestCase):
    def test_changing_project_status(self):
        user = User.objects.create(username='MiskKSA')
        self.client.force_login(user)

        pr = ProjectFactory(
            title='Project1',
            keywords=['Keyword'],
            start_search_date='2022-10-10T00:00:00Z',
            end_search_date='2022-10-16T00:00:00Z',
            creator=user
        )

        schedule = CrontabSchedule.objects.create(
            minute='*/20',
            hour='*',
            day_of_week='*',
            day_of_month='*',
        )

        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'LiveSearch_project_{pr.id}',
            task='talkwalker.tasks.livesearch_sender',
            args=json.dumps([pr.id, 'Project']),
        )

        self.assertEqual(pr.status, 'collecting_data')

        data = {'status': 'inactive'}
        url = reverse('project_statuses-detail', kwargs={'pk':pr.pk})
        response = self.client.patch(url, data)
        pr = Project.objects.get(pk=pr.pk)
        pt = PeriodicTask.objects.get(name=f'LiveSearch_project_{pr.id}')

        self.assertEqual(pt.enabled, False)
        self.assertEqual(pr.status, 'inactive')
