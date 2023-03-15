from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from .widgets.dashboard.content_volume_by_top_locations import *
from .widgets.dashboard.content_volume_by_top_languages import *
from .widgets.dashboard.content_volume_by_top_authors import *
from .widgets.dashboard.sentiment_languages import *
from .widgets.dashboard.sentiment_locations import *
from .widgets.dashboard.sentiment_authors import *
from tweet_binder.models import TweetBinderPost
from .widgets.dashboard.summary_widget import *
from .widgets.dashboard.content_volume import *
from .widgets.dashboard.clipping_feed import *
from .widgets.dashboard.top_locations import *
from .widgets.dashboard.top_languages import *
from .widgets.summary.gender_volume import *
from .widgets.dashboard.top_authors import *
from .widgets.dashboard.sentiment import *
from rest_framework import viewsets, filters
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q
from functools import reduce
from .serializers import *
from .models import *
import json

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

class ProjectsSotialViewSet(viewsets.ModelViewSet):
  queryset = ProjectSocial.objects.all()
  serializer_class = ProjectSocialSerializer  

def keywords_posts(keys, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(text__contains=key) for key in keys]))
  return posts

def exclude_keywords_posts(posts, exceptions):
  to_be_removed = []
  for post in posts:
    for word in exceptions:
      if word in post.text:
        to_be_removed.append(post.id)
        break
  posts = posts.exclude(id__in=to_be_removed)
  return posts

def additional_keywords_posts(posts, additions):
  for word in additions:
    posts = posts.filter(text__contains=word)
  return posts

def data_range_posts(start_date, end_date):
  interval = [start_date, end_date]
  posts = TweetBinderPost.objects.filter(creation_date__range=interval)
  return posts

def twitter_posts_search(request):
  body = json.loads(request.body)
  keys = body['keywords']
  exceptions = body['exceptions']
  additions = body['additions']
  country = body['country']
  language = body['language']
  source = body['source']
  author = body['author']
  sentiment = body['sentiment']
  country_dimensions = body['country_dimensions']
  language_dimensions = body['language_dimensions']
  source_dimensions = body['source_dimensions']
  author_dimensions = body['author_dimensions']
  sentiment_dimensions = body['sentiment_dimensions']
  date_range = body['date_range']
  posts_per_page = body['posts_per_page']
  page_number = body['page_number']
  posts = data_range_posts(date_range[0], date_range[1])
  posts = keywords_posts(keys, posts)
  if additions:
    posts = additional_keywords_posts(posts, additions)
  if exceptions:
    posts = exclude_keywords_posts(posts, exceptions)
  if country:
    posts = posts.filter(locationString=country)
  if language:
    posts = posts.filter(language=language)
  if source:
    posts = posts.filter(source=source)
  if author:
    posts = posts.filter(user_name=author)
  if sentiment:
    posts = posts.filter(sentiment_vote=sentiment)
  if country_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(locationString=country) for country in country_dimensions]))
  if language_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(language=language) for language in language_dimensions]))  
  if source_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(source=source) for source in source_dimensions]))  
  if author_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(user_name=author) for author in author_dimensions]))
  if sentiment_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(sentiment_vote=sentiment) for sentiment in sentiment_dimensions]))    
  posts = posts.values(
    'id',
    'post_id',
    'user_name',
    'user_alias',
    'text',
    'sentiment_vote',
    'creation_date',
    'locationString',
    'language',
    'count_favorites',
    'count_retweets',
    'count_replies',
    )

  p = Paginator(posts, posts_per_page)
  posts_list=list(p.page(page_number))
  res = { 'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list }
  return JsonResponse(res, safe = False)

#=========Social Widgets=======
def social_summary_widget(request, pk, widget_pk):
  return summary(pk, widget_pk)

def clipping_feed_content(request, pk, widget_pk):
  return clipping_feed(pk, widget_pk)

def social_top_locations(request, pk, widget_pk):
  return top_locations(pk, widget_pk)

def social_top_languages(request, pk, widget_pk):
  return top_languages(pk, widget_pk)

def social_top_authors(request, pk, widget_pk):
  return top_authors(pk, widget_pk)

def social_content_volume(request, pk, widget_pk):
  return content_volume(pk, widget_pk)

def social_content_volume_by_top_locations(request, pk, widget_pk):
  return content_volume_by_top_locations(pk, widget_pk)

def social_content_volume_by_top_authors(request, pk, widget_pk):
  return content_volume_by_top_authors(pk, widget_pk)

def social_content_volume_by_top_languages(request, pk, widget_pk):
  return content_volume_by_top_languages(pk, widget_pk)

def social_sentiment(request, pk, widget_pk):
  return sentiment(pk, widget_pk)

def social_sentiment_authors(request, pk, widget_pk):
  return sentiment_authors(pk, widget_pk)

def social_sentiment_languages(request, pk, widget_pk):
  return sentiment_languages(pk, widget_pk)

def social_sentiment_locations(request, pk, widget_pk):
  return sentiment_locations(pk, widget_pk)

def social_gender_volume(request, pk, widget_pk):
  return gender_volume(pk, widget_pk)

class ProjectSocialWidgetsAPIView(RetrieveAPIView):
 serializer_class = WidgetsListSerializer
 
 def get_object(self):
   return SocialWidgetsList.objects.get(project_id=self.kwargs['pk'])

class UpdateSocialProjectsWidgetsAPIView(UpdateAPIView):
  serializer_class = WidgetsListSerializer

  def get_object(self):
    return SocialWidgetsList.objects.get(project_id=self.kwargs['pk'])
  
class SocialAuthorList(ListAPIView):
  serializer_class = TweetBinderPostAuthorSerializer
  queryset = TweetBinderPost.objects.distinct('user_name')
  filter_backends = [filters.SearchFilter]
  search_fields = ['^user_name']

class SocialLocationList(ListAPIView):
  serializer_class = TweetBinderPostLocationSerializer
  queryset = TweetBinderPost.objects.distinct('locationString')
  filter_backends = [filters.SearchFilter]
  search_fields = ['^locationString']

class SocialLanguageList(ListAPIView):
  serializer_class = TweetBinderPostLanguageSerializer
  queryset = TweetBinderPost.objects.distinct('language')
  filter_backends = [filters.SearchFilter]
  search_fields = ['^language']
