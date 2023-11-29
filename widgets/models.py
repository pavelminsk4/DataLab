from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver
from project.models import Project
from project.models import Post
from django.db import models


class Dimensions(models.Model):
    title       = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)


class WidgetDescription(models.Model):
    is_active           = models.BooleanField(default=False)
    title               = models.CharField(default='Title', max_length=50)
    default_title       = models.CharField(default='Default Title', max_length=50)
    top_counts          = models.IntegerField(default=5)
    description         = models.TextField(default='', null=True, blank=True)
    aggregation_period  = models.CharField(default='day', max_length=10)
    author_dim_pivot    = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    country_dim_pivot   = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    source_dim_pivot    = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    language_dim_pivot  = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    sentiment_dim_pivot = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    chart_type          = models.CharField(max_length=150, default=None, null=True, blank=True)


class WidgetsList(models.Model):
    project                         = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='widget_list', editable=False)
    summary_widget                  = models.BooleanField(default=False)
    volume_widget                   = models.BooleanField(default=False)
    clipping_feed_content_widget    = models.BooleanField(default=False)
    top_10_authors_by_volume_widget = models.BooleanField(default=False)

    def __str__(self):
        return str(self.project)


class WidgetsList2(models.Model):
    project                      = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='widgets_list_2', editable=False)
    summary                      = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_summary', null=True)
    volume                       = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_volume', null=True)
    clipping_feed_content        = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_clipping_feed_content', null=True)
    top_authors                  = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_top_authors', null=True)
    top_sources                  = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_top_sources', null=True)
    top_countries                = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_top_countries', null=True)
    top_languages                = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_top_languages', null=True)
    content_volume_top_sources   = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_content_volume_top_sources', null=True)
    sentiment_top_sources        = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sentiment_top_sources', null=True)
    sentiment_top_countries      = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sentiment_top_countries', null=True)
    sentiment_top_authors        = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sentiment_top_authors', null=True)
    sentiment_top_languages      = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sentiment_top_languages', null=True)
    sentiment_for_period         = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sentiment_for_period', null=True)
    content_volume_top_authors   = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_content_volume_top_authors', null=True)
    content_volume_top_countries = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_content_volume_top_countries', null=True)
    top_keywords                 = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_top_keywords', null=True)
    sentiment_top_keywords       = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sentiment_top_keywords', null=True)
    sentiment_number_of_results  = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sentiment_number_of_results', null=True)
    sentiment_diagram            = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sentiment_diagram', null=True)
    authors_by_country           = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_authors_by_country', null=True)
    top_sharing_sources          = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_top_sharing_sources', null=True)
    overall_top_sources          = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_overall_top_sources', null=True)
    sources_by_country           = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sources_by_country', null=True)
    sources_by_language          = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_sources_by_language', null=True)
    authors_by_language          = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_authors_by_language', null=True)
    authors_by_sentiment         = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_authors_by_sentiment', null=True)
    overall_top_authors          = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_overall_top_authors', null=True)
    top_keywords_by_country      = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_top_keywords_by_country', null=True)
    languages_by_country         = models.ForeignKey(WidgetDescription, on_delete=models.CASCADE, related_name='onl_languages_by_country', null=True)

    def __str__(self):
        return str(self.project)


class ClippingFeedContentWidget(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')
    post    = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post', related_name='posts')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project_id', 'post_id'], name='clipping widget uniqueness constraint')
        ]


class ProjectDimensions(models.Model):
    project   = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')
    dimension = models.ForeignKey(Dimensions, on_delete=models.CASCADE, verbose_name='Dimension')


@receiver(post_save, sender=Project)
def create_widgets_list(sender, instance, created, **kwargs):
    if created:
        WidgetsList2.objects.create(project=instance)


@receiver(post_save, sender=WidgetsList2)
def create_widget_description(sender, instance, created, **kwargs):
    if created:
        instance.summary                      = WidgetDescription.objects.create(title='Summary', default_title='Summary')
        instance.volume                       = WidgetDescription.objects.create(title='Content volume', default_title='Content volume')
        instance.clipping_feed_content        = WidgetDescription.objects.create(title='Clipping feed content', default_title='Clipping feed content')
        instance.top_authors                  = WidgetDescription.objects.create(title='Top authors', default_title='Top authors')
        instance.top_sources                  = WidgetDescription.objects.create(title='Top sources', default_title='Top sources')
        instance.top_countries                = WidgetDescription.objects.create(title='Top countries', default_title='Top countries')
        instance.top_languages                = WidgetDescription.objects.create(title='Top languages', default_title='Top languages')
        instance.content_volume_top_sources   = WidgetDescription.objects.create(title='Content Volume by top sources', default_title='Content Volume by top sources')
        instance.sentiment_top_sources        = WidgetDescription.objects.create(title='Sentiment top sources', default_title='Sentiment top sources')
        instance.sentiment_top_countries      = WidgetDescription.objects.create(title='Sentiment top countries', default_title='Sentiment top countries')
        instance.sentiment_top_authors        = WidgetDescription.objects.create(title='Sentiment top authors', default_title='Sentiment top authors')
        instance.sentiment_top_languages      = WidgetDescription.objects.create(title='Sentiment top languages', default_title='Sentiment top languages')
        instance.sentiment_for_period         = WidgetDescription.objects.create(title='Sentiment for period', default_title='Sentiment for period')
        instance.content_volume_top_authors   = WidgetDescription.objects.create(title='Content volume by top authors', default_title='Content Volume by authors')
        instance.content_volume_top_countries = WidgetDescription.objects.create(title='Content volume by top countries', default_title='Content Volume by countries')
        instance.top_keywords                 = WidgetDescription.objects.create(title='Top keywords', default_title='Top keywords')
        instance.sentiment_top_keywords       = WidgetDescription.objects.create(title='Sentiment top keywords', default_title='Sentiment top keywords')
        instance.sentiment_number_of_results  = WidgetDescription.objects.create(title='Sentiment number of results', default_title='Sentiment number of results')
        instance.sentiment_diagram            = WidgetDescription.objects.create(title='Sentiment diagram', default_title='Sentiment diagram')
        instance.authors_by_country           = WidgetDescription.objects.create(title='Authors by country', default_title='Authors by country')
        instance.top_sharing_sources          = WidgetDescription.objects.create(title='Top sharing sources', default_title='Top sharing sources')
        instance.sources_by_country           = WidgetDescription.objects.create(title='Sources by country', default_title='Sources by country')
        instance.sources_by_language          = WidgetDescription.objects.create(title='Sources by language', default_title='Sources by language')
        instance.overall_top_sources          = WidgetDescription.objects.create(title='Overall top sources', default_title='Overall top sources')
        instance.authors_by_language          = WidgetDescription.objects.create(title='Authors by language', default_title='Authors by language')
        instance.authors_by_sentiment         = WidgetDescription.objects.create(title='Authors by sentiment', default_title='Authors by sentiment')
        instance.overall_top_authors          = WidgetDescription.objects.create(title='Overall top authors', default_title='Overall top authors')
        instance.top_keywords_by_country      = WidgetDescription.objects.create(title='Top keywords by country', default_title='Top keywords by country')
        instance.languages_by_country         = WidgetDescription.objects.create(title='Top languages by country', default_title='Top languages by country')
        instance.save()
