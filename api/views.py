from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import UserSerializer
from .serializers import ProjectSerializer
from django.contrib.auth.models import User
from project.models import Project

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
