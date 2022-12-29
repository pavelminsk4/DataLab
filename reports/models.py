from django.db import models
from django.contrib.auth.models import User
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Templates(models.Model):
  title = models.CharField(max_length=50)
  layout_file = models.FileField(upload_to='static/report_templates')

  def __str__(self):
    return self.title

class RegularReport(models.Model):
  title = models.CharField(max_length=50)
  project = models.ForeignKey('project.Project', on_delete=models.SET_NULL, null=True, blank=True)
  user = models.ManyToManyField(User, null=True, blank=True)
  email_title = models.TextField(max_length=500, null=True, blank=True)
  h_template = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_h_template')
  h_minute = models.CharField(max_length=4, default='*')
  h_hour = models.CharField(max_length=4, default='*')
  h_day_of_week = models.CharField(max_length=4, default='*')
  h_day_of_month = models.CharField(max_length=4, default='*')
  h_ending_date = models.DateTimeField(null=True, blank=True)
  hourly_periodic_task = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_h_periodic_task')
  hourly_crontab_schedule = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_h_crontab_sch')
  hourly_enabled = models.BooleanField(default=False)
  d_template = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_d_template')
  d_minute = models.CharField(max_length=4, default='*')
  d_hour = models.CharField(max_length=4, default='*')
  d_day_of_week = models.CharField(max_length=4, default='*')
  d_day_of_month = models.CharField(max_length=4, default='*')
  d_ending_date = models.DateTimeField(null=True, blank=True)
  daily_periodic_task = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_d_periodic_task')
  daily_crontab_schedule = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_d_crontab_sch')
  daily_enabled = models.BooleanField(default=False)
  w_template = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_w_template')
  w_minute = models.CharField(max_length=4, default='*')
  w_hour = models.CharField(max_length=4, default='*')
  w_day_of_week = models.CharField(max_length=4, default='*')
  w_day_of_month = models.CharField(max_length=4, default='*')
  w_ending_date = models.DateTimeField(null=True, blank=True)
  weekly_periodic_task = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_w_periodic_task')
  weekly_crontab_schedule = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_w_crontab_sch')
  weekly_enabled = models.BooleanField(default=False)
  m_template = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_m_template')
  m_minute = models.CharField(max_length=4, default='*')
  m_hour = models.CharField(max_length=4, default='*')
  m_day_of_week = models.CharField(max_length=4, default='*')
  m_day_of_month = models.CharField(max_length=4, default='*')
  m_ending_date = models.DateTimeField(null=True, blank=True)
  monthly_periodic_task = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_m_periodic_task')
  monthly_crontab_schedule = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_m_crontab_sch')
  monthly_enabled = models.BooleanField(default=False)

  def __str__(self):
    return self.title

@receiver(post_save, sender=RegularReport)
def create_periodic_task(sender, instance, created, **kwargs):
  if created:
    if instance.hourly_enabled:
      crontab_schedule = CrontabSchedule.objects.create(
        minute = instance.h_minute,
        hour = instance.h_hour,
        day_of_week = instance.h_day_of_week,
        day_of_month = instance.h_day_of_month,
      )
      instance.hourly_crontab_schedule = crontab_schedule
      periodic_task = PeriodicTask.objects.create(
        crontab = crontab_schedule,
        name = 'REGULAR_REPORT_' + instance.title + str(datetime.now()),
        task = 'reports.tasks.regular_report_sender',
        args = [ instance.id, 'hourly' ],
      )
      instance.hourly_periodic_task = periodic_task
    if instance.daily_enabled:
      crontab_schedule = CrontabSchedule.objects.create(
        minute = instance.d_minute,
        hour = instance.d_hour,
        day_of_week = instance.d_day_of_week,
        day_of_month = instance.d_day_of_month,
      )
      instance.daily_crontab_schedule = crontab_schedule
      periodic_task = PeriodicTask.objects.create(
        crontab = crontab_schedule,
        name = 'REGULAR_REPORT_' + instance.title + str(datetime.now()),
        task = 'reports.tasks.regular_report_sender',
        args = [ instance.id, 'daily' ],
      )
      if instance.weekly_enabled:
        crontab_schedule = CrontabSchedule.objects.create(
          minute = instance.w_minute,
          hour = instance.w_hour,
          day_of_week = instance.w_day_of_week,
          day_of_month = instance.w_day_of_month,
        )
        instance.weekly_crontab_schedule = crontab_schedule
        periodic_task = PeriodicTask.objects.create(
          crontab = crontab_schedule,
          name = 'REGULAR_REPORT_' + instance.title + str(datetime.now()),
          task = 'reports.tasks.regular_report_sender',
          args = [ instance.id, 'weekly' ],
        )
      if instance.monthly_enabled:
        crontab_schedule = CrontabSchedule.objects.create(
          minute = instance.m_minute,
          hour = instance.m_hour,
          day_of_week = instance.m_day_of_week,
          day_of_month = instance.m_day_of_month,
        )
        instance.monthly_crontab_schedule = crontab_schedule
        periodic_task = PeriodicTask.objects.create(
          crontab = crontab_schedule,
          name = 'REGULAR_REPORT_' + instance.title + str(datetime.now()),
          task = 'reports.tasks.regular_report_sender',
          args = [ instance.id, 'monthly' ],
        )
      instance.monthly_periodic_task = periodic_task
    instance.save()
