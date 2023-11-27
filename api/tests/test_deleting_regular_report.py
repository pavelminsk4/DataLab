from reports.models import RegularReport, CrontabSchedule, PeriodicTask
from common.factories.user import UserFactory
from common.factories.department import DepartmentFactory
from common.factories.project import ProjectFactory
from rest_framework.test import APITestCase
from rest_framework import status


class DeleteRegularReportTests(APITestCase):
    def test_regular_reports_delete_api(self):
        """Regular Report can be deleted via API"""
        department = DepartmentFactory(departmentname='First Dep')
        user = UserFactory()
        user.user_profile.department = department
        user.user_profile.save()

        project1 = ProjectFactory(
            title='Project1',
            keywords=['Keyword'],
            start_search_date="2022-10-10T00:00:00Z",
            end_search_date="2022-10-16T00:00:00Z",
            creator=user
        )

        project2 = ProjectFactory(
            title='Project2',
            keywords=['Keyword'],
            start_search_date="2022-10-10T00:00:00Z",
            end_search_date="2022-10-16T00:00:00Z",
            creator=user
        )

        r1 = RegularReport.objects.create(title='First Report', project=project1, department=department)
        r2 = RegularReport.objects.create(title='Third Report', project=project2, department=department)
        r3 = RegularReport.objects.create(
            title='Second Report',
            project=project2,
            department=department,
            hourly_enabled=True,
            daily_enabled=False,
            weekly_enabled=True,
            monthly_enabled=True
        )

        self.client.force_login(user)
        response = self.client.delete(f'/api/reports/regular_reports/{r3.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertTrue(RegularReport.objects.filter(id=r2.id))
        self.assertFalse(RegularReport.objects.filter(id=r3.id))
        self.assertFalse(CrontabSchedule.objects.filter(id=r3.hourly_crontab_schedule_id))
        self.assertFalse(CrontabSchedule.objects.filter(id=r3.daily_crontab_schedule_id))
        self.assertFalse(CrontabSchedule.objects.filter(id=r3.weekly_crontab_schedule_id))
        self.assertFalse(CrontabSchedule.objects.filter(id=r3.monthly_periodic_task_id))
        self.assertFalse(PeriodicTask.objects.filter(id=r3.hourly_periodic_task_id))
        self.assertFalse(PeriodicTask.objects.filter(id=r3.daily_periodic_task_id))
        self.assertFalse(PeriodicTask.objects.filter(id=r3.weekly_periodic_task_id))
        self.assertFalse(PeriodicTask.objects.filter(id=r3.monthly_periodic_task_id))
