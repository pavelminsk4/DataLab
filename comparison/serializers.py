from drf_writable_nested.serializers import WritableNestedModelSerializer
from comparison.models import ProjectComparison, WorkspaceComparison, ComparisonItem
from api.serializers import UserSerializer


class ComparisonItemSerializer(WritableNestedModelSerializer):
    class Meta:
        model = ComparisonItem
        fields = '__all__'


class ProjectComparisonSerializer(WritableNestedModelSerializer):
    members = UserSerializer(many=True, required=False)
    cmpr_items = ComparisonItemSerializer(many=True, required=False)

    class Meta:
        model = ProjectComparison
        fields = '__all__'


class WorkspaceComparisonSerializer(WritableNestedModelSerializer):
    cmpr_workspace_projects = ProjectComparisonSerializer(many=True, required=False)
    members = UserSerializer(many=True, required=False)

    class Meta:
        model = WorkspaceComparison
        fields = '__all__'
