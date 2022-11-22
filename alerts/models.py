from django.db import models
from accounts.models import department
from project.models import Project
from django.contrib.auth.models import User

class Alert(models.Model):
  title = models.CharField(max_length=50)
  project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='alerts')
  user = models.ManyToManyField(User, blank=True, null=True)
  triggered_on_every_n_new_posts = models.IntegerField(default=1)
  how_many_posts_to_send = models.IntegerField(default=1)
  alert_condition = models.CharField(max_length=50, blank=True, null=True)
  #privious_posts_count = models.PositiveBigIntegerField(default=0)

  def __str__(self):
    return self.title
