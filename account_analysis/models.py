from django.db.models.signals import post_save, pre_delete
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models

class WorkspaceAccountAnalysis(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=1000, null=True, blank=True)
  members = models.ManyToManyField(User, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  department = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True, related_name='account_analysis_workspaces')

  def __str__(self):
    return self.title
  
class ProjectAccountAnalysis(models.Model):
  title = models.CharField(max_length=100)
  creator = models.ForeignKey(User,related_name='creator_account_analysis', on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  profile_handle = models.CharField(max_length=100)
  workspace = models.ForeignKey(WorkspaceAccountAnalysis, related_name='account_analysis_workspace_projects', blank=True, null=True, on_delete=models.CASCADE)
  start_search_date = models.DateTimeField()
  end_search_date = models.DateTimeField()
  min_followers = models.IntegerField(default=0)
  max_followers = models.IntegerField(default=1000000000)
  language_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  country_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  sentiment_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  source_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  author_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  language_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  country_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  sentiment_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  source_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  author_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  members = models.ManyToManyField(User, related_name='projects_account_analysis', blank=True, null=True)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    total_projects_count = 0
    if self.workspace:
        for workspace in self.workspace.department.workspaces.all():
            total_projects_count += workspace.projects.all().count()
        if total_projects_count < self.workspace.department.max_projects_account_analysis:
            return super(ProjectAccountAnalysis, self).save(*args, **kwargs)
        raise ValidationError('Projects creation limit reached')
    super(ProjectAccountAnalysis, self).save(*args, **kwargs)

@receiver(post_save, sender=ProjectAccountAnalysis)
def increase_cur_number_of_projects(sender, instance, created, **kwargs):
  if created:
    if instance.workspace:
      instance.workspace.department.current_number_of_account_analysis_projects += 1
      instance.workspace.department.save()

@receiver(post_save, sender=WorkspaceAccountAnalysis)
def increase_cur_number_of_projects_2(sender, instance, created, **kwargs):
  if created:
    instance.department.current_number_of_account_analysis_projects += 1
    instance.department.save()

@receiver(pre_delete, sender=ProjectAccountAnalysis)
def decrease_cur_number_of_projects(sender, instance, using, **kwargs):
  instance.workspace.department.current_number_of_account_analysis_projects -= 1
  instance.workspace.department.save()

class AccountAnalysisWidgetDescription(models.Model):
  is_active = models.BooleanField(default=False)
  title = models.CharField(default='Title', max_length=50)
  default_title = models.CharField(default='Default Title', max_length=50)
  description = models.TextField(default='', null=True, blank=True)
  aggregation_period = models.CharField(default='day', max_length=10)
  country_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  language_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  sentiment_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  author_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  chart_type = models.CharField(max_length=150, default=None, null=True, blank=True)
  top_counts = models.IntegerField(default=5)  

  def __str__(self):
    return str(self.title)
  
class AccountAnalysisWidgetsList(models.Model):
  project = models.OneToOneField(ProjectAccountAnalysis, on_delete=models.CASCADE, related_name='account_analysis_widgets_list', editable=False)
  summary = models.ForeignKey(AccountAnalysisWidgetDescription,on_delete=models.CASCADE,related_name='account_analysis_summary', null=True)
  
  def __str__(self):
    return str(self.project)  

@receiver(post_save, sender=ProjectAccountAnalysis)
def create_widgets_list(sender, instance, created, **kwargs):
  if created:
    AccountAnalysisWidgetsList.objects.create(project=instance)

@receiver(post_save, sender=AccountAnalysisWidgetsList)
def create_social_widget_description(sender, instance, created, **kwargs):
  if created:
    wd1 = AccountAnalysisWidgetDescription.objects.create(title='Summary', default_title='Summary')
    wd1.save()
    instance.summary = wd1
    instance.save()
