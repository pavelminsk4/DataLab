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
  template = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True, blank=True)
  h_minute = models.CharField(max_length=4, default='*')
  h_hour = models.CharField(max_length=4, default='*')
  h_day_of_week = models.CharField(max_length=4, default='*')
  h_day_of_month = models.CharField(max_length=4, default='*')
  h_ending_date = models.DateTimeField(null=True, blank=True)
  hourly_periodic_task = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_h_periodic_task')
  hourly_crontab_schedule = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_h_crontab_sch')
  hourly_enabled = models.BooleanField(default=False)
  d_minute = models.CharField(max_length=4, default='*')
  d_hour = models.CharField(max_length=4, default='*')
  d_day_of_week = models.CharField(max_length=4, default='*')
  d_day_of_month = models.CharField(max_length=4, default='*')
  d_ending_date = models.DateTimeField(null=True, blank=True)
  daily_periodic_task = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_d_periodic_task')
  daily_crontab_schedule = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_d_crontab_sch')
  daily_enabled = models.BooleanField(default=False)

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
        args = [ instance.id ],
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
        args = [ instance.id ],
      )
      instance.daily_periodic_task = periodic_task
    instance.save()
