from django.contrib.auth.models import User
from project.models import Project, Workspace
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
  users = UserSerializer
  class Meta:
    model = Project
    fields = "__all__"

class WorkspaceSerializer(serializers.ModelSerializer):
  projects = ProjectSerializer(many=True)
  class Meta:
    model = Workspace
    fields = ['id', 'title', 'description', 'members', 'company', 'projects']
    #fields = '__all__'

class WorkspaceCreateSerializer(serializers.ModelSerializer):
  projects = ProjectSerializer(many=True)
  class Meta:
    model = Workspace
    fields = '__all__'

  def create(self, validated_data):
    workspace = Workspace.objects.create(title=validated_data['title'], description=validated_data['description'])
    project = Project.objects.create(**validated_data['projects'][0])
    workspace.members.set(validated_data["members"])
    workspace.projects.add(project)
    return workspace
