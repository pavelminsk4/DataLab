from django.shortcuts import get_object_or_404
from project.models import Post, Project
from django.http import JsonResponse
from django.db.models import Count, Q
from functools import reduce
from django.db.models.functions import Trunc
import json
import pandas as pd
from datetime import datetime

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

def author_filter_posts(author, posts):
  posts = posts.filter(entry_author=author)
  return posts

def language_filter_posts(language, posts):
  posts = posts.filter(feed_language__language=language)
  return posts  

def country_filter_posts(country, posts):
  posts = posts.filter(feedlink__country=country)
  return posts  

def source_filter_posts(source, posts):
  posts = posts.filter(feedlink__source1=source)
  return posts  

def posts_agregator(project):
  posts = data_range_posts(project.start_search_date, project.end_search_date)
  posts = keywords_posts(project.keywords, posts)
  if project.additional_keywords!=[]:
    posts = additional_keywords_posts(posts, project.additional_keywords)
  else:
    posts = keywords_posts(project.keywords, posts)
  if project.ignore_keywords!=[]:
    posts = exclude_keywords_posts(posts, project.ignore_keywords)
  if project.author_filter:
    posts = author_filter_posts(project.author_filter, posts)
  if project.language_filter:
    posts = language_filter_posts(project.language_filter, posts)
  if project.country_filter:
    posts = country_filter_posts(project.country_filter, posts)
  if project.source_filter:
    posts = country_filter_posts(project.source_filter, posts)  
  return posts
  
def sentiment_for_period(pk):
  project = Project.objects.get(id=pk)
  posts = posts_agregator(project)
  dates = list(posts.annotate(date=Trunc('entry_published', 'day')).values("date"))
  negative_posts = posts.annotate(date=Trunc('entry_published', 'day')).values("date").filter(sentiment='negative').annotate(count_negative=Count('sentiment')).order_by("date")
  neutral_posts = posts.annotate(date=Trunc('entry_published', 'day')).values("date").filter(sentiment='neutral').annotate(count_neutral=Count('sentiment')).order_by("date")
  positive_posts = posts.annotate(date=Trunc('entry_published', 'day')).values("date").filter(sentiment='positive').annotate(count_positive=Count('sentiment')).order_by("date")
  post_by_sentiment = list(negative_posts) + list(neutral_posts) + list(positive_posts)
  results = []
  for date in sorted(list(set(d['date'] for d in post_by_sentiment))):
    negative, neutral, positive = 0, 0, 0
    for count_post in post_by_sentiment:
      if date == count_post['date']:
        negative += (count_post.get("count_negative") if count_post.get("count_negative") else 0)
        neutral += (count_post.get("count_neutral") if count_post.get("count_neutral") else 0)
        positive += (count_post.get("count_positive") if count_post.get("count_positive") else 0)
    results.append({str(date): {"negative": negative, "neutral": neutral, "positive": positive}})   
  return JsonResponse(results, safe = False)  
