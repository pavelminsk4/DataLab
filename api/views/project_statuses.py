from api.services.stop_livestream import stop_livestream
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
        pr = self.get_object()
        data = request.data
        if data.get('status') == 'inactive':
            pr.status = data.get('status')
            pr.save()
            stop_livestream(pr.pk)
            serializer = ProjectSerializer(pr, partial=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
