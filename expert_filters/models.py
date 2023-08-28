from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    creator = models.ForeignKey(User, related_name='group_creator', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Preset(models.Model):
    title = models.CharField(max_length=100)
    query = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    creator = models.ForeignKey(User, related_name='preset_creator', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
