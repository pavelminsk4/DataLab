from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  max_users = models.IntegerField()
  max_projects = models.IntegerField()
  max_online_feeds = models.IntegerField()
  max_social_feeds = models.IntegerField()
  max_twitter_data = models.IntegerField()
  
class Workspace(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  members = models.ManyToManyField(User,null=True,blank=True)
  company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)

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
  workspase = models.ForeignKey(Workspace, related_name='projects', blank=True, null=True, on_delete=models.CASCADE)
