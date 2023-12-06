from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from api.services.collect_service import CollectService
from project.models import Project, User, Workspace
from api.serializers import ProjectSerializer

from celery import shared_task
import environ


def exclude(data, keys):
    return {k: v for k, v in data.items() if k not in keys}


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

        project = Project.objects.create(
            **exclude(data, ['sources']),
            creator=creator,
            workspace=workspace,
            sources=data['sources'] or [environ.Env()('DEFAULT_SOURCE')]
        )
        self.collect_data.delay(project.id)

        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        data = request.data
        
        if data['recollect']:
            Project.objects.filter(id=data['project_pk']).update(
                **exclude(data, ['sort_posts', 'project_pk', 'recollect']),
            )
      
            project = Project.objects.get(id=data['project_pk'])
            project.posts.all().delete()

            self.collect_data.delay(project.id)

            return Response(ProjectSerializer(project).data)
        else:
            partial    = kwargs.pop('partial', False)
            instance   = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
