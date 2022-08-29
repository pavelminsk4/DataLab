from django.db import models
from django.contrib.auth.models import User

class Workspace(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  members = models.ManyToManyField(User,null=True,blank=True)

class Project(models.Model):
  title = models.CharField(max_length=100)
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  note = models.CharField(max_length=200, null=True, blank=True)
  keywords = models.CharField(max_length=200, null=True, blank=True)
  ignore_keywords = models.CharField(max_length=200, null=True, blank=True)
  max_items = models.CharField(max_length=200, null=True, blank=True)
  image = models.ImageField(null=True, blank=True, upload_to='images')
  arabic_name = models.CharField(max_length=100, null=True, blank=True)
  english_name = models.CharField(max_length=100, null=True, blank=True)
  workspase_id = models.ForeignKey(Workspace, blank=True, null=True, on_delete=models.CASCADE)
