from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from reports.models import RegularReport
from rest_framework import status
from django.urls import reverse
from accounts.models import *
from unittest import skip
import json


class RegularReportsTests(APITestCase):
  @skip("Don't want to test")
  def test_regular_reports_api(self):
    user = User.objects.create(username='Fox')
    dep1 = department.objects.create(
      departmentname = 'First Dep',
    )
    dep2 = department.objects.create(
      departmentname = 'Second Dep',
    )
    user.user_profile.department = dep1
    rr = RegularReport.objects.create(title='First Report', creator=user, module_type='Project', module_project_id=1, department=dep1)
    RegularReport.objects.create(title='Second Report', creator=user, module_type='SocialProject', module_project_id=2, department=dep2)
    RegularReport.objects.create(title='Third Report', creator=user, module_type='Project', module_project_id=3, department=dep2)
 
    url = reverse('regular_reports-list', kwargs={'dep_pk':dep1.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    user_profile = {
                    'email': '',
                    'first_name': '',
                    'groups': [],
                    'id': user.id,
                    'is_active': True,
                    'is_staff': False,
                    'is_superuser': False,
                    'last_login': None,
                    'last_name': '',
                    'password': '',
                    'user_permissions': [],
                    'user_profile': {
                                      'department': None,
                                      'id': user.user_profile.id,
                                      'jobtitle': None,
                                      'phone': None,
                                      'photo': None,
                                      'role': 'Regular User',
                                      'user': user.id
                                    },
                    'username': 'Fox',
                  }
    
    res = [
            { 
              'id': rr.id,
              'title': 'First Report',
              'module_type': 'Project',
              'module_project_id': 1,
              'department': dep1.id,
              'creator': user_profile,
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
              'project': None,
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
              'user': [],
              'report_template': None,
              'report_format': 'pdf',
              'report_language': 'English',
              'dashboard_is_active': False,
              'summary_is_active': False,
              'sentiment_is_active': False,
              'demography_is_active': False,
              'gender_is_active': False,
              'photo_video_is_active': False,
              'influencers_is_active': False,
              'topic_is_active': False,
              'updated_at': rr.updated_at.replace(tzinfo=None).isoformat() + 'Z',
              'created_at': rr.created_at.replace(tzinfo=None).isoformat() + 'Z',
          },
      ]
    self.assertEqual(json.loads(response.content), res)
