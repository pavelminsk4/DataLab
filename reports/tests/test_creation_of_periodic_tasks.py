from django.test import TestCase
from reports.models import RegularReport

class RegularReportTestCase(TestCase):
  def setUp(self):
    RegularReport.objects.create(
          title='Full Regular Report',
          module_type='Project',
          module_project_id=1,
          hourly_enabled=True,
          h_minute=15,
          h_hour=3,
          daily_enabled=True,
          weekly_enabled=True,
          monthly_enabled=True,
        )
    RegularReport.objects.create(
          title='Daily Regular Report',
          module_type='Social',
          module_project_id=2,
          hourly_enabled=False,
          daily_enabled=True,
          d_minute=20,
          d_hour=4,
          d_day_of_week=6,
          weekly_enabled=False,
          monthly_enabled=False,
        )

  def test_creation_crontab_tasks(self):
    rr = RegularReport.objects.get(title='Full Regular Report')

    hourly_periodic_task = rr.hourly_periodic_task
    hourly_crontab_schedule = rr.hourly_crontab_schedule
    daily_periodic_task = rr.daily_periodic_task
    daily_crontab_schedule = rr.daily_crontab_schedule
    weekly_periodic_task = rr.weekly_periodic_task
    weekly_crontab_schedule =rr.weekly_crontab_schedule
    monthly_periodic_task = rr.monthly_periodic_task
    monthly_crontab_schedule = rr.monthly_crontab_schedule

    self.assertEqual(type(hourly_periodic_task).__name__, 'PeriodicTask')
    self.assertEqual(type(hourly_crontab_schedule).__name__, 'CrontabSchedule')
    self.assertEqual(hourly_crontab_schedule.hour, '*/3')
    self.assertEqual(hourly_crontab_schedule.minute, '0')
    self.assertEqual(hourly_crontab_schedule.day_of_week, '*')
    self.assertEqual(hourly_crontab_schedule.day_of_month, '*')
    self.assertEqual(hourly_crontab_schedule.month_of_year, '*')

    self.assertEqual(type(daily_periodic_task).__name__, 'PeriodicTask')
    self.assertEqual(type(daily_crontab_schedule).__name__, 'CrontabSchedule')

    self.assertEqual(type(weekly_periodic_task).__name__, 'PeriodicTask')
    self.assertEqual(type(weekly_crontab_schedule).__name__, 'CrontabSchedule')

    self.assertEqual(type(monthly_periodic_task).__name__, 'PeriodicTask')
    self.assertEqual(type(monthly_crontab_schedule).__name__, 'CrontabSchedule')

  def test_creation_crontab_tasks_with_disable_options(self):
    rr2 = RegularReport.objects.get(title='Daily Regular Report')

    hourly_periodic_task = rr2.hourly_periodic_task
    hourly_crontab_schedule = rr2.hourly_crontab_schedule
    daily_periodic_task = rr2.daily_periodic_task
    daily_crontab_schedule = rr2.daily_crontab_schedule
    weekly_periodic_task = rr2.weekly_periodic_task
    weekly_crontab_schedule =rr2.weekly_crontab_schedule
    monthly_periodic_task = rr2.monthly_periodic_task
    monthly_crontab_schedule = rr2.monthly_crontab_schedule

    self.assertEqual(hourly_periodic_task, None)
    self.assertEqual(hourly_crontab_schedule, None)

    self.assertEqual(type(daily_periodic_task).__name__, 'PeriodicTask')
    self.assertEqual(type(daily_crontab_schedule).__name__, 'CrontabSchedule')
    self.assertEqual(daily_crontab_schedule.minute, '20')
    self.assertEqual(daily_crontab_schedule.hour, '4')
    self.assertEqual(daily_crontab_schedule.day_of_week, '6')

    self.assertEqual(weekly_periodic_task, None)
    self.assertEqual(weekly_crontab_schedule, None)

    self.assertEqual(monthly_periodic_task, None)
    self.assertEqual(monthly_crontab_schedule, None)
