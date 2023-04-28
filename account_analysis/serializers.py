from drf_writable_nested.serializers import WritableNestedModelSerializer
from tweet_binder.models import *
from api.serializers import UserSerializer
from rest_framework import serializers
from .models import *


class ProjectAccountAnalysisSerializer(serializers.ModelSerializer):
    users = UserSerializer

    class Meta:
        model = ProjectAccountAnalysis
        fields = '__all__'


class WorkspaceAccountAnalysisSerializer(WritableNestedModelSerializer):
    account_analysis_workspace_projects = ProjectAccountAnalysisSerializer(
        many=True, required=False)
    description = serializers.CharField(
        max_length=1000, allow_blank=True, required=False)
    members = UserSerializer(many=True, required=False)

    class Meta:
        model = WorkspaceAccountAnalysis
        fields = ['id', 'title', 'description', 'members',
                  'account_analysis_workspace_projects', 'created_at']


class WorkspaceCreateSerializer(serializers.ModelSerializer):
    projects = ProjectAccountAnalysisSerializer(many=True, required=False)
    description = serializers.CharField(max_length=1000, allow_blank=True)
    account_analysis_workspace_projects = ProjectAccountAnalysisSerializer(
        many=True, required=False)

    class Meta:
        model = WorkspaceAccountAnalysis
        fields = '__all__'

    def create(self, validated_data):
        workspace = WorkspaceAccountAnalysis.objects.create(
            title=validated_data['title'], description=validated_data['description'], department=validated_data['department'] or None)
        project = ProjectAccountAnalysis.objects.create(
            **validated_data['projects'][0])
        workspace.members.set(validated_data["members"])
        workspace.account_analysis_workspace_projects.add(project)
        return workspace


class AccountAnalysisWidgetDescriptionSerializer(WritableNestedModelSerializer):
    class Meta:
        model = AccountAnalysisWidgetDescription
        fields = '__all__'


class WidgetsListSerializer(WritableNestedModelSerializer):
    summary = AccountAnalysisWidgetDescriptionSerializer()
    profile_timeline = AccountAnalysisWidgetDescriptionSerializer()
    most_frequent_post_types = AccountAnalysisWidgetDescriptionSerializer()
    most_engaging_post_types = AccountAnalysisWidgetDescriptionSerializer()

    class Meta:
        model = AccountAnalysisWidgetsList
        fields = '__all__'


class TweetBinderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetBinderPost
        fields = '__all__'


class TweetBinderUserTrackerSerializer(serializers.ModelSerializer):
    account_analysis_project = ProjectAccountAnalysisSerializer()

    class Meta:
        model = TweetBinderUserTracker
        fields = '__all__'


class TweetBinderUserTrackerAnalysisSerializer(serializers.ModelSerializer):
    user_alias = TweetBinderUserTrackerSerializer()

    class Meta:
        model = TweetBinderUserTrackerAnalysis
        fields = '__all__'
