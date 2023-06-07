from comparison.serializers import WorkspaceComparisonPostSerializer
from comparison.serializers import ProjectComparisonPostSerializer
from comparison.serializers import WorkspaceComparisonSerializer
from comparison.serializers import ProjectComparisonSerializer
from django.http import JsonResponse
from rest_framework import viewsets


class ProjectComparisonViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectComparisonPostSerializer
        return ProjectComparisonSerializer


class WorkspaceComparisonViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WorkspaceComparisonPostSerializer
        return WorkspaceComparisonSerializer


def get_projects(request):
    online_ws = request.user.user_profile.department.workspaces.all()
    social_ws = request.user.user_profile.department.social_workspaces.all()
    res = {
        'Online': [{ws.title: [{'title': pr.title, 'id': pr.id} for pr in ws.projects.all()]} for ws in online_ws],
        'Social': [{ws.title: [{'title': pr.title, 'id': pr.id} for pr in ws.projects.all()]} for ws in social_ws],
    }
    return JsonResponse(res, safe=False)
