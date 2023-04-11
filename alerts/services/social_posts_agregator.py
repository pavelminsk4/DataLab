from project_social.models import ProjectSocial
from tweet_binder.models import TweetBinderPost
from django.shortcuts import get_object_or_404
from functools import reduce
from django.db.models import Q

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

def social_posts_agregator(project_id):
  project = get_object_or_404(ProjectSocial, pk = project_id)
  keys = project.keywords
  exceptions = project.ignore_keywords
  additions = project.additional_keywords
  country = project.country_filter
  language = project.language_filter
  source = project.source_filter
  author = project.author_filter
  sentiment = project.sentiment_filter
  country_dimensions = project.country_dimensions
  language_dimensions = project.language_dimensions
  source_dimensions = project.source_dimensions
  author_dimensions = project.author_dimensions
  sentiment_dimensions = project.sentiment_dimensions
  posts = data_range_posts(project.start_search_date, project.end_search_date)
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
    posts = posts.filter(sentiment=sentiment)
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
  return posts
