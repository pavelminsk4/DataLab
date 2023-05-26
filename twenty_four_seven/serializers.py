from rest_framework import serializers
from .models import *
from api.serializers import UserSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from project.models import *


class PostSerializer(WritableNestedModelSerializer):
    feedlink__country = serializers.CharField(source='feedlink.country')
    class Meta:
        model = Post
        fields = ['id', 'entry_title', 'entry_summary', 'entry_links_href', 'entry_published', 'sentiment', 'feedlink__country']
        

class ItemSerializer(serializers.ModelSerializer):
    online_post = PostSerializer(required=False)

    class Meta:
        model = Item
        fields = '__all__'


class ProjectTwentyFourSevenPostSerializer(WritableNestedModelSerializer):

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
    
    class Meta:
        model = ProjectTwentyFourSeven
        fields = '__all__'


class WorkspaceTwentyFourSevenSerializer(WritableNestedModelSerializer):
    tfs_workspace_projects = ProjectTwentyFourSevenSerializer(many=True, required=False)
    members = UserSerializer(many=True, required=False)
   
    class Meta:
        model = WorkspaceTwentyFourSeven
        fields = '__all__'
