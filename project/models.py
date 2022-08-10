from django.db import models
from django.contrib.auth.models import User

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
  english_name = models.CharField(max_length=100, null=True, blank=True
  )
