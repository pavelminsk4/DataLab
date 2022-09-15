from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import UserSerializer, WorkspaceSerializer, ProjectSerializer, WorkspaceCreateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer, Workspace
from django.contrib.auth.models import User
from project.models import Project, Workspace, Post
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt

# ==== User API =======================

class UserList(ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserCreate(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserUpdate(UpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDelete(DestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
class LoggedInUserView(APIView):
  def get(self, request):
    serializer = UserSerializer(self.request.user)
    return Response(serializer.data)

# === Project API ====================

class ListProjectAPIView(ListAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

class CreateProjectAPIView(CreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

class UpdateProjectAPIView(UpdateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

class DeleteProjectAPIView(DestroyAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

# === Workspace API ===========

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

# === Search API =====

#@csrf_exempt
def search(request):
  key = request.POST.get("fname")
  print("------->key")
  print(key)
  print("------<")
  posts = Post.objects.filter(entry_title__contains=key).values('entry_title')
  posts_list=list(posts)
  return JsonResponse(posts_list,safe = False)
