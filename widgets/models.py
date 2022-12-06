from django.db import models
from project.models import Project, Post
from django.db.models.signals import post_save
from django.dispatch import receiver

class Dimensions(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField(blank=True)

  def __str__(self):
    return str(self.title)

class WidgetDescription(models.Model):
  is_active = models.BooleanField(default=False)
  title = models.CharField(default='Title', max_length=30)
  description = models.TextField(default='Description')
  aggregation_period = models.CharField(default='day', max_length=10)
  linked_dimensions = models.ManyToManyField(Dimensions, blank=True)
  author_dim_pivot = models.CharField(max_length=30, default=None, null=True, blank=True)
  country_dim_pivot = models.CharField(max_length=30, default=None, null=True, blank=True)
  source_dim_pivot = models.CharField(max_length=30, default=None, null=True, blank=True)
  language_dim_pivot = models.CharField(max_length=30, default=None, null=True, blank=True)
  sentiment_dim_pivot = models.CharField(max_length=30, default=None, null=True, blank=True)

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
  #clipping_widget = models.ForeignKey(WidgetDescription, on_delete=models.SET_NULL, related_name='clippint_widg_description', null=True)

  def __str__(self):
    return str(self.project)

@receiver(post_save, sender=Project)
def create_widgets_list(sender, instance, created, **kwargs):
  if created:
    WidgetsList2.objects.create(project=instance)

@receiver(post_save, sender=WidgetsList2)
def create_widget_description(sender, instance, created, **kwargs):
  if created:
    wd1 = WidgetDescription.objects.create(title='Summary')
    wd1.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0]) # List of permited dimensions ???
    wd1.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0]) # Second permited dimension 
    wd1.save()
    wd2 = WidgetDescription.objects.create(title='Content volume')
    wd2.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0]) # List of permited dimensions ???
    wd2.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd2.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0]) # Second permited dimension
    wd2.linked_dimensions.add(Dimensions.objects.get_or_create(title='All Data')[0])
    wd2.save()
    wd3 = WidgetDescription.objects.create(title='Clipping feed content')
    wd3.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0]) # List of permited dimensions ???
    wd3.linked_dimensions.add(Dimensions.objects.get_or_create(title='City')[0]) # Second permited dimension
    wd3.save()
    wd4 = WidgetDescription.objects.create(title='Top 10 authors by volume')
    wd4.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0]) # List of permited dimensions ???
    wd4.linked_dimensions.add(Dimensions.objects.get_or_create(title='City')[0]) # Second permited dimension
    wd4.save()
    wd5 = WidgetDescription.objects.create(title='Top 10 brands by volume')
    wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Sentiment')[0])
    wd5.save()
    # wd5 = WidgetDescription.objects.create(title='Clipping Widget')
    # wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Country')[0])
    # wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Author')[0])
    # wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Language')[0])
    # wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Source')[0])
    # wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='Sentiment')[0])
    # wd5.linked_dimensions.add(Dimensions.objects.get_or_create(title='All Data')[0])
    # wd5.save()
    instance.summary_widget = wd1
    instance.volume_widget = wd2
    instance.clipping_feed_content_widget = wd3
    instance.top_10_authors_by_volume_widget = wd4
    instance.top_10_brands_widget = wd5
    # instance.clipping_widget = wd5
    instance.save()

class ClippingFeedContentWidget(models.Model):
  project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='Project')
  post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name ='Post', related_name='posts')


class ProjectDimensions(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project') 
  dimension = models.ForeignKey(Dimensions,on_delete=models.CASCADE,verbose_name='Dimension')
