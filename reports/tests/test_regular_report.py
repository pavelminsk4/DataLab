from rest_framework.test import APITestCase
from rest_framework import status
from reports.models import RegularReport
from project.models import Project
from django.urls import reverse
import json
from pprint import pprint
from datetime import datetime
from django.contrib.auth.models import User


class DimensionsTests(APITestCase):
  def test_regular_reposrts_api(self):
    user = User.objects.create(username='Fox')
    pr1 = Project.objects.create(
        title='Project1',
        keywords=['Keyword'],
        start_search_date=datetime(2022, 10, 10),
        end_search_date=datetime(2022, 10, 16),
        creator=user
        )
    pr2 = Project.objects.create(
        title='Project2',
        keywords=['Keyword'],
        start_search_date=datetime(2022, 10, 10),
        end_search_date=datetime(2022, 10, 16),
        creator=user
        )
    rr1 = RegularReport.objects.create(title='First Report', project=pr1)
    rr2 = RegularReport.objects.create(title='Second Report', project=pr2)
    rr3 = RegularReport.objects.create(title='Third Report', project=pr2)
 
    url = reverse('regular_reports-list', kwargs={'pk':pr2.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {
              'crontab_schedule': rr2.crontab_schedule.id,
              'day_of_month': '*',
              'day_of_week': '*',
              'email_title': None,
              'ending_date': None,
              'hour': '*',
              'id': rr2.id,
              'minute': '*',
              'periodic_task': rr2.periodic_task.id,
              'project': pr2.id,
              'template': None,
              'title': 'Second Report',
              'user': [],
            },
            {
              'crontab_schedule': rr3.crontab_schedule.id,
              'day_of_month': '*',
              'day_of_week': '*',
              'email_title': None,
              'ending_date': None,
              'hour': '*',
              'id': rr3.id,
              'minute': '*',
              'periodic_task': rr3.periodic_task.id,
              'project': pr2.id,
              'template': None,
              'title': 'Third Report',
              'user': [],
            },
          ]
    self.assertEqual(json.loads(response.content), res)
