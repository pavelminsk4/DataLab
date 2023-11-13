from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db import models


class Preset(models.Model):
    title       = models.CharField(max_length=100)
    query       = ArrayField(models.TextField(), null=True, blank=True)
    creator     = models.ForeignKey(User, related_name='preset_creator', on_delete=models.SET_NULL, null=True)
    updated_at  = models.DateTimeField(auto_now=True)
    created_at  = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
    title       = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    presets     = models.ManyToManyField(Preset, blank=True)
    creator     = models.ForeignKey(User, related_name='group_creator', on_delete=models.SET_NULL, null=True)
    updated_at  = models.DateTimeField(auto_now=True)
    created_at  = models.DateTimeField(auto_now_add=True)
