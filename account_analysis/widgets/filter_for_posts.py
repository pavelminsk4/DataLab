from account_analysis.models import ProjectAccountAnalysis, AccountAnalysisWidgetDescription
from tweet_binder.models import TweetBinderPost
from django.db.models import Q
from functools import reduce

def keyword_posts(profile, posts):
  posts = posts.filter(Q(user_alias__icontains=profile)|Q(text__icontains=f'@{profile}')|Q(user_name__icontains=profile))
  return posts

def data_range_posts(start_date, end_date):
  interval = [start_date, end_date]
  posts = TweetBinderPost.objects.filter(date__range=interval)
  return posts

def language_filter_posts(languages, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(language=language) for language in languages]))
  return posts  

def country_filter_posts(countries, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(user_location=country) for country in countries]))
  return posts  

def sentiment_filter_posts(sentiments, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(sentiment=sentiment) for sentiment in sentiments]))
  return posts

def source_filter_posts(sources, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(source=source) for source in sources]))
  return posts

def author_filter_posts(authors, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(user_name=author) for author in authors]))
  return posts

def language_dimensions_posts(languages, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(language=language) for language in languages]))
  return posts  

def country_dimensions_posts(countries, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(user_location=country) for country in countries]))
  return posts  

def sentiment_dimensions_posts(sentiments, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(sentiment=sentiment) for sentiment in sentiments]))
  return posts

def source_dimensions_posts(sources, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(source=source) for source in sources]))
  return posts

def author_dimensions_posts(authors, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(user_name=author) for author in authors]))
  return posts

def posts_aggregator(project):
  posts = data_range_posts(project.start_search_date, project.end_search_date)
  posts = keyword_posts(project.profile_handle, posts)
  if project.language_filter:
    posts = language_filter_posts(project.language_filter, posts)
  if project.country_filter:
    posts = country_filter_posts(project.country_filter, posts)
  if project.sentiment_filter:
    posts = sentiment_filter_posts(project.sentiment_filter, posts)
  if project.author_filter:
    posts = author_filter_posts(project.author_filter, posts)  
  if project.author_dimensions:
    posts = author_dimensions_posts(project.author_dimensions, posts)
  if project.language_dimensions:
    posts = language_dimensions_posts(project.language_dimensions, posts)
  if project.country_dimensions:
    posts = country_dimensions_posts(project.country_dimensions, posts)
  if project.sentiment_dimensions:
    posts = sentiment_dimensions_posts(project.sentiment_dimensions, posts)    
  return posts

def filter_for_account_posts(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project).filter(user_alias=project.profile_handle)
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    return posts, project, widget

def filter_for_mentions_posts(pk, widget_pk):  
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project).filter(text__icontains=f'@{project.profile_handle}')
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    return posts, project, widget
