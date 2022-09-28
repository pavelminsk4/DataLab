from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import SpeechSerializer, UserSerializer, WorkspaceSerializer, ProjectSerializer, WorkspaceCreateSerializer, CountrySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer, Workspace
from django.contrib.auth.models import User
from project.models import Project, Workspace, Post, Speech, Feedlinks
from django.http import JsonResponse
import json
from django.db.models import Q
from functools import reduce
from  nltk.sentiment import SentimentIntensityAnalyzer
from django.views.decorators.csrf import csrf_exempt
from countries_plus.models import Country

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
def get_string_from_score(sentiments):
  if sentiments['neg'] > sentiments['neu'] and sentiments['neg'] > sentiments['pos']:
      res = 'negative'
  elif sentiments['neu'] > sentiments['pos']:
    res = 'neutral'
  else:
    res = 'positive'
  return res

def add_sentiment_score(posts):
  for post in posts:
    sentiments = SentimentIntensityAnalyzer().polarity_scores(post['entry_title'])
    post['sentiment'] = get_string_from_score(sentiments)
  return posts

def keywords_posts(keys):
  posts = Post.objects.filter(reduce(lambda x,y: x | y, [Q(entry_title__contains=key) for key in keys]))
  return posts

def exclude_keywords_posts(posts, exceptions):
  to_be_removed = []
  for post in posts:
    for word in exceptions:
      if word in post.entry_title:
        to_be_removed.append(post.id)
        break
  posts = posts.exclude(id__in=to_be_removed)
  return posts

def additional_keywords_posts(keys, additions):
  posts = Post.objects.filter(reduce(lambda x,y: x | y, [Q(entry_title__contains=key) for key in keys]))
  for word in additions:
    posts = posts.filter(entry_title__contains=word)
  return posts

#@csrf_exempt
def search(request):
  body = json.loads(request.body)
  keys = body['keywords']
  exceptions = body['exceptions']
  additions = body['additions']
  #country = body['country']
  #language = body['language']
  #sentiment = body['sentiment']
  #date_range = body['date_range']
  if additions!=[]:
    posts = additional_keywords_posts(keys, additions)
  else:
    posts = keywords_posts(keys)
  if exceptions!=[]:
    posts = exclude_keywords_posts(posts, exceptions)
  posts = posts.values('entry_title', 'entry_published', 'entry_summary', 'entry_media_thumbnail_url', 'feed_language__language')
  add_sentiment_score(posts)
  posts_list=list(posts)
  return JsonResponse(posts_list, safe = False)

# === Countries API ==========

class CountriesList(ListAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer

class SpeechesList(ListAPIView):
  queryset = Speech.objects.all().order_by('language')
  serializer_class = SpeechSerializer

# === Sources API ========

def sources(request):
  set = Feedlinks.objects.all().values('source1').distinct()
  sources_list = list(set)
  return JsonResponse(sources_list, safe = False)
