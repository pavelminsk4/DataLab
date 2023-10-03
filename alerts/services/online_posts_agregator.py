from django.shortcuts import get_object_or_404
from common.post_locator import PostLocator
from project.models import Project
from django.db.models import Q
from functools import reduce

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

def posts_agregator(project_id):
  project = get_object_or_404(Project, pk = project_id)
  posts = PostLocator().post.objects.all()
  posts = keywords_posts(project.keywords, posts)
  if project.additional_keywords!=[]:
    posts = additional_keywords_posts(posts, project.additional_keywords)
  if project.ignore_keywords!=[]:
    posts = exclude_keywords_posts(posts, project.ignore_keywords)
  if project.country_filter!=None:
    posts = posts.filter(feedlink__country=project.country_filter)
  if project.language_filter!=None:
    posts = posts.filter(feed_language__language=project.language_filter)
  if project.source_filter!=None:
    posts = posts.filter(feedlink__source1=project.source_filter)
  if project.author_filter!=None:
    posts = posts.filter(entry_author=project.author_filter)
  if project.sentiment_filter!=None:
    posts = posts.filter(sentiment=project.sentiment_filter)
  return posts
