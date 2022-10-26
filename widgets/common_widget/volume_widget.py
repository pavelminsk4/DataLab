from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from project.models import Project, Post
from django.db.models import Q
from functools import reduce
from django.db.models.functions import Trunc
from django.db.models import Count
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

def posts_agregator(project):
  project = get_object_or_404(Project, pk = project.pk)
  posts = data_range_posts(project.start_search_date, project.end_search_date)
  posts = keywords_posts(project.keywords, posts)
  if project.additional_keywords!=[]:
    posts = additional_keywords_posts(posts, project.additional_keywords)
  else:
    posts = keywords_posts(project.keywords, posts)
  if project.ignore_keywords!=[]:
    posts = exclude_keywords_posts(posts, project.ignore_keywords)
  return posts

def volume(request, pk):
  project = get_object_or_404(Project, pk=pk)
  posts = posts_agregator(project)
  #smpl_freq = request.smpl_freq
  #smpl_freq = 'day'
  #smpl_freq = 'week'
  #smpl_freq = 'quarter'
  #smpl_freq = 'month'
  #smpl_freq = 'year'
  smpl_freq = json.loads(request.body)
  posts_per_smpl_freq = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date")
  res = list(posts_per_smpl_freq)
  return JsonResponse(res, safe = False)
