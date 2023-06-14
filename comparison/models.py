from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models


class WorkspaceComparison(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    members = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True, related_name='comparison_workspaces')

    def __str__(self):
        return self.title


class ProjectComparison(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, related_name='creator_cmpr', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=200, null=True, blank=True)
    workspace = models.ForeignKey(WorkspaceComparison, related_name='cmpr_workspace_projects', blank=True, null=True, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects_cmpr', blank=True)

    def __str__(self):
        return self.title


class ComparisonItem(models.Model):
    MODULE_TYPE_CHOICES = [
        ('Project', 'Online'),
        ('ProjectSocial', 'Social'),
    ]
    module_type = models.CharField(max_length=70)
    module_project_id = models.IntegerField(blank=True, null=True)
    project = models.ForeignKey(ProjectComparison, related_name='cmpr_items', on_delete=models.SET_NULL, null=True)


class ComparisonWidgetDescription(models.Model):
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
    project = models.ForeignKey(ProjectComparison, related_name='cmpr_widgets', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title)

@receiver(post_save, sender=ProjectComparison)
def create_comparison_widget_description(sender, instance, created, **kwargs):
    if created:
        instance.cmpr_widgets.create(title='Summary', default_title='Summary')
        instance.cmpr_widgets.create(title='Content volume', default_title='Content volume')
        instance.cmpr_widgets.create(title='Top authors', default_title='Top authors')
        instance.cmpr_widgets.create(title='Sentiment', default_title='Sentiment')
        instance.cmpr_widgets.create(title='Top sources', default_title='Top sources')
        instance.cmpr_widgets.create(title='Top keywords', default_title='Top keywords')
        instance.cmpr_widgets.create(title='Top languages', default_title='Top languages')
        instance.cmpr_widgets.create(title='Top countries', default_title='Top countries')
