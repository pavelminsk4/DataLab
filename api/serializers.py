from django.contrib.auth.models import User
from project.models import Project, Workspace, Speech
from accounts.models import Profile, department
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from countries_plus.models import Country

class DepartmentSerializer(WritableNestedModelSerializer):
  class Meta:
    model = department
    fields = '__all__'
class ProfileSerializer(WritableNestedModelSerializer):
  department = DepartmentSerializer()
  class Meta:
    model = Profile
    fields = '__all__'
class UserSerializer(WritableNestedModelSerializer):
  user_profile = ProfileSerializer()
  class Meta:
    model = User
    fields = "__all__"
 

class ProjectSerializer(serializers.ModelSerializer):
  users = UserSerializer
  description = serializers.CharField(max_length=1000, allow_blank=True)
  class Meta:
    model = Project
    fields = "__all__"

class WorkspaceSerializer(serializers.ModelSerializer):
  projects = ProjectSerializer(many=True, required=False)
  description = serializers.CharField(max_length=1000, allow_blank=True)
  class Meta:
    model = Workspace
    fields = ['id', 'title', 'description', 'members', 'company', 'projects']

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

class CountrySerializer(WritableNestedModelSerializer):
  class Meta:
    model = Country
    fields = ['name']

class SpeechSerializer(WritableNestedModelSerializer):
  class Meta:
    model = Speech
    fields = ['language']
