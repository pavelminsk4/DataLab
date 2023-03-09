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
  workspace = models.ForeignKey(WorkspaceSocial, related_name='social_workspace_projects', blank=True, null=True, on_delete=models.CASCADE)
  start_search_date = models.DateTimeField()
  end_search_date = models.DateTimeField()
  author_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  language_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  country_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  source_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  sentiment_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
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

class SocialWidgetDescription(models.Model):
  is_active = models.BooleanField(default=False)
  title = models.CharField(default='Title', max_length=50)
  default_title = models.CharField(default='Default Title', max_length=50)
  description = models.TextField(default='', null=True, blank=True)
  aggregation_period = models.CharField(default='day', max_length=10)
  author_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  country_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  source_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  language_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  sentiment_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  chart_type = models.CharField(max_length=150, default=None, null=True, blank=True)

class SocialWidgetsList(models.Model):
  project = models.OneToOneField(ProjectSocial, on_delete=models.CASCADE, related_name='social_widgets_list', editable=False)
  summary_widget = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_summary_widget', null=True)
  clipping_feed_content = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_clipping_feed_content', null=True)
  top_countries = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_top_countries', null=True)
  top_authors = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_top_authors', null=True)
  top_languages = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_top_languages', null=True)
  content_volume = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_content_volume', null=True)
  content_volume_by_top_countries = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_content_volume_by_top_countries', null=True)
  content_volume_by_top_authors = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_content_volume_by_top_authors', null=True)
  content_volume_by_top_languages = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_content_volume_by_top_languages', null=True)
  sentiment = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_sentiment', null=True)
  gender_volume = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_genter_volume', null=True)
  sentiment_number_of_results = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_sentiment_number_of_results', null=True)
  sentiment_authors = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_sentiment_authors', null=True)
  sentiment_countries = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_sentiment_countries', null=True)
  sentiment_languages = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_sentiment_languages', null=True)
  sentiment_by_gender = models.ForeignKey(SocialWidgetDescription,on_delete=models.CASCADE,related_name='social_sentiment_by_gender', null=True)
  
  def __str__(self):
    return str(self.project)

@receiver(post_save, sender=ProjectSocial)
def create_widgets_list(sender, instance, created, **kwargs):
  if created:
    SocialWidgetsList.objects.create(project=instance)

@receiver(post_save, sender=SocialWidgetsList)
def create_social_widget_description(sender, instance, created, **kwargs):
  if created:
    wd1 = SocialWidgetDescription.objects.create(title='Summary', default_title='Summary')
    wd1.save()
    wd2 = SocialWidgetDescription.objects.create(title='Clipping feed content', default_title='Clipping feed content')
    wd2.save()
    wd3 = SocialWidgetDescription.objects.create(title='Top countries', default_title='Top countries')
    wd3.save()
    wd4 = SocialWidgetDescription.objects.create(title='Top authors', default_title='Top authors')
    wd4.save()
    wd5 = SocialWidgetDescription.objects.create(title='Top languages', default_title='Top languages')
    wd5.save()
    wd6 = SocialWidgetDescription.objects.create(title='Content volume', default_title='Content volume')
    wd6.save()
    wd7 = SocialWidgetDescription.objects.create(title='Content volume by top countries', default_title='Content volume by top countries')
    wd7.save()
    wd8 = SocialWidgetDescription.objects.create(title='Content volume by top authors', default_title='Content volume by top authors')
    wd8.save()
    wd9 = SocialWidgetDescription.objects.create(title='Content volume by top languages', default_title='Content volume by top languages')
    wd9.save()
    wd10 = SocialWidgetDescription.objects.create(title='Social sentiment', default_title='Social sentiment')
    wd10.save()
    wd11 = SocialWidgetDescription.objects.create(title='Social gender volume', default_title='Social gender volume')
    wd11.save()
    wd12 = SocialWidgetDescription.objects.create(title='Social sentiment number of results', default_title='Social sentiment number of results')
    wd12.save()
    wd13 = SocialWidgetDescription.objects.create(title='Social sentiment authors', default_title='Social sentiment authors')
    wd13.save()
    wd14 = SocialWidgetDescription.objects.create(title='Social sentiment countries', default_title='Social sentiment countries')
    wd14.save()
    wd15 = SocialWidgetDescription.objects.create(title='Social sentiment languages', default_title='Social sentiment languages')
    wd15.save()
    wd16 = SocialWidgetDescription.objects.create(title='Social sentiment by gender', default_title='Social sentiment by gender')
    wd16.save()
    instance.summary_widget = wd1
    instance.clipping_feed_content = wd2
    instance.top_countries = wd3
    instance.top_authors = wd4
    instance.top_languages = wd5
    instance.content_volume = wd6
    instance.content_volume_by_top_countries = wd7
    instance.content_volume_by_top_authors = wd8
    instance.content_volume_by_top_languages = wd9
    instance.sentiment = wd10
    instance.gender_volume = wd11
    instance.sentiment_number_of_results = wd12
    instance.sentiment_authors = wd13
    instance.sentiment_countries = wd14
    instance.sentiment_languages = wd15
    instance.sentiment_by_gender = wd16
    instance.save()
