from drf_writable_nested.serializers import WritableNestedModelSerializer
from comparison.models import ProjectComparison, WorkspaceComparison
from api.serializers import UserSerializer



class ProjectComparisonPostSerializer(WritableNestedModelSerializer):

    class Meta:
        model = ProjectComparison
        fields = '__all__'


class WorkspaceComparisonPostSerializer(WritableNestedModelSerializer):
    cmpr_workspace_projects = ProjectComparisonPostSerializer(many=True, required=False)

    class Meta:
        model = WorkspaceComparison
        fields = '__all__'


class ProjectComparisonSerializer(WritableNestedModelSerializer):
    members = UserSerializer(many=True, required=False)

    class Meta:
        model = ProjectComparison
        fields = '__all__'


class WorkspaceComparisonSerializer(WritableNestedModelSerializer):
    cmpr_workspace_projects = ProjectComparisonSerializer(many=True, required=False)
    members = UserSerializer(many=True, required=False)

    class Meta:
        model = WorkspaceComparison
        fields = '__all__'
