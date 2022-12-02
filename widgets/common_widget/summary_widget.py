from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from project.models import Project, Post
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
  posts = Post.objects.only('id').filter(entry_published__range=interval)
  return posts

def calculate_summary_widget(pk):
  project = get_object_or_404(Project, pk = pk)
  posts = data_range_posts(project.start_search_date, project.end_search_date)
  posts = keywords_posts(project.keywords, posts)
  if project.additional_keywords!=[]:
    posts = additional_keywords_posts(posts, project.additional_keywords)
  else:
    posts = keywords_posts(project.keywords, posts)
  if project.ignore_keywords!=[]:
    posts = exclude_keywords_posts(posts, project.ignore_keywords)
  author_dim_pivot = project.widgets_list_2.summary_widget.author_dim_pivot
  country_dim_pivot = project.widgets_list_2.summary_widget.country_dim_pivot
  language_dim_pivot = project.widgets_list_2.summary_widget.language_dim_pivot
  source_dim_pivot = project.widgets_list_2.summary_widget.source_dim_pivot
  sentiment_dim_pivot =project.widgets_list_2.summary_widget.sentiment_dim_pivot
  if author_dim_pivot!=None:
   posts = posts.filter(entry_author=author_dim_pivot)
  if country_dim_pivot!=None:
   posts = posts.filter(feedlink__country=country_dim_pivot)
  if language_dim_pivot!=None:
   posts = posts.filter(feed_language__language=language_dim_pivot)
  if source_dim_pivot!=None:
   posts = posts.filter(feedlink__source1=source_dim_pivot)
  if sentiment_dim_pivot!=None:
   posts = posts.filter(sentiment=sentiment_dim_pivot)
  posts_quantity = posts.count()
  sources_quantity = posts.values('feedlink__source1').distinct().count()
  authors_quantity = posts.values('entry_author').distinct().count()
  countries_quantity = posts.values('feedlink__country').distinct().count()
  languages_quantity = posts.values('feed_language').distinct().count()
  pos_posts = posts.filter(sentiment='positive').count()
  neg_posts = posts.filter(sentiment='negative').count()
  neut_posts = posts_quantity - pos_posts - neg_posts
  potential_reach = posts.order_by('-feedlink__alexaglobalrank')[0].feedlink.alexaglobalrank
  return {
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

def summary_widget(pk):
  res = calculate_summary_widget(pk)
  return JsonResponse(res, safe=False)
