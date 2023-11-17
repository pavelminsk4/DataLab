from drf_writable_nested.serializers import WritableNestedModelSerializer
from expert_filters.models import Group, Preset


class PresetSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Preset
        fields = '__all__'


class GroupNestedSerializer(WritableNestedModelSerializer):
    presets = PresetSerializer(many=True, required=False)

    class Meta:
        model = Group
        fields = '__all__'


class GroupBasicSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
