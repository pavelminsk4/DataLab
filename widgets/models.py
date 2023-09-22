from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from talkwalker.models import TalkwalkerPost
from django.dispatch import receiver
from project.models import Project
from django.db import models

class Dimensions(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField(blank=True)

  def __str__(self):
    return str(self.title)

class WidgetDescription(models.Model):
  is_active = models.BooleanField(default=False)
  title = models.CharField(default='Title', max_length=50)
  default_title = models.CharField(default='Default Title', max_length=50)
  top_counts = models.IntegerField(default=5)
  description = models.TextField(default='', null=True, blank=True)
  aggregation_period = models.CharField(default='day', max_length=10)
  linked_dimensions = models.ManyToManyField(Dimensions, blank=True)
  author_dim_pivot = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  country_dim_pivot = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  source_dim_pivot = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  language_dim_pivot = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  sentiment_dim_pivot = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
  chart_type = models.CharField(max_length=150, default=None, null=True, blank=True)

class WidgetsList(models.Model):
  project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='widget_list', editable=False)
  summary_widget = models.BooleanField(default=False)
  volume_widget = models.BooleanField(default=False)
  clipping_feed_content_widget = models.BooleanField(default=False)
  top_10_authors_by_volume_widget = models.BooleanField(default=False)

  def __str__(self):
    return str(self.project)

class WidgetsList2(models.Model):
  project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='widgets_list_2', editable=False)
  summary = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_summary', null=True)
  volume = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_volume', null=True)
  clipping_feed_content = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_clipping_feed_content',null=True)
  top_authors = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_top_authors',null=True)
  top_sources = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_top_sources', null=True)
  top_countries = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_top_countries', null=True)
  top_languages = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_top_languages', null=True)
  content_volume_top_sources = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_content_volume_top_sources', null=True)
  sentiment_top_sources = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sentiment_top_sources', null=True)
  sentiment_top_countries = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sentiment_top_countries', null=True)
  sentiment_top_authors = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sentiment_top_authors', null=True)
  sentiment_top_languages = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sentiment_top_languages', null=True)
  sentiment_for_period = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sentiment_for_period', null=True)
  content_volume_top_authors = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_content_volume_top_authors', null=True)
  content_volume_top_countries = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_content_volume_top_countries', null=True)
  top_keywords = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_top_keywords', null=True)
  sentiment_top_keywords = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sentiment_top_keywords', null=True)
  sentiment_number_of_results = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sentiment_number_of_results', null=True)
  sentiment_diagram = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sentiment_diagram',null=True)
  authors_by_country = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_authors_by_country',null=True)
  top_sharing_sources = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_top_sharing_sources',null=True)
  overall_top_sources = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_overall_top_sources',null=True)
  sources_by_country = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sources_by_country',null=True)
  sources_by_language = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_sources_by_language',null=True)
  authors_by_language = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_authors_by_language',null=True)
  authors_by_sentiment = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_authors_by_sentiment',null=True)
  overall_top_authors = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_overall_top_authors',null=True)
  top_keywords_by_country = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_top_keywords_by_country',null=True)
  languages_by_country = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='onl_languages_by_country',null=True)

  def __str__(self):
    return str(self.project)

@receiver(post_save, sender=Project)
def create_widgets_list(sender, instance, created, **kwargs):
  if created:
    WidgetsList2.objects.create(project=instance)

