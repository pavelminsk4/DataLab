from tweet_binder.models import TweetBinderPost
from django.db.models import Q
from functools import reduce

def keyword_posts(profile, posts):
  posts = posts.filter(Q(user_alias__icontains=profile)|Q(text__icontains=f'@{profile}'))
  return posts

def data_range_posts(start_date, end_date):
  interval = [start_date, end_date]
  posts = TweetBinderPost.objects.filter(date__range=interval)
  return posts

def language_filter_posts(languages, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(language=language) for language in languages]))
  return posts  

def country_filter_posts(countries, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(locationString=country) for country in countries]))
  return posts  

def sentiment_filter_posts(sentiments, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(sentiment=sentiment) for sentiment in sentiments]))
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
  return posts
