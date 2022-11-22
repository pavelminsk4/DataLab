from django.contrib.auth.models import User
from project.models import Project, Workspace, Speech
from accounts.models import Profile, department
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from countries_plus.models import Country
from widgets.models import WidgetsList, WidgetsList2, ClippingFeedContentWidget, WidgetDescription, Dimensions, ProjectDimensions
from reports.models import Templates
from alerts.models import Alert

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
  note = serializers.CharField(max_length=1000, allow_blank=True)
  class Meta:
    model = Project
    fields = '__all__'

class WorkspaceSerializer(WritableNestedModelSerializer):
  projects = ProjectSerializer(many=True, required=False)
  description = serializers.CharField(max_length=1000, allow_blank=True)
  members = UserSerializer(many=True)
  class Meta:
    model = Workspace
    fields = ['id', 'title', 'description', 'members', 'company', 'projects', 'created_at']

class WorkspaceCreateSerializer(serializers.ModelSerializer):
  projects = ProjectSerializer(many=True, required=False)
  description = serializers.CharField(max_length=1000, allow_blank=True)
  class Meta:
    model = Workspace
    fields = '__all__'

  def create(self, validated_data):
    workspace = Workspace.objects.create(title=validated_data['title'], description=validated_data['description'] or None)
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

class WidgetDescriptionSerializer(WritableNestedModelSerializer):
  class Meta:
    model = WidgetDescription
    fields = '__all__'

class WidgetsListSerializer(WritableNestedModelSerializer):
  summary_widget = WidgetDescriptionSerializer()
  volume_widget = WidgetDescriptionSerializer()
  clipping_feed_content_widget = WidgetDescriptionSerializer()
  top_10_authors_by_volume_widget = WidgetDescriptionSerializer()
  class Meta:
    model = WidgetsList2
    #fields = '__all__'
    fields = ['summary_widget', 'volume_widget', 'clipping_feed_content_widget', 'top_10_authors_by_volume_widget']

class ClippingFeedContentWidgetListSerializer(serializers.ListSerializer):
  def create(self, validated_data):
    users = [ClippingFeedContentWidget(**item) for item in validated_data]
    return ClippingFeedContentWidget.objects.bulk_create(users)
    
class ClippingFeedContentWidgetSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClippingFeedContentWidget
    fields = '__all__'
    list_serializer_class = ClippingFeedContentWidgetListSerializer

class DimensionsSerializer(WritableNestedModelSerializer):
  class Meta:
    model = Dimensions
    fields = '__all__'

class ProjectDimensionsSerializer(WritableNestedModelSerializer):
  class Meta:
    model = ProjectDimensions
    fields = '__all__'

class ProjectDimensionsListSerializer(WritableNestedModelSerializer):
  dimension = DimensionsSerializer()
  class Meta:
    model = ProjectDimensions
    fields = '__all__'

class TemplatesSerializer(WritableNestedModelSerializer):
  class Meta:
    model = Templates
    fields = '__all__'

class AlertsSerializer(WritableNestedModelSerializer):
  user = UserSerializer(many=True)
  class Meta:
    model = Alert
    fields = '__all__'
