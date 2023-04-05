from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from project.models import Project, Post
from django.dispatch import receiver
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
  summary_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sum_widg_description', null=True)
  volume_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='vol_widg_description', null=True)
  clipping_feed_content_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='cl_fd_cont_widg_description',null=True)
  top_10_authors_by_volume_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='top_10_auth_by_vol_widg_description',null=True)
  top_10_brands_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='top_10_brands_widg_description', null=True)
  top_10_countries_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='top_10_countries_widg_description', null=True)
  top_10_languages_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='top_10_languages_widg_description', null=True)
  content_volume_top_5_source_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='content_volume_top_5_source_widget', null=True)
  sentiment_top_10_sources_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sentiment_top_10_sources_widget', null=True)
  sentiment_top_10_countries_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sentiment_top_10_countries_widget', null=True)
  sentiment_top_10_authors_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sentiment_top_10_authors_widget', null=True)
  sentiment_top_10_languages_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sentiment_top_10_languages_widget', null=True)
  sentiment_for_period_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sentiment_for_period_widget', null=True)
  content_volume_top_5_authors_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='content_volume_top_5_authors_widget', null=True)
  content_volume_top_5_countries_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='content_volume_top_5_countries_widget', null=True)
  top_keywords = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='top_keywords', null=True)
  sentiment_top_keywords = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sentiment_top_keywords', null=True)
  sentiment_number_of_results = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sentiment_number_of_results', null=True)
  sentiment_diagram = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sentiment_diagram', null=True)
  authors_by_country = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='authors_by_country', null=True)

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
    wd1.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0]) # List of permited dimensions ???
    wd1.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0]) # Second permited dimension 
    wd1.save()
    wd2 = WidgetDescription.objects.create(title='Content volume', default_title='Content volume')
    wd2.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0]) # List of permited dimensions ???
    wd2.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd2.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0]) # Second permited dimension
    wd2.linked_dimensions.add(Dimensions.objects.get_or_create(title='All Data')[0])
    wd2.save()
    wd3 = WidgetDescription.objects.create(title='Clipping feed content', default_title='Clipping feed content')
    wd3.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0]) # List of permited dimensions ???
    wd3.linked_dimensions.add(Dimensions.objects.get_or_create(title='City')[0]) # Second permited dimension
    wd3.save()
    wd4 = WidgetDescription.objects.create(title='Top authors by volume', default_title='Top 10 authors by volume')
    wd4.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0]) # List of permited dimensions ???
    wd4.linked_dimensions.add(Dimensions.objects.get_or_create(title='City')[0]) # Second permited dimension
    wd4.save()
    wd5 = WidgetDescription.objects.create(title='Top brands by volume', default_title='Top 10 brands by volume')
    wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Sentiment')[0])
    wd5.save()
    wd6 = WidgetDescription.objects.create(title='Top countries by volume', default_title='Top 10 countries by volume')
    wd6.linked_dimensions.add(Dimensions.objects.get_or_create(title='Source')[0])
    wd6.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    wd6.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    wd6.linked_dimensions.add(Dimensions.objects.get_or_create(title='Sentiment')[0])
    wd6.save()
    wd7 = WidgetDescription.objects.create(title='Top languages', default_title='Top 10 languages')
    wd7.linked_dimensions.add(Dimensions.objects.get_or_create(title='Source')[0])
    wd7.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    wd7.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd7.save()
    wd8 = WidgetDescription.objects.create(title='Content Volume by top sources', default_title='Content Volume by Top 5 sources')
    wd8.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    wd8.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    wd8.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd8.save()
    wd9 = WidgetDescription.objects.create(title='Sentiment top sources widget', default_title='Sentiment top 10 sources widget')
    wd9.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    wd9.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    wd9.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd9.save()
    wd10 = WidgetDescription.objects.create(title='Sentiment top countries widget', default_title='Sentiment top 10 countries widget')
    wd10.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    wd10.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    wd10.linked_dimensions.add(Dimensions.objects.get_or_create(title='Source')[0])
    wd10.save()
    wd11 = WidgetDescription.objects.create(title='Sentiment top authors widget', default_title='Sentiment top 10 authors widget')
    wd11.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    wd11.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd11.linked_dimensions.add(Dimensions.objects.get_or_create(title='Source')[0])
    wd11.save()
    wd12 = WidgetDescription.objects.create(title='Sentiment top languages widget', default_title='Sentiment top 10 languages widget')
    wd12.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd12.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd12.linked_dimensions.add(Dimensions.objects.get_or_create(title='Source')[0])
    wd12.save()
    wd13 = WidgetDescription.objects.create(title='Sentiment for period widget', default_title='Sentiment for period widget')
    wd13.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd13.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    wd13.linked_dimensions.add(Dimensions.objects.get_or_create(title='Source')[0])
    wd13.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    wd13.save()
    wd14 = WidgetDescription.objects.create(title='Content volume by top authors', default_title='Content Volume by Top 5 authors')
    wd14.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd14.linked_dimensions.add(Dimensions.objects.get_or_create(title='Source')[0])
    wd14.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    wd14.save()
    wd15 = WidgetDescription.objects.create(title='Content volume by top countries', default_title='Content Volume by Top 5 countries')
    wd15.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    wd15.linked_dimensions.add(Dimensions.objects.get_or_create(title='Source')[0])
    wd15.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
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
    instance.summary_widget = wd1
    instance.volume_widget = wd2
    instance.clipping_feed_content_widget = wd3
    instance.top_10_authors_by_volume_widget = wd4
    instance.top_10_brands_widget = wd5
    instance.top_10_countries_widget = wd6
    instance.top_10_languages_widget = wd7
    instance.content_volume_top_5_source_widget = wd8
    instance.sentiment_top_10_sources_widget = wd9
    instance.sentiment_top_10_countries_widget = wd10
    instance.sentiment_top_10_authors_widget = wd11
    instance.sentiment_top_10_languages_widget = wd12
    instance.sentiment_for_period_widget = wd13
    instance.content_volume_top_5_authors_widget = wd14
    instance.content_volume_top_5_countries_widget = wd15
    instance.top_keywords = wd16
    instance.sentiment_top_keywords = wd17
    instance.sentiment_number_of_results = wd18
    instance.sentiment_diagram = wd19
    instance.authors_by_country = wd20
    instance.save()

class ClippingFeedContentWidget(models.Model):
  project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='Project')
  post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name ='Post', related_name='posts')

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['project_id', 'post_id'], name='clipping widget uniqueness constraint')
    ]


class ProjectDimensions(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project') 
  dimension = models.ForeignKey(Dimensions,on_delete=models.CASCADE,verbose_name='Dimension')
