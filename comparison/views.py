from comparison.serializers import WorkspaceComparisonSerializer
from comparison.serializers import ProjectComparisonSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import status

class ProjectComparisonViewSet(viewsets.ViewSet):
    def list(self, request, **kwargs):
        department = request.user.user_profile.department
        queryset = department.comparison_workspaces.get(id=kwargs['workspace_pk']).cmpr_workspace_projects.all()
        serializer = ProjectComparisonSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def retrieve(self, request, **kwargs):
        department = request.user.user_profile.department
        queryset = department.comparison_workspaces.get(id=kwargs['workspace_pk']).cmpr_workspace_projects.all()
        project = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = ProjectComparisonSerializer(project)
        return JsonResponse(serializer.data, safe=False)


class WorkspaceComparisonViewSet(viewsets.ViewSet):
    def list(self, request):
        department = request.user.user_profile.department
        queryset = department.comparison_workspaces.all()
        serializer = WorkspaceComparisonSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def create(self, request):
        data = request.data
        serializer = WorkspaceComparisonSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def get_projects(request):
    online_ws = request.user.user_profile.department.workspaces.all()
    social_ws = request.user.user_profile.department.social_workspaces.all()
    res = {
        'Online': [{ws.title: [{'title': pr.title, 'id': pr.id} for pr in ws.projects.all()]} for ws in online_ws],
        'Social': [{ws.title: [{'title': pr.title, 'id': pr.id} for pr in ws.social_workspace_projects.all()]} for ws in social_ws],
    }
    return JsonResponse(res, safe=False)
