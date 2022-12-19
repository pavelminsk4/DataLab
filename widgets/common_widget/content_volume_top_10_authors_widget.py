from django.shortcuts import get_object_or_404
from project.models import Post, Project
from django.http import JsonResponse
from django.db.models import Count, Q
from functools import reduce
from django.db.models.functions import Trunc
import json

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

def source_filter_posts(source, posts):
  posts = posts.filter(feedlink__source1=source)
  return posts  

def language_filter_posts(language, posts):
  posts = posts.filter(feed_language__language=language)
  return posts  

def country_filter_posts(country, posts):
  posts = posts.filter(feedlink__country=country)
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
    posts = source_filter_posts(project.source_filter, posts)
  if project.language_filter:
    posts = language_filter_posts(project.language_filter, posts)
  if project.country_filter:
    posts = country_filter_posts(project.country_filter, posts)
  return posts
  
def content_volume_top_10_authors(request, pk):
  project = Project.objects.get(id=pk)
  posts = posts_agregator(project)
  body = json.loads(request.body)
  smpl_freq = body['smpl_freq']
  top_authors = list(map(lambda x: x['entry_author'], list(posts.values('entry_author').annotate(author_count=Count('entry_author')).order_by('-author_count')[:10])))
  results = [{author: list(posts.filter(entry_author=author).annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date"))} for author in top_authors]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_authors[elem]])):
      dates.add(str(results[elem][top_authors[elem]][i]['date']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      if date in sorted(list({str(results[elem][top_authors[elem]][i]['date']) for i in range(len(results[elem][top_authors[elem]]))})):
        for i in range(len(results[elem][top_authors[elem]])):
          if date == str(results[elem][top_authors[elem]][i]['date']): 
            list_dates.append({"date": date, "post_count": results[elem][top_authors[elem]][i]['created_count']})
      else:
        list_dates.append({"date": date, "post_count": 0})
    res.append({top_authors[elem]: list_dates})    
  return JsonResponse(res, safe = False)
