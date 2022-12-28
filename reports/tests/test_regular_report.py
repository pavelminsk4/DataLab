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
 
    url = reverse('regular_reports-list', kwargs={'proj_pk':pr2.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [{  'id': rr2.id, 
              'title': 'Second Report', 
              'email_title': None, 
              'h_minute': '*', 
              'h_hour': '*', 
              'h_day_of_week': '*', 
              'h_day_of_month': '*', 
              'h_ending_date': None, 
              'hourly_enabled': False, 
              'd_minute': '*', 
              'd_hour': '*', 
              'd_day_of_week': '*', 
              'd_day_of_month': '*', 
              'd_ending_date': None, 
              'daily_enabled': False, 
              'w_minute': '*', 'w_hour': '*', 
              'w_day_of_week': '*', 
              'w_day_of_month': '*', 
              'w_ending_date': None, 
              'weekly_enabled': False, 
              'm_minute': '*', 
              'm_hour': '*', 
              'm_day_of_week': '*', 
              'm_day_of_month': '*', 
              'm_ending_date': None, 
              'monthly_enabled': False, 
              'project': pr2.pk, 
              'h_template': None, 
              'hourly_periodic_task': None, 
              'hourly_crontab_schedule': None, 
              'd_template': None, 
              'daily_periodic_task': None, 
              'daily_crontab_schedule': None, 
              'w_template': None, 
              'weekly_periodic_task': None, 
              'weekly_crontab_schedule': None, 
              'm_template': None, 
              'monthly_periodic_task': None, 
              'monthly_crontab_schedule': None, 
              'user': []
           },
           {  'id': rr3.id, 
              'title': 'Third Report', 
              'email_title': None, 
              'h_minute': '*', 
              'h_hour': '*', 
              'h_day_of_week': '*', 
              'h_day_of_month': '*', 
              'h_ending_date': None, 
              'hourly_enabled': False, 
              'd_minute': '*', 
              'd_hour': '*', 
              'd_day_of_week': '*', 
              'd_day_of_month': '*', 
              'd_ending_date': None, 
              'daily_enabled': False, 
              'w_minute': '*', 
              'w_hour': '*', 
              'w_day_of_week': '*', 
              'w_day_of_month': '*', 
              'w_ending_date': None, 
              'weekly_enabled': False, 
              'm_minute': '*', 
              'm_hour': '*', 
              'm_day_of_week': '*', 
              'm_day_of_month': '*', 
              'm_ending_date': None, 
              'monthly_enabled': False, 
              'project': pr2.pk, 
              'h_template': None, 
              'hourly_periodic_task': None, 
              'hourly_crontab_schedule': None, 
              'd_template': None, 
              'daily_periodic_task': None, 
              'daily_crontab_schedule': None, 
              'w_template': None, 
              'weekly_periodic_task': None, 
              'weekly_crontab_schedule': None, 
              'm_template': None, 
              'monthly_periodic_task': None, 
              'monthly_crontab_schedule': None, 
              'user': []
           }
    ]
    self.assertEqual(json.loads(response.content), res)
