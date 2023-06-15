from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from .widgets.dashboard.content_volume_top_locations import content_volume_top_locations
from .widgets.dashboard.content_volume_top_languages import content_volume_top_languages
from .widgets.filters_for_widgets import post_agregator_with_dimensions, posts_agregator
from .widgets.sentiment.sentiment_number_of_results import sentiment_number_of_results
from .widgets.dashboard.content_volume_top_authors import content_volume_top_authors
from .widgets.sentiment.sentiment_top_keywords import sentiment_top_keywords
from .widgets.demography.top_authors_by_gender import top_authors_by_gender
from .widgets.demography.languages_by_location import languages_by_location
from .widgets.influencers.authors_by_sentiment import authors_by_sentiment
from .widgets.demography.keywords_by_location import keywords_by_location
from .widgets.influencers.top_sharing_sources import top_sharing_sources
from .widgets.influencers.overall_top_authors import overall_top_authors
from .widgets.demography.authors_by_language import authors_by_language
from .widgets.demography.authors_by_location import authors_by_location
from .widgets.dashboard.sentiment_languages import sentiment_languages
from .widgets.dashboard.sentiment_locations import sentiment_locations
from .widgets.sentiment.sentiment_by_gender import sentiment_by_gender
from .widgets.demography.authors_by_gender import authors_by_gender
from .widgets.dashboard.sentiment_authors import sentiment_authors
from .widgets.dimensions_for_widgets import dimensions_for_each
from .widgets.dashboard.content_volume import content_volume
from .widgets.interactive_widgets import interactive_widgets
from .widgets.dashboard.top_locations import top_locations
from .widgets.dashboard.clipping_feed import clipping_feed
from .widgets.dashboard.top_languages import top_languages
from .widgets.summary.gender_volume import gender_volume
from .widgets.dashboard.top_authors import top_authors
from rest_framework import viewsets, filters, generics
from .widgets.summary.top_keywords import top_keywords
from .widgets.dashboard.summary_widget import summary
from .widgets.dashboard.sentiment import sentiment
from .models import ChangingTweetbinderSentiment
from tweet_binder.models import TweetBinderPost
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from functools import reduce
from .serializers import *
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
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(text__contains=key) | Q(user_name__contains=key) | Q(user_alias__contains=key) for key in keys]))
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
  posts = TweetBinderPost.objects.filter(date__range=interval)
  return posts

def change_social_sentiment(request, pk, department_pk,sentiment):
  try:
    updated_values = {'sentiment': sentiment}
    ChangingTweetbinderSentiment.objects.update_or_create(tweet_post_id=pk,department_id=department_pk,defaults=updated_values)
  except:
    return HttpResponse(status=406)
  return HttpResponse(status=201)


def change_tweet_post_sentiment(post, dict_changing):
    if post['id'] in dict_changing:
        new_sentiment = dict_changing[post['id']]
        post['sentiment'] = new_sentiment
    return post


def posts_values(posts):
  return posts.values(
    'id',
    'post_id',
    'user_name',
    'user_alias',
    'text',
    'sentiment',
    'date',
    'locationString',
    'language',
    'count_favorites',
    'count_retweets',
    'count_replies',
    'user_picture',
    'images',
    )


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
  department_id = request.user.user_profile.department
  posts = data_range_posts(date_range[0], date_range[1]).order_by('-creation_date')
  posts = keywords_posts(keys, posts)
  if additions:
    posts = additional_keywords_posts(posts, additions)
  if exceptions:
    posts = exclude_keywords_posts(posts, exceptions)
  if country:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(locationString=c) for c in country]))
  if language:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(language=lan) for lan in language])) 
  if source:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(source=s) for s in source])) 
  if author:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(user_name=a) for a in author]))
  if sentiment:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(sentiment=sen) for sen in sentiment])) 
  if country_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(locationString=country) for country in country_dimensions]))
  if language_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(language=language) for language in language_dimensions]))  
  if source_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(source=source) for source in source_dimensions]))  
  if author_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(user_name=author) for author in author_dimensions]))
  if sentiment_dimensions:
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(sentiment=sentiment) for sentiment in sentiment_dimensions]))    
  posts = posts_values(posts)
  p = Paginator(posts, posts_per_page)
  posts_list=list(p.page(page_number))
  department_changing = ChangingTweetbinderSentiment.objects.filter(department_id=department_id).values()
  dict_changing = {x['tweet_post_id']: x['sentiment'] for x in department_changing}
  for post in posts_list:
    post = change_tweet_post_sentiment(post, dict_changing)
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
  return content_volume(request, pk, widget_pk)

def social_content_volume_top_locations(request, pk, widget_pk):
  return content_volume_top_locations(request, pk, widget_pk)

def social_content_volume_top_authors(request, pk, widget_pk):
  return content_volume_top_authors(request, pk, widget_pk)

