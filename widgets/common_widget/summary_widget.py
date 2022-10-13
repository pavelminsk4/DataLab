from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from project.models import Project, Post
from django.db.models import Q
from functools import reduce

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


def summary_widget(pk):
  project = get_object_or_404(Project, pk = pk)
  posts = keywords_posts(project.keywords)
  if project.additional_keywords!=[]:
    posts = additional_keywords_posts(project.keywords, project.additional_keywords)
  else:
    posts = keywords_posts(project.keywords)
  if project.ignore_keywords!=[]:
    posts = exclude_keywords_posts(posts, project.ignore_keywords)
  posts_quantity = len(posts)
  sources_quantity = len(posts.values('feedlink__source1').distinct())
  authors_quantity = len(posts.values('entry_author').distinct())
  countries_quantity = len(posts.values('feedlink__country').distinct())
  languages_quantity = len(posts.values('feed_language').distinct())
  pos_posts = len(posts.filter(sentiment='positive'))
  neg_posts = len(posts.filter(sentiment='negative'))
  neut_posts = posts_quantity - pos_posts - neg_posts
  potential_reach = 'blank' 
  res = {
    'posts':posts_quantity,
    'sources':sources_quantity,
    'authors':authors_quantity,
    'countries':countries_quantity,
    'languages':languages_quantity,
    'pos':pos_posts,
    'neg':neg_posts,
    'neut':neut_posts,
    'reach':potential_reach
    }
  return JsonResponse(res, safe=False)
