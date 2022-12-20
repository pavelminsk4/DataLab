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
  minute = models.CharField(max_length=2, default='*')
  hour = models.CharField(max_length=2, default='*')
  day_of_week = models.CharField(max_length=2, default='*')
  day_of_month = models.CharField(max_length=2, default='*')
  ending_date = models.DateTimeField(null=True, blank=True)
  periodic_task = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True)
  crontab_schedule = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.title

@receiver(post_save, sender=RegularReport)
def create_periodic_task(sender, instance, created, **kwargs):
  if created:
    crontab_schedule = CrontabSchedule.objects.create(
      minute = instance.minute,
      hour = instance.hour,
      day_of_week = instance.day_of_week,
      day_of_month = instance.day_of_month,
    )
    instance.crontab_schedule = crontab_schedule
    periodic_task = PeriodicTask.objects.create(
      crontab = crontab_schedule,
      name = 'REGULAR_REPORT_' + instance.title + str(datetime.now()),
      task = 'reports.tasks.regular_report_sender',
      args = [ instance.id ],
    )
    instance.periodic_task = periodic_task
    instance.save()
