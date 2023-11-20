from drf_writable_nested.serializers import WritableNestedModelSerializer
from twenty_four_seven.models import WorkspaceTwentyFourSeven
from twenty_four_seven.models import ProjectTwentyFourSeven
from twenty_four_seven.models import WARecipient
from twenty_four_seven.models import Item
from api.serializers import UserSerializer
from rest_framework import serializers
from project.models import Post


class WARecipientSerializer(WritableNestedModelSerializer):
    class Meta:
        model = WARecipient
        exclude = ['id', 'updated_at', 'created_at']


class PostSerializer(WritableNestedModelSerializer):
    feedlink__country = serializers.CharField(source='feedlink.country')
    feed_language__language = serializers.CharField(source='feed_language.language')
    feedlink__alexaglobalrank = serializers.CharField(source='feedlink.alexaglobalrank')
    feedlink__sourceurl = serializers.CharField(source='feedlink.sourceurl')

    class Meta:
        model = Post
        fields = [
            'id',
            'entry_title',
            'entry_summary',
            'entry_links_href',
            'entry_published',
            'sentiment',
            'feedlink__country',
            'feed_language__language',
            'feedlink__alexaglobalrank',
            'full_text',
            'feed_image_link',
            'feedlink__sourceurl',
        ]


class NestedItemSerializer(WritableNestedModelSerializer):
    post = PostSerializer(required=False)

    class Meta:
        model = Item
        exclude = ['linked_items']


class ItemPatchSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemSerializer(WritableNestedModelSerializer):
    post = PostSerializer(required=False)
    linked_items = NestedItemSerializer(many=True, required=False)

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
    wa_recipient = WARecipientSerializer(many=True, required=False)
    
    class Meta:
        model = ProjectTwentyFourSeven
        fields = '__all__'


class WorkspaceTwentyFourSevenSerializer(WritableNestedModelSerializer):
    tfs_workspace_projects = ProjectTwentyFourSevenSerializer(many=True, required=False)
    members = UserSerializer(many=True, required=False)
   
    class Meta:
        model = WorkspaceTwentyFourSeven
        fields = '__all__'
