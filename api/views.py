from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView
from .serializers import SpeechSerializer, UserSerializer, WorkspaceSerializer, ProjectSerializer, WorkspaceCreateSerializer, CountrySerializer, WidgetsListSerializer, ClippingFeedContentWidgetSerializer
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
from dateutil import parser
from django.db.models.functions import ExtractYear
from widgets.models import ClippingFeedContentWidget, WidgetsList
from rest_framework import status

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
def keywords_posts(keys, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(entry_title__contains=key) for key in keys]))
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

def additional_keywords_posts(posts, additions):
  for word in additions:
    posts = posts.filter(entry_title__contains=word)
  return posts

def data_range_posts(start_date, end_date):
  interval = [start_date, end_date]
  posts = Post.objects.filter(entry_published__range=interval)
  return posts

#@csrf_exempt
def search(request):
  body = json.loads(request.body)
  keys = body['keywords']
  exceptions = body['exceptions']
  additions = body['additions']
  country = body['country']
  language = body['language']
  source = body['source']
  author = body['author']
  sentiment = body['sentiment']
  date_range = body['date_range']
  posts = data_range_posts(date_range[0], date_range[1])
  posts = keywords_posts(keys, posts)
  if additions!=[]:
    posts = additional_keywords_posts(posts, additions)
  if exceptions!=[]:
    posts = exclude_keywords_posts(posts, exceptions)
  if country!=[]:
    posts = posts.filter(feedlink__country=country)
  if language!=[]:
    posts = posts.filter(feed_language__language=language)
  if source!=[]:
    posts = posts.filter(feedlink__source1=source)
  if author!=[]:
    posts = posts.filter(entry_author=author)
  if sentiment!=[]:
    posts = posts.filter(sentiment=sentiment)
  posts = posts.values('id', 'entry_title', 'entry_published', 'entry_summary', 'entry_media_thumbnail_url', 'feed_language__language', 'entry_author', 'feedlink__country', 'feedlink__source1', 'sentiment')
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
  set = Feedlinks.objects.all().values('source1').distinct().order_by('source1')
  sources_list = list(set)
  return JsonResponse(sources_list, safe = False)

def authors(request):
  set = Post.objects.all().values('entry_author').distinct().order_by('entry_author')
  authors_list = list(set)
  return JsonResponse(authors_list, safe = False)

def years(request):
  years = Post.objects.annotate(year=ExtractYear('entry_published')).values('year').distinct().order_by('year')
  years_list = list(years)
  return JsonResponse(years_list, safe = False)

# === Widgets =====
#class ProjectWidgetsAPIView(RetrieveAPIView):
#  serializer_class = WidgetsListSerializer
#  
#  def get_object(self):
#    return WidgetsList.objects.get(project_id=self.kwargs['pk'])

def widgets_list(request, pk):
  w = WidgetsList.objects.get(project_id=pk)
  res = {
    'summary_widget':
      {
        'name':'Summary', 'is_active':w.summary_widget
      },
    'volume_widget':
      {
        'name':'Content volume', 'is_active':w.volume_widget
      },
    'clipping_feed_content_widget':
      {
        'name':'Clipping feed content', 'is_active':w.clipping_feed_content_widget
      },
    'top_10_authors_by_volume_widget':
      {
        'name':'Top 10 authors by volume', 'is_active':w.top_10_authors_by_volume_widget
      },
    }
  return JsonResponse(res, safe = False)

class UpdateProjectsWidgetsAPIView(UpdateAPIView):
  serializer_class = WidgetsListSerializer

  def get_object(self):
    return WidgetsList.objects.get(project_id=self.kwargs['pk'])

class ClippingFeedContentWidgetDelete(DestroyAPIView):
  queryset = ClippingFeedContentWidget.objects.all()
  serializes_class = ClippingFeedContentWidgetSerializer

class ClippingFeedContentWidgetCreate(ListCreateAPIView):
  serializer_class = ClippingFeedContentWidgetSerializer
  queryset = ClippingFeedContentWidget.objects.all()

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
