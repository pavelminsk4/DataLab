from django.db.models.signals import post_save, pre_delete
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models


class WorkspaceAccountAnalysis(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True, related_name='account_analysis_workspaces')
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class ProjectAccountAnalysis(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User,related_name='creator_account_analysis', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_handle = models.CharField(max_length=100)
    workspace = models.ForeignKey(WorkspaceAccountAnalysis, related_name='account_analysis_workspace_projects', blank=True, null=True, on_delete=models.CASCADE)
    start_search_date = models.DateTimeField(blank=True, null=True)
    end_search_date = models.DateTimeField(blank=True, null=True)
    min_followers = models.IntegerField(blank=True, default=0, null=True)
    max_followers = models.IntegerField(blank=True, default=1000000000, null=True)
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
    count_posts = models.IntegerField(blank=True, default=0, null=True)
    followers = models.IntegerField(blank=True, default=0, null=True)

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
    summary = models.ForeignKey(AccountAnalysisWidgetDescription, on_delete=models.CASCADE, related_name='account_analysis_summary', null=True)
    profile_timeline = models.ForeignKey(AccountAnalysisWidgetDescription, on_delete=models.CASCADE, related_name='account_analysis_profile_timeline', null=True)
    most_frequent_post_types = models.ForeignKey(AccountAnalysisWidgetDescription, on_delete=models.CASCADE, related_name='account_analysis_most_frequent_post_types', null=True)
    most_engaging_post_types = models.ForeignKey(AccountAnalysisWidgetDescription, on_delete=models.CASCADE, related_name='account_analysis_most_engaging_post_types', null=True)
    most_frequent_media_types = models.ForeignKey(AccountAnalysisWidgetDescription, on_delete=models.CASCADE, related_name='account_analysis_most_frequent_media_types', null=True)
    most_engaging_media_types = models.ForeignKey(AccountAnalysisWidgetDescription, on_delete=models.CASCADE, related_name='account_analysis_most_engaging_media_types', null=True)
    follower_growth = models.ForeignKey(AccountAnalysisWidgetDescription, on_delete=models.CASCADE, related_name='follower_growth', null=True)
    optimal_post_length = models.ForeignKey(AccountAnalysisWidgetDescription, on_delete=models.CASCADE, related_name='optimal_post_length', null=True)
    top_hashtags = models.ForeignKey(AccountAnalysisWidgetDescription, on_delete=models.CASCADE, related_name='top_hashtags', null=True)

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
        wd2 = AccountAnalysisWidgetDescription.objects.create(title='Profile timeline', default_title='Profile timeline')
        wd2.save()
        wd3 = AccountAnalysisWidgetDescription.objects.create(title='Most frequent post types', default_title='Most frequent post types')
        wd3.save()
        wd4 = AccountAnalysisWidgetDescription.objects.create(title='Most engaging post types', default_title='Most engaging post types')
        wd4.save()
        wd5 = AccountAnalysisWidgetDescription.objects.create(title='Most frequent media types', default_title='Most frequent media types')
        wd5.save()
        wd6 = AccountAnalysisWidgetDescription.objects.create(title='Most engaging media types', default_title='Most engaging media types')
        wd6.save()
        wd7 = AccountAnalysisWidgetDescription.objects.create(title='Follower growth', default_title='Follower growth')
        wd7.save()
        wd8 = AccountAnalysisWidgetDescription.objects.create(title='Optimal post length', default_title='Optimal post length')
        wd8.save()
        wd9 = AccountAnalysisWidgetDescription.objects.create(title='Top hashtags', default_title='Top hashtags')
        wd9.save()
        instance.summary = wd1
        instance.profile_timeline = wd2
        instance.most_frequent_post_types = wd3
        instance.most_engaging_post_types = wd4
        instance.most_frequent_media_types = wd5
        instance.most_engaging_media_types = wd6
        instance.follower_growth = wd7
        instance.optimal_post_length = wd8
        instance.top_hashtags = wd9
        instance.save()
