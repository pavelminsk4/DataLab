from django.db import models
from django.contrib.auth.models import User
#from widgets.models import *
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.db.models.signals import post_save
from django.dispatch import receiver

class Templates(models.Model):
  title = models.CharField(max_length=50)
  layout_file = models.FileField(upload_to='static/report_templates')

  def __str__(self):
    return self.title

class RegularReport(models.Model):
  title = models.CharField(max_length=50)
  user = models.ManyToManyField(User, blank=True, null=True)
  email_title = models.TextField(max_length=500)
  #widget_for_report = models.ManyToManyField()
  template = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True)
  ending_date = models.DateTimeField()
  type = models.CharField(max_length=10)
  periodic_task = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True)
  crontab_schedule = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True)

@receiver(post_save, sender=RegularReport)
def create_periodic_task(sender, instance, created, **kwargs):
  if created:
    periodic_task=PeriodicTask.objects.create()
    instance.periodic_task = periodic_task.id

@receiver(post_save, sender=RegularReport)
def create_crontab_schedule(sender, instance, created, **kwargs):
  if created:
    crontab_schedule=CrontabSchedule.objects.create()
    instance.crontab_schedule = crontab_schedule.id
