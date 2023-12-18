from django.db.models.signals import post_save, pre_delete
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models

from tweet_binder.models import TweetBinderPost
from expert_filters.models import Preset
from reports.models import Templates


class WorkspaceSocial(models.Model):
    title       = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    members     = models.ManyToManyField(User, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    department  = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True, related_name='social_workspaces')

    def __str__(self):
        return self.title


class ProjectSocial(models.Model):
    title                = models.CharField(max_length=100)
    note                 = models.CharField(max_length=200, null=True, blank=True)
    source               = models.CharField(max_length=100, null=True, blank=True, default='Social')
    report_format        = models.CharField(max_length=3, default='pdf', blank=True)
    query_filter         = models.CharField(max_length=5000, blank=True, null=True)
    expert_mode          = models.BooleanField(default=False)
    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)
    start_search_date    = models.DateTimeField()
    end_search_date      = models.DateTimeField()
    keywords             = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    ignore_keywords      = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    additional_keywords  = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    author_filter        = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    language_filter      = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    country_filter       = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    source_filter        = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    sentiment_filter     = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    author_dimensions    = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    language_dimensions  = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    country_dimensions   = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    source_dimensions    = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    sentiment_dimensions = ArrayField(models.CharField(max_length=10), blank=True, null=True)

    creator              = models.ForeignKey(User, related_name='creator_social', on_delete=models.SET_NULL, null=True)
    report_template      = models.ForeignKey(Templates, related_name='project_social_templates', on_delete=models.SET_NULL, null=True, blank=True)
    workspace            = models.ForeignKey(WorkspaceSocial, related_name='social_workspace_projects', blank=True, null=True, on_delete=models.CASCADE)
    expert_presets       = models.ManyToManyField(Preset, blank=True)
    members              = models.ManyToManyField(User, related_name='projects_social', blank=True)

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
def increase_workspace_projects_count(sender, instance, created, **kwargs):
    if created:
        if instance.workspace:
            instance.workspace.department.current_number_of_social_projects += 1
            instance.workspace.department.save()


@receiver(post_save, sender=WorkspaceSocial)
def increase_department_projects_count(sender, instance, created, **kwargs):
    if created:
        instance.department.current_number_of_social_projects += 1
        instance.department.save()


@receiver(pre_delete, sender=ProjectSocial)
def decrease_workspace_projects_count(sender, instance, using, **kwargs):
    instance.workspace.department.current_number_of_social_projects -= 1
    instance.workspace.department.save()


class SocialWidgetDescription(models.Model):
    title                = models.CharField(default='Title', max_length=50)
    default_title        = models.CharField(default='Default Title', max_length=50)
    aggregation_period   = models.CharField(default='day', max_length=10)
    chart_type           = models.CharField(max_length=150, default=None, null=True, blank=True)
    description          = models.TextField(default='', null=True, blank=True)
    is_active            = models.BooleanField(default=False)
    top_counts           = models.IntegerField(default=5)
    author_dimensions    = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    country_dimensions   = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    source_dimensions    = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    language_dimensions  = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    sentiment_dimensions = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)


class SocialWidgetsList(models.Model):
    project                      = models.OneToOneField(ProjectSocial, on_delete=models.CASCADE, related_name='social_widgets_list', editable=False)
    summary                      = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_summary', null=True)
    clipping_feed_content        = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_clipping_feed_content', null=True)
    top_locations                = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_top_locations', null=True)
    top_authors                  = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_top_authors', null=True)
    top_languages                = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_top_languages', null=True)
    content_volume               = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_content_volume', null=True)
    content_volume_top_locations = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_content_volume_top_locations', null=True)
    content_volume_top_authors   = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_content_volume_top_authors', null=True)
    content_volume_top_languages = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_content_volume_top_languages', null=True)
    sentiment                    = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_sentiment', null=True)
    gender_volume                = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_genter_volume', null=True)
    sentiment_number_of_results  = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_sentiment_number_of_results', null=True)
    sentiment_authors            = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_sentiment_authors', null=True)
    sentiment_locations          = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_sentiment_locations', null=True)
    sentiment_languages          = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_sentiment_languages', null=True)
    sentiment_by_gender          = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_sentiment_by_gender', null=True)
    top_keywords                 = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_top_keywords', null=True)
    sentiment_top_keywords       = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_sentiment_top_keywords', null=True)
    sentiment_diagram            = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_sentiment_diagram', null=True)
    top_sharing_sources          = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_top_sharing_sources', null=True)
    overall_top_authors          = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_overall_top_authors', null=True)
    top_authors_by_gender        = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_top_authors_by_gender', null=True)
    authors_by_language          = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_authors_by_language', null=True)
    authors_by_location          = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_authors_by_location', null=True)
    authors_by_sentiment         = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_authors_by_sentiment', null=True)
    authors_by_gender            = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='social_authors_by_gender', null=True)
    keywords_by_location         = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='keywords_by_location', null=True)
    languages_by_location        = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='languages_by_location', null=True)
    gender_by_location           = models.ForeignKey(SocialWidgetDescription, on_delete=models.CASCADE, related_name='gender_by_location', null=True)

    def __str__(self):
        return str(self.project)


