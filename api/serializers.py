from django.contrib.auth.models import User
from project.models import Project
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = "__all__"
