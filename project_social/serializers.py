from drf_writable_nested.serializers import WritableNestedModelSerializer
from tweet_binder.models import TweetBinderPost
from api.serializers import UserSerializer
from rest_framework import serializers
from .models import *

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
  social_workspace_projects = ProjectSocialSerializer(many=True, required=False)
  class Meta:
    model = WorkspaceSocial
    fields = '__all__'

  def create(self, validated_data):
    workspace = WorkspaceSocial.objects.create(title=validated_data['title'], description=validated_data['description'], department=validated_data['department'] or None)
    project = ProjectSocial.objects.create(**validated_data['projects'][0])
    workspace.members.set(validated_data["members"])
    workspace.social_workspace_projects.add(project)
    return workspace

class SocialWidgetDescriptionSerializer(WritableNestedModelSerializer):
  class Meta:
    model = SocialWidgetDescription
    fields = '__all__'

class WidgetsListSerializer(WritableNestedModelSerializer):
  summary = SocialWidgetDescriptionSerializer()
  clipping_feed_content = SocialWidgetDescriptionSerializer()
  top_locations = SocialWidgetDescriptionSerializer()
  top_authors = SocialWidgetDescriptionSerializer()
  top_languages = SocialWidgetDescriptionSerializer()
  content_volume = SocialWidgetDescriptionSerializer()
  content_volume_by_top_locations = SocialWidgetDescriptionSerializer()
  content_volume_by_top_authors = SocialWidgetDescriptionSerializer()
  content_volume_by_top_languages = SocialWidgetDescriptionSerializer()
  sentiment = SocialWidgetDescriptionSerializer()
  gender_volume = SocialWidgetDescriptionSerializer()
  sentiment_number_of_results = SocialWidgetDescriptionSerializer()
  sentiment_authors = SocialWidgetDescriptionSerializer()
  sentiment_locations = SocialWidgetDescriptionSerializer()
  sentiment_languages = SocialWidgetDescriptionSerializer()
  sentiment_by_gender = SocialWidgetDescriptionSerializer()
  class Meta:
    model = SocialWidgetsList
    fields = '__all__'

class TweetBinderPostAuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = TweetBinderPost
    fields = ['user_name']

class TweetBinderPostLocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = TweetBinderPost
    fields = ['locationString']

class TweetBinderPostLanguageSerializer(serializers.ModelSerializer):
  class Meta:
    model = TweetBinderPost
    fields = ['language']
