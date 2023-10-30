from rest_framework import viewsets
from api.serializers import ProjectSerializer
from project.models import Project


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
