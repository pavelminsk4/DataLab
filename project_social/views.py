from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from .models import *
from .serializers import *

# === Social Workspace API ===========

class WorkspaceSocialList(ListAPIView):
  serializer_class = WorkspaceSocialSerializer

  def get_queryset(self):
    user = self.request.user
    if not user.is_anonymous:
      return WorkspaceSocial.objects.filter(members=user)

    return WorkspaceSocial.objects.none()

class WorkspaceSocialCreate(CreateAPIView):
  queryset = WorkspaceSocial.objects.all()
  serializer_class = WorkspaceCreateSerializer

class WorkspaceSocialUpdate(UpdateAPIView):
  queryset = WorkspaceSocial.objects.all()
  serializer_class = WorkspaceSocialSerializer

class WorkspaceSocialDelete(DestroyAPIView):
  queryset = WorkspaceSocial.objects.all()
  serializer_class = WorkspaceSocialSerializer