def social_content_volume_top_languages(request, pk, widget_pk):
  return content_volume_top_languages(request, pk, widget_pk)

def social_sentiment(request, pk, widget_pk):
  return sentiment(request, pk, widget_pk)

def social_sentiment_authors(request, pk, widget_pk):
  return sentiment_authors(pk, widget_pk)

def social_sentiment_languages(request, pk, widget_pk):
  return sentiment_languages(pk, widget_pk)

def social_sentiment_locations(request, pk, widget_pk):
  return sentiment_locations(pk, widget_pk)

def social_gender_volume(request, pk, widget_pk):
  return gender_volume(request, pk, widget_pk)

def social_sentiment_by_gender(request, pk, widget_pk):
  return sentiment_by_gender(pk, widget_pk)

def social_top_keywords(request, pk, widget_pk):
  return top_keywords(pk, widget_pk)

def social_top_sharing_sources(request, pk, widget_pk):
  return top_sharing_sources(pk, widget_pk)

def social_sentiment_top_keywords(request, pk, widget_pk):
  return sentiment_top_keywords(pk, widget_pk)

def social_sentiment_number_of_results(request, pk, widget_pk):
  return sentiment_number_of_results(pk, widget_pk)

def social_sentiment_diagram(request, pk, widget_pk):
  return sentiment_number_of_results(pk, widget_pk)

def social_overall_top_authors(request, pk, widget_pk):
  return overall_top_authors(pk, widget_pk)

def social_top_authors_by_gender(request, pk, widget_pk):
  return top_authors_by_gender(pk, widget_pk)

def social_authors_by_language(request, pk, widget_pk):
  return authors_by_language(pk, widget_pk)

def social_authors_by_location(request, pk, widget_pk):
  return authors_by_location(pk, widget_pk)

def social_authors_by_sentiment(request, pk, widget_pk):
  return authors_by_sentiment(pk, widget_pk)

def dimensions_for_each_widgets(request, project_pk, widget_pk):
  return dimensions_for_each(request, widget_pk)

def social_authors_by_gender(request, pk, widget_pk):
  return authors_by_gender(pk, widget_pk)

def social_keywords_by_location(request, pk, widget_pk):
  return keywords_by_location(pk, widget_pk)

def social_languages_by_location(request, pk, widget_pk):
  return languages_by_location(pk, widget_pk)

def interactive_data_for_widgets(request, project_pk, widget_pk):
  return interactive_widgets(request, project_pk, widget_pk)

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
  queryset = TweetBinderPost.objects.distinct('user_alias')
  filter_backends = [filters.SearchFilter]
  search_fields = ['^user_alias']

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

class SocialClippingWidgetDelete(DestroyAPIView):
  serializes_class = SocialClippingWidgetSerializer

  def get_object(self):
    return SocialClippingWidget.objects.filter(post_id=self.kwargs['post_pk'], project_id=self.kwargs['project_pk'])

class SocialClippingWidget(viewsets.ModelViewSet):
  serializer_class = SocialClippingWidgetSerializer
  queryset = SocialClippingWidget.objects.all()

class ListAuthorsInProject(generics.ListAPIView):
  serializer_class = TweetBinderPostAuthorSerializer

  def get_queryset(self):
    pk = self.kwargs.get('pk', None)
    project = get_object_or_404(ProjectSocial, pk=pk)
    posts = posts_agregator(project)
    queryset = posts.values('user_alias').order_by('user_alias').distinct()
    return queryset

class ListLanguagesInProject(generics.ListAPIView):
  serializer_class = TweetBinderPostLanguageSerializer

  def get_queryset(self):
    pk = self.kwargs.get('pk', None)
    project = get_object_or_404(ProjectSocial, pk=pk)
    posts = posts_agregator(project)
    queryset = posts.values('language').order_by('language').distinct()
    return queryset

class ListLocationsInProject(generics.ListAPIView):
  serializer_class = TweetBinderPostLocationSerializer
  
  def get_queryset(self):
    pk = self.kwargs.get('pk', None)
    project = get_object_or_404(ProjectSocial, pk=pk)
    posts = posts_agregator(project)
    queryset = posts.values('locationString').order_by('locationString').distinct()
    return queryset

def project_posts(request, pk):
  body = json.loads(request.body)
  posts_per_page = body['posts_per_page']
  page_number = body['page_number']
  dep_id = body['department_id']
  posts = post_agregator_with_dimensions(ProjectSocial.objects.get(id=pk)).order_by('-creation_date')
  posts = posts_values(posts)
  p = Paginator(posts, posts_per_page)
  posts_list = list(p.page(page_number))
  department_changing = ChangingTweetbinderSentiment.objects.filter(department_id=dep_id).values()
  dict_changing = {x['tweet_post_id']: x['sentiment'] for x in department_changing}
  for post in posts_list:
    post = change_tweet_post_sentiment(post, dict_changing)
  res = { 'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list }
  return JsonResponse(res, safe = False)