@receiver(post_save, sender=ProjectSocial)
def create_widgets_list(sender, instance, created, **kwargs):
    if created:
        SocialWidgetsList.objects.create(project=instance)


@receiver(post_save, sender=SocialWidgetsList)
def create_social_widget_description(sender, instance, created, **kwargs):
    if created:
        instance.summary                      = SocialWidgetDescription.objects.create(title='Summary', default_title='Summary')
        instance.clipping_feed_content        = SocialWidgetDescription.objects.create(title='Clipping feed content', default_title='Clipping feed content')
        instance.top_locations                = SocialWidgetDescription.objects.create(title='Top locations', default_title='Top locations')
        instance.top_authors                  = SocialWidgetDescription.objects.create(title='Top authors', default_title='Top authors')
        instance.top_languages                = SocialWidgetDescription.objects.create(title='Top languages', default_title='Top languages')
        instance.content_volume               = SocialWidgetDescription.objects.create(title='Content volume', default_title='Content volume')
        instance.content_volume_top_locations = SocialWidgetDescription.objects.create(title='Content volume by top locations', default_title='Content volume by top locations')
        instance.content_volume_top_authors   = SocialWidgetDescription.objects.create(title='Content volume by top authors', default_title='Content volume by top authors')
        instance.content_volume_top_languages = SocialWidgetDescription.objects.create(title='Content volume by top languages', default_title='Content volume by top languages')
        instance.sentiment                    = SocialWidgetDescription.objects.create(title='Sentiment', default_title='Sentiment')
        instance.gender_volume                = SocialWidgetDescription.objects.create(title='Gender volume', default_title='Gender volume')
        instance.sentiment_number_of_results  = SocialWidgetDescription.objects.create(title='Sentiment number of results', default_title='Sentiment number of results')
        instance.sentiment_authors            = SocialWidgetDescription.objects.create(title='Sentiment authors', default_title='Sentiment authors')
        instance.sentiment_locations          = SocialWidgetDescription.objects.create(title='Sentiment locations', default_title='Sentiment locations')
        instance.sentiment_languages          = SocialWidgetDescription.objects.create(title='Sentiment languages', default_title='Sentiment languages')
        instance.sentiment_by_gender          = SocialWidgetDescription.objects.create(title='Sentiment by gender', default_title='Sentiment by gender')
        instance.top_keywords                 = SocialWidgetDescription.objects.create(title='Top keywords', default_title='Top keywords')
        instance.sentiment_top_keywords       = SocialWidgetDescription.objects.create(title='Sentiment top keywords', default_title='Sentiment top keywords')
        instance.sentiment_diagram            = SocialWidgetDescription.objects.create(title='Sentiment diagram', default_title='Sentiment diagram')
        instance.top_sharing_sources          = SocialWidgetDescription.objects.create(title='Top sharing sources', default_title='Top sharing sources')
        instance.overall_top_authors          = SocialWidgetDescription.objects.create(title='Overall top authors', default_title='Overall top authors')
        instance.top_authors_by_gender        = SocialWidgetDescription.objects.create(title='Top authors by gender', default_title='Top authors by gender')
        instance.authors_by_language          = SocialWidgetDescription.objects.create(title='Authors by language', default_title='Authors by language')
        instance.authors_by_location          = SocialWidgetDescription.objects.create(title='Authors by location', default_title='Authors by location')
        instance.authors_by_sentiment         = SocialWidgetDescription.objects.create(title='Authors by sentiment', default_title='Authors by sentiment')
        instance.authors_by_gender            = SocialWidgetDescription.objects.create(title='Authors by gender', default_title='Authors by gender')
        instance.keywords_by_location         = SocialWidgetDescription.objects.create(title='Top keywords by location', default_title='Top keywords by location')
        instance.languages_by_location        = SocialWidgetDescription.objects.create(title='Top languages by location', default_title='Top languages by location')
        instance.gender_by_location           = SocialWidgetDescription.objects.create(title='Top gender by location', default_title='Top gender by location')
        instance.save()


class SocialClippingWidget(models.Model):
    project = models.ForeignKey(ProjectSocial, on_delete=models.CASCADE)
    post    = models.ForeignKey(TweetBinderPost, on_delete=models.CASCADE, related_name='social_posts')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project_id', 'post_id'], name='social clipping widget uniqueness constraint')
        ]


class ChangingTweetbinderSentiment(models.Model):
    sentiment  = models.CharField('sentiment', max_length=10)
    department = models.ForeignKey('accounts.department', on_delete=models.CASCADE)
    post = models.ForeignKey(TweetBinderPost, on_delete=models.CASCADE)

    def ___str__(self):
        return self.sentiment
