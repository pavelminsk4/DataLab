from rest_framework import serializers
from .models import *
from api.serializers import UserSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class ProjectTwentyFourSevenSerializer(WritableNestedModelSerializer):
    members = UserSerializer(many=True, required=False)
    tfs_project_items = ItemSerializer(many=True, required=False)

    class Meta:
        model = ProjectTwentyFourSeven
        fields = '__all__'


class WorkspaceTwentyFourSevenSerializer(WritableNestedModelSerializer):
    tfs_workspace_projects = ProjectTwentyFourSevenSerializer(many=True, required=False)
    description = serializers.CharField(max_length=1000, allow_blank=True, required=False)
    members = UserSerializer(many=True, required=False)

    class Meta:
        model = WorkspaceTwentyFourSeven
        fields = ['id', 'title', 'description', 'members', 'tfs_workspace_projects', 'created_at']

    
class WorkspaceTwentyFourSevenCreateSerializer(serializers.ModelSerializer):
    tfs_workspace_projects = ProjectTwentyFourSevenSerializer(many=True, required=False)

    class Meta:
        model = WorkspaceTwentyFourSeven
        fields = '__all__'

    def create(self, validated_data):
        workspace = WorkspaceTwentyFourSeven.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            department=validated_data['department']
        )
        project = ProjectTwentyFourSeven.objects.create(**validated_data['tfs_workspace_projects'][0])
        workspace.members.set(validated_data['members'])
        workspace.tfs_workspace_projects.add(project)
        return workspace
