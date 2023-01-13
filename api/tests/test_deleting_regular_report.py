from rest_framework.test import APITestCase
from rest_framework import status
from reports.models import RegularReport, CrontabSchedule, PeriodicTask
from project.models import Project
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

class DeleteRegularReportTests(APITestCase):
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
    rr2 = RegularReport.objects.create(title='Second Report', project=pr2, hourly_enabled=True, daily_enabled=True, weekly_enabled=True, monthly_enabled=True)
    rr3 = RegularReport.objects.create(title='Third Report', project=pr2)
    url = reverse('regular_reports-list', kwargs={'proj_pk':pr2.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.client.force_authenticate(user=user)
    url = f'/api/regularreports/{rr2.id}/'
    RegularReport.objects.get(pk=rr2.id).delete()
    self.assertTrue(RegularReport.objects.filter(pk=rr3.id))
    self.assertFalse(RegularReport.objects.filter(pk=rr2.id))
    self.assertFalse(CrontabSchedule.objects.filter(pk=rr2.hourly_crontab_schedule_id))
    self.assertFalse(CrontabSchedule.objects.filter(pk=rr2.daily_crontab_schedule_id))
    self.assertFalse(CrontabSchedule.objects.filter(pk=rr2.weekly_crontab_schedule_id))
    self.assertFalse(CrontabSchedule.objects.filter(pk=rr2.monthly_periodic_task_id))
    self.assertFalse(PeriodicTask.objects.filter(pk=rr2.hourly_periodic_task_id))
    self.assertFalse(PeriodicTask.objects.filter(pk=rr2.daily_periodic_task_id))
    self.assertFalse(PeriodicTask.objects.filter(pk=rr2.weekly_periodic_task_id))
    self.assertFalse(PeriodicTask.objects.filter(pk=rr2.monthly_periodic_task_id))
