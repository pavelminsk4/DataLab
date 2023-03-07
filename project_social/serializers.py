from rest_framework import serializers
from .models import *
from api.serializers import UserSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer

class ProjectSocialSerializer(serializers.ModelSerializer):
  users = UserSerializer
  note = serializers.CharField(max_length=1000, allow_blank=True)
  class Meta:
    model = ProjectSocial
    fields = '__all__'

class WorkspaceSocialSerializer(WritableNestedModelSerializer):
  social_workspace_projects = ProjectSocialSerializer(many=True, required=False)
  description = serializers.CharField(max_length=1000, allow_blank=True, required=False)
  members = UserSerializer(many=True, required=False)
  class Meta:
    model = WorkspaceSocial
    fields = ['id', 'title', 'description', 'members', 'social_workspace_projects', 'created_at']

class WorkspaceCreateSerializer(serializers.ModelSerializer):
  projects = ProjectSocialSerializer(many=True, required=False)
  description = serializers.CharField(max_length=1000, allow_blank=True)
  class Meta:
    model = WorkspaceSocial
    fields = '__all__'

  def create(self, validated_data):
    workspace = WorkspaceSocial.objects.create(title=validated_data['title'], description=validated_data['description'], department=validated_data['department'] or None)
    project = ProjectSocial.objects.create(**validated_data['projects'][0])
    workspace.members.set(validated_data["members"])
    workspace.social_workspace_projects.add(project)
    return workspace
