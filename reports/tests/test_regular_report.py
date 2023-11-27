from rest_framework.test import APITestCase
from common.factories.user import UserFactory
from common.factories.department import DepartmentFactory
from reports.models import RegularReport
from rest_framework import status
import json


def exclude(data, keys):
    return list(map(lambda record: {k: v for k, v in record.items() if k not in keys}, data))


class RegularReportsTests(APITestCase):
    maxDiff = None

    def test_regular_reports_get_list_api(self):
        """Regular Reports list can be returned via API"""
        dep1 = DepartmentFactory(departmentname='First Dep')
        dep2 = DepartmentFactory(departmentname='Second Dep')

        user = UserFactory()
        user.user_profile.department = dep1
        user.user_profile.save()

        report = RegularReport.objects.create(title='First Report', creator=user, department=dep1)
        RegularReport.objects.create(title='Second Report', creator=user, department=dep2)
        RegularReport.objects.create(title='Third Report', creator=user, department=dep2)

        expected = [
            {
                'id': report.id,
                'title': 'First Report',
                'department': dep1.id,
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
                'items': [],
                'report_template': None,
                'report_format': 'pdf',
                'report_language': 'English'
            }
        ]

        self.client.force_login(user)
        response = self.client.get(f'/api/reports/regular_reports/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(exclude(json.loads(response.content), ['creator', 'created_at', 'updated_at']), expected)
