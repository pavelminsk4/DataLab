from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex
from reports.models import Templates
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

class WorkspaceSocial(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=1000, null=True, blank=True)
  members = models.ManyToManyField(User, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  department = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True, related_name='social_workspaces')

  def __str__(self):
    return self.title

class ProjectSocial(models.Model):
  title = models.CharField(max_length=100)
  creator = models.ForeignKey(User,related_name='creator_social', on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  note = models.CharField(max_length=200, null=True, blank=True)
  keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  ignore_keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  additional_keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  workspace = models.ForeignKey(WorkspaceSocial, related_name='worksplace_social', blank=True, null=True, on_delete=models.CASCADE)
  start_search_date = models.DateTimeField()
  end_search_date = models.DateTimeField()
  author_filter = models.CharField(max_length=50, blank=True, null=True)
  language_filter = models.CharField(max_length=50, blank=True, null=True)
  country_filter = models.CharField(max_length=50, blank=True, null=True)
  source_filter = models.CharField(max_length=50, blank=True, null=True)
  sentiment_filter = models.CharField(max_length=10, blank=True, null=True)
  members = models.ManyToManyField(User, related_name='projects_social', blank=True, null=True)
  author_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
  language_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
  country_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
  source_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
  sentiment_dimensions = ArrayField(models.CharField(max_length=10), blank=True, null=True)
    
  def save(self, *args, **kwargs):
    total_projects_count = 0
    if self.workspace:
        for workspace in self.workspace.department.workspaces.all():
            total_projects_count += workspace.projects.all().count()
        if total_projects_count < self.workspace.department.max_projects_social:
            return super(ProjectSocial, self).save(*args, **kwargs)
        raise ValidationError('Projects creation limit reached')
    super(ProjectSocial, self).save(*args, **kwargs)

  def __str__(self):
    return self.title

@receiver(post_save, sender=ProjectSocial)
def increase_cur_number_of_projects(sender, instance, created, **kwargs):
  if created:
    if instance.workspace:
      instance.workspace.department.current_number_of_social_projects += 1
      instance.workspace.department.save()

@receiver(post_save, sender=WorkspaceSocial)
def increase_cur_number_of_projects_2(sender, instance, created, **kwargs):
  if created:
    instance.department.current_number_of_social_projects += 1
    instance.department.save()

@receiver(pre_delete, sender=ProjectSocial)
def decrease_cur_number_of_projects(sender, instance, using, **kwargs):
  instance.workspace.department.current_number_of_social_projects -= 1
  instance.workspace.department.save()
