from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from project.models import Project
from api.serializers import ProjectSerializer

from talkwalker.classes.livestream import Livestream
from talkwalker.classes.asker import Asker

from django_celery_beat.models import PeriodicTask, CrontabSchedule

import environ
import json

env = environ.Env()
ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def collect_data(self, id):
        Asker(id, 'Project').run()
        Livestream(id, 'Project').create()

        schedule = CrontabSchedule.objects.create(
            minute='*/20',
            hour='*',
            day_of_week='*',
            day_of_month='*',
        )

        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'LiveSearch_project_{id}',
            task='talkwalker.tasks.livesearch_sender',
            args=json.dumps([id, 'Project']),
        )

    def create(self, request, *args, **kwargs):
        project = Project.objects.create(**request.data)

        if ALLOWED_HOSTS[0] != 'localhost':
            self.collect_data(project.id)

        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
