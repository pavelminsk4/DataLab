from talkwalker.classes.livestream import Livestream
from api.serializers import ProjectSerializer
from project.models import Project

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status


class ProjectStatusesViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    http_method_names = ['patch']

    def get_queryset(self):
        user = self.request.user

        if not user.is_anonymous:
            return Project.objects.filter(creator=user)

    def partial_update(self, request, *args, **kwargs):
        data = request.data
        if data.get('status') != 'inactive':
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        project  = self.get_object()
        project.status = data.get('status')
        project.save()

        Livestream(project.id, 'Project').delete()

        serializer = ProjectSerializer(project, partial=True)
        return Response(serializer.data)
