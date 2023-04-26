from django.db import models
from project.models import Project
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from alerts.services.online_posts_agregator import posts_agregator
from alerts.services.social_posts_agregator import social_posts_agregator

class AlertItem(models.Model):
  MODULE_TYPE_CHOICES = [
    ('Project', 'Online'),
    ('ProjectSocial', 'Social'),
  ]
  module_type = models.CharField(max_length=70, choices=MODULE_TYPE_CHOICES)
  module_project_id = models.IntegerField()
  previous_posts_count = models.PositiveBigIntegerField(default=0)

class Alert(models.Model):
  title = models.CharField(max_length=50)
  creator = models.ForeignKey(User, related_name='alert_creator', on_delete=models.SET_NULL, null=True)
  department = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True)
  project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='alerts')
  user = models.ManyToManyField(User, blank=True, null=True)
  triggered_on_every_n_new_posts = models.IntegerField(default=1)
  how_many_posts_to_send = models.IntegerField(default=1)
  alert_condition = models.CharField(max_length=50, blank=True, null=True)
  items = models.ManyToManyField(AlertItem, null=True, related_name='alert')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

@receiver(post_save, sender=AlertItem)
def define_initial_posts_count(sender, instance, created, **kwargs):
  if created:
    if instance.module_type == 'Project':
      initial_posts_count = posts_agregator(instance.module_project_id).count()
    if instance.module_type == 'ProjectSocial':
      initial_posts_count = social_posts_agregator(instance.module_project_id).count()
    instance.previous_posts_count = initial_posts_count
    instance.save()

@receiver(pre_delete, sender=Alert)
def delete_related_items(sender, instance, *args, **kwargs):
  items = instance.items.all()
  for item in items:
    item.delete()
