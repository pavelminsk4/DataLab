from comparison.serializers import WorkspaceComparisonCreateSerializer
from comparison.serializers import ProjectComparisonCreateSerializer
from comparison.serializers import WorkspaceComparisonSerializer
from comparison.serializers import ProjectComparisonSerializer
from comparison.classes.summary_feature import SummaryFactory
from comparison.serializers import ComparisonItemSerializer
from comparison.models import WorkspaceComparison
from comparison.models import ProjectComparison
from comparison.models import ComparisonItem
from django.http import JsonResponse
from rest_framework import viewsets


class WorkspaceComparisonViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return WorkspaceComparison.objects.filter(members=user)
        return WorkspaceComparison.objects.none()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WorkspaceComparisonCreateSerializer
        return WorkspaceComparisonSerializer


class ProjectComparisonViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return ProjectComparison.objects.filter(members=user, workspace=self.kwargs['workspace_pk'])
        return ProjectComparison.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectComparisonCreateSerializer
        return ProjectComparisonSerializer


class ItemComparisonViewSet(viewsets.ModelViewSet):
    serializer_class = ComparisonItemSerializer
    queryset = ComparisonItem.objects.all()


def get_projects(request):
    online_ws = request.user.user_profile.department.workspaces.all()
    social_ws = request.user.user_profile.department.social_workspaces.all()
    res = {
        'Online': [{ws.title: [{'title': pr.title, 'id': pr.id} for pr in ws.projects.all()]} for ws in online_ws],
        'Social': [{ws.title: [{'title': pr.title, 'id': pr.id} for pr in ws.social_workspace_projects.all()]} for ws in social_ws],
    }
    return JsonResponse(res, safe=False)


def get_summary_feature(request, pk):
    pr = ProjectComparison.objects.get(id=pk)
    res = [SummaryFactory(item).define().get_widgets() for item in pr.cmpr_items.all()]
    return JsonResponse(res, safe=False)
