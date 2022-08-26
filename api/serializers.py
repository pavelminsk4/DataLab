from django.contrib.auth.models import User
from project.models import Project
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Project
    fields = ['title', 'creator', 'keywords']
