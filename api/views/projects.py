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
            start_date=data['start_search_date'],
            sources=data['sources'] or [environ.Env()('DEFAULT_SOURCE')]
        )
        self.collect_data.delay(project.id)

        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        data = request.data
        
        if data['recollect']:
            project                     = Project.objects.get(pk=data['project_pk'])
            project.keywords            = data['keywords']
            project.start_date          = data['start_date']
            project.start_search_date   = data['start_search_date']
            project.additional_keywords = data['additional_keywords']
            project.ignore_keywords     = data['ignore_keywords']
            project.author_filter       = data['author_filter']
            project.language_filter     = data['language_filter']
            project.country_filter      = data['country_filter']
            project.source_filter       = data['source_filter']
            project.sentiment_filter    = data['sentiment_filter']
            project.status              = Project.STATUS_COLLECTING
            project.posts.all().delete()
            project.save(update_fields=['keywords', 'start_date', 'start_search_date', 'additional_keywords', 'ignore_keywords',
                'author_filter', 'language_filter', 'country_filter', 'source_filter', 'sentiment_filter', 'status'])
            
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
