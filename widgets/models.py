from django.db import models
from project.models import Project
from django.db.models.signals import post_save
from django.dispatch import receiver

class WidgetsList(models.Model):
  project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='widget_list', editable=False)
  summary_widget = models.BooleanField(default=False)
  volume_widget = models.BooleanField(default=False)

  def __str__(self):
    return str(self.project)

@receiver(post_save, sender=Project)
def create_widgets_list(sender, instance, created, **kwargs):
    if created:
        WidgetsList.objects.create(project=instance)
