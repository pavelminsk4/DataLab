from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from project.models import Project, User, Workspace
from api.serializers import ProjectSerializer
from api.services.collect_service import CollectService

from celery import shared_task


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @shared_task
    def collect_data(id):
        CollectService().execute(id)

    def create(self, request, *args, **kwargs):
        data         = request.data
        creator_id   = data.pop('creator', None)
        workspace_id = data.pop('workspace', None)

        creator   = User.objects.filter(id=creator_id).first() if creator_id else None
        workspace = Workspace.objects.filter(id=workspace_id).first() if workspace_id else None

        project = Project.objects.create(**data, creator=creator, workspace=workspace, start_date=data['start_search_date'])
        self.collect_data.delay(project.id)

        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
