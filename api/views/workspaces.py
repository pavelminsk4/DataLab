from project.models import Workspace
from ..serializers import WorkspaceSerializer, WorkspaceCreateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView


class WorkspaceList(ListAPIView):
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return Workspace.objects.filter(members=user)

        return Workspace.objects.none()


class SingleWorkspace(RetrieveAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer


class WorkspaceCreate(CreateAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceCreateSerializer


class WorkspaceUpdate(UpdateAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer


class WorkspaceDelete(DestroyAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