@receiver(post_save, sender=WidgetsList2)
def create_widget_description(sender, instance, created, **kwargs):
  if created:
    wd1 = WidgetDescription.objects.create(title='Summary', default_title='Summary')
    wd1.save()
    wd2 = WidgetDescription.objects.create(title='Content volume', default_title='Content volume')
    wd2.save()
    wd3 = WidgetDescription.objects.create(title='Clipping feed content', default_title='Clipping feed content')
    wd3.save()
    wd4 = WidgetDescription.objects.create(title='Top authors', default_title='Top authors')
    wd4.save()
    wd5 = WidgetDescription.objects.create(title='Top sources', default_title='Top sources')
    wd5.save()
    wd6 = WidgetDescription.objects.create(title='Top countries', default_title='Top countries')
    wd6.save()
    wd7 = WidgetDescription.objects.create(title='Top languages', default_title='Top languages')
    wd7.save()
    wd8 = WidgetDescription.objects.create(title='Content Volume by top sources', default_title='Content Volume by top sources')
    wd8.save()
    wd9 = WidgetDescription.objects.create(title='Sentiment top sources', default_title='Sentiment top sources')
    wd9.save()
    wd10 = WidgetDescription.objects.create(title='Sentiment top countries', default_title='Sentiment top countries')
    wd10.save()
    wd11 = WidgetDescription.objects.create(title='Sentiment top authors', default_title='Sentiment top authors')
    wd11.save()
    wd12 = WidgetDescription.objects.create(title='Sentiment top languages', default_title='Sentiment top languages')
    wd12.save()
    wd13 = WidgetDescription.objects.create(title='Sentiment for period', default_title='Sentiment for period')
    wd13.save()
    wd14 = WidgetDescription.objects.create(title='Content volume by top authors', default_title='Content Volume by authors')
    wd14.save()
    wd15 = WidgetDescription.objects.create(title='Content volume by top countries', default_title='Content Volume by countries')
    wd15.save()
    wd16 = WidgetDescription.objects.create(title='Top keywords', default_title='Top keywords')
    wd16.save()
    wd17 = WidgetDescription.objects.create(title='Sentiment top keywords', default_title='Sentiment top keywords')
    wd17.save()
    wd18 = WidgetDescription.objects.create(title='Sentiment number of results', default_title='Sentiment number of results')
    wd18.save()
    wd19 = WidgetDescription.objects.create(title='Sentiment diagram', default_title='Sentiment diagram')
    wd19.save()
    wd20 = WidgetDescription.objects.create(title='Authors by country', default_title='Authors by country')
    wd20.save()
    wd21 = WidgetDescription.objects.create(title='Top sharing sources', default_title='Top sharing sources')
    wd21.save()
    wd22 = WidgetDescription.objects.create(title='Sources by country', default_title='Sources by country')
    wd22.save()
    wd23 = WidgetDescription.objects.create(title='Sources by language', default_title='Sources by language')
    wd23.save()
    wd24 = WidgetDescription.objects.create(title='Overall top sources', default_title='Overall top sources')
    wd24.save()
    wd25 = WidgetDescription.objects.create(title='Authors by language', default_title='Authors by language')
    wd25.save()
    wd26 = WidgetDescription.objects.create(title='Authors by sentiment', default_title='Authors by sentiment')
    wd26.save()
    wd27 = WidgetDescription.objects.create(title='Overall top authors', default_title='Overall top authors')
    wd27.save()
    wd28 = WidgetDescription.objects.create(title='Top keywords by country', default_title='Top keywords by country')
    wd28.save()
    wd29 = WidgetDescription.objects.create(title='Top languages by country', default_title='Top languages by country')
    wd29.save()
    instance.summary = wd1
    instance.volume = wd2
    instance.clipping_feed_content = wd3
    instance.top_authors = wd4
    instance.top_sources = wd5
    instance.top_countries = wd6
    instance.top_languages = wd7
    instance.content_volume_top_sources = wd8
    instance.sentiment_top_sources = wd9
    instance.sentiment_top_countries = wd10
    instance.sentiment_top_authors = wd11
    instance.sentiment_top_languages = wd12
    instance.sentiment_for_period = wd13
    instance.content_volume_top_authors = wd14
    instance.content_volume_top_countries = wd15
    instance.top_keywords = wd16
    instance.sentiment_top_keywords = wd17
    instance.sentiment_number_of_results = wd18
    instance.sentiment_diagram = wd19
    instance.authors_by_country = wd20
    instance.top_sharing_sources = wd21
    instance.sources_by_country = wd22
    instance.sources_by_language = wd23
    instance.overall_top_sources = wd24
    instance.authors_by_language = wd25
    instance.authors_by_sentiment = wd26
    instance.overall_top_authors = wd27
    instance.top_keywords_by_country = wd28
    instance.languages_by_country = wd29
    instance.save()

class ClippingFeedContentWidget(models.Model):
  project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='Project')
  post = models.ForeignKey(TalkwalkerPost,on_delete=models.CASCADE,verbose_name ='Post', related_name='posts')

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['project_id', 'post_id'], name='clipping widget uniqueness constraint')
    ]


class ProjectDimensions(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project') 
  dimension = models.ForeignKey(Dimensions,on_delete=models.CASCADE,verbose_name='Dimension')
