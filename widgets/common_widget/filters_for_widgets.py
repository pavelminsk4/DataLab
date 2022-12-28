from project.models import Post
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

def author_filter_posts(author, posts):
  posts = posts.filter(entry_author=author)
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
  if project.author_filter:
    posts = author_filter_posts(project.author_filter, posts)  
  return posts