from drf_writable_nested.serializers import WritableNestedModelSerializer
from expert_filters.models import Group, Preset


class GroupSerializer(WritableNestedModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'


class PresetSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Preset
        fields = '__all__'
