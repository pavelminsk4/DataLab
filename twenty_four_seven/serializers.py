from rest_framework import serializers
from .models import *
from api.serializers import UserSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class ProjectTwentyFourSevenPostSerializer(WritableNestedModelSerializer):
    tfs_project_items = ItemSerializer(many=True, required=False)

    class Meta:
        model = ProjectTwentyFourSeven
        fields = '__all__'


class WorkspaceTwentyFourSevenPostSerializer(WritableNestedModelSerializer):
    tfs_workspace_projects = ProjectTwentyFourSevenPostSerializer(many=True, required=False)

    class Meta:
        model = WorkspaceTwentyFourSeven
        fields = '__all__'


class ProjectTwentyFourSevenSerializer(WritableNestedModelSerializer):
    members = UserSerializer(many=True, required=False)
    tfs_project_items = ItemSerializer(many=True, required=False)
    
    class Meta:
        model = ProjectTwentyFourSeven
        fields = '__all__'


class WorkspaceTwentyFourSevenSerializer(WritableNestedModelSerializer):
    tfs_workspace_projects = ProjectTwentyFourSevenSerializer(many=True, required=False)
    members = UserSerializer(many=True, required=False)
   
    class Meta:
        model = WorkspaceTwentyFourSeven
        fields = '__all__'
