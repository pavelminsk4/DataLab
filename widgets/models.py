from django.db import models
from project.models import Project, Post
from django.db.models.signals import post_save
from django.dispatch import receiver

class WidgetDescription(models.Model):
  is_active = models.BooleanField(default=False)
  title = models.CharField(default='Title', max_length=30)
  description = models.TextField(default='Description')
  aggregation_period = models.CharField(default='day', max_length=10)

class WidgetsList(models.Model):
  project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='widget_list', editable=False)
  summary_widget = models.BooleanField(default=False)
  volume_widget = models.BooleanField(default=False)
  clipping_feed_content_widget = models.BooleanField(default=False)
  top_10_authors_by_volume_widget = models.BooleanField(default=False)

  def __str__(self):
    return str(self.project)

class WidgetsList2(models.Model):
  project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='project', editable=False)
  summary_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='sum_widg_description', null=True)
  volume_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='vol_widg_description', null=True)
  clipping_feed_content_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='cl_fd_cont_widg_description',null=True)
  top_10_authors_by_volume_widget = models.ForeignKey(WidgetDescription,on_delete=models.CASCADE,related_name='top_10_auth_by_vol_widg_description',null=True)

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
    wd1.save()
    wd2 = WidgetDescription.objects.create(title='Content volume')
    wd2.save()
    wd3 = WidgetDescription.objects.create(title='Clipping feed content')
    wd3.save()
    wd4 = WidgetDescription.objects.create(title='Top 10 authors by volume')
    wd4.save()
    instance.summary_widget = wd1
    instance.volume_widget = wd2
    instance.clipping_feed_content_widget = wd3
    instance.top_10_authors_by_volume_widget = wd4
    instance.save()

class ClippingFeedContentWidget(models.Model):
  project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name ='Project')
  post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name ='Post', related_name='posts')
