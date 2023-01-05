from django.contrib.auth.models import User
from project.models import Project, Workspace, Speech
from accounts.models import Profile, department
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from countries_plus.models import Country
from widgets.models import WidgetsList2, ClippingFeedContentWidget, WidgetDescription, Dimensions, ProjectDimensions
from reports.models import Templates
from alerts.models import Alert
from project.models import Post

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

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
  top_10_brands_widget = WidgetDescriptionSerializer()
  top_10_countries_widget = WidgetDescriptionSerializer()
  top_10_languages_widget = WidgetDescriptionSerializer()
  content_volume_top_5_source_widget = WidgetDescriptionSerializer()
  sentiment_top_10_sources_widget = WidgetDescriptionSerializer()
  sentiment_top_10_countries_widget = WidgetDescriptionSerializer()
  sentiment_top_10_authors_widget = WidgetDescriptionSerializer()
  sentiment_top_10_languages_widget = WidgetDescriptionSerializer()
  sentiment_for_period_widget = WidgetDescriptionSerializer()
  content_volume_top_5_authors_widget = WidgetDescriptionSerializer()
  content_volume_top_5_countries_widget = WidgetDescriptionSerializer()
  class Meta:
    model = WidgetsList2
    fields = [
      'summary_widget',
      'volume_widget',
      'clipping_feed_content_widget',
      'top_10_authors_by_volume_widget',
      'top_10_brands_widget',
      'top_10_countries_widget',
      'top_10_languages_widget',
      'content_volume_top_5_source_widget',
      'sentiment_top_10_sources_widget',
      'sentiment_top_10_countries_widget',
      'sentiment_top_10_authors_widget',
      'sentiment_top_10_languages_widget',
      'sentiment_for_period_widget',
      'content_volume_top_5_authors_widget',
      'content_volume_top_5_countries_widget',
    ]

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
  class Meta:
    model = Alert
    fields = '__all__'

class PostsSerializer(WritableNestedModelSerializer):
  class Meta:
    model = Post
    fields = ['entry_author']

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
      model = User
      fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
      extra_kwargs = {
          'first_name': {'required': True},
          'last_name': {'required': True}
      }

  def validate(self, attrs):
      if attrs['password'] != attrs['password2']:
          raise serializers.ValidationError({"password": "Password fields didn't match."})

      return attrs

  def create(self, validated_data):
      user = User.objects.create(
          username=validated_data['username'],
          email=validated_data['email'],
          first_name=validated_data['first_name'],
          last_name=validated_data['last_name']
      )

      user.set_password(validated_data['password'])
      user.save()

      return user
