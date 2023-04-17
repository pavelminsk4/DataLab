from project_social.models import SocialWidgetDescription
from project_social.models import ProjectSocial
from django.core.paginator import Paginator
from django.http import JsonResponse
from .filters_for_widgets import *
import json

def interactive_widgets(request, project_pk, widget_pk):
  project = ProjectSocial.objects.get(id=project_pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  body = json.loads(request.body)
  posts_per_page = body['posts_per_page']
  page_number = body['page_number']
  if widget.default_title == 'Top languages':
    posts = language_filter_posts([body['data']], posts)
  elif widget.default_title == 'Top locations':
    posts = country_filter_posts([body['data']], posts)
  elif widget.default_title == 'Top authors':
    posts = author_filter_posts([body['data']], posts)
  elif widget.default_title == 'Social sentiment locations':
    posts = sentiment_filter_posts([body['data']], posts)
    posts = country_filter_posts([body['value']], posts)
  elif widget.default_title == 'Social sentiment authors':
    posts = sentiment_filter_posts([body['data']], posts)
    posts = author_filter_posts([body['value']], posts)
  elif widget.default_title == 'Social sentiment locations':
    posts = sentiment_filter_posts([body['data']], posts)
    posts = country_filter_posts([body['value']], posts)
  elif widget.default_title == 'Content volume by top authors':
    posts = author_dimensions_posts([body['data']], posts).filter(creation_date__range=body['dates'])
  elif widget.default_title == "Content volume by top locations":
    posts = country_dimensions_posts([body['data']], posts).filter(creation_date__range=body['dates'])
  elif widget.default_title == "Content volume by top languages":
    posts = language_dimensions_posts([body['data']], posts).filter(creation_date__range=body['dates'])
  posts = posts.values(
    'id',
    'post_id',
    'user_name',
    'user_alias',
    'text',
    'sentiment',
    'date',
    'locationString',
    'language',
    'count_favorites',
    'count_retweets',
    'count_replies',
    'user_picture',
    'images',
    )
  p = Paginator(posts, posts_per_page)
  posts_list=list(p.page(page_number))
  res = { 'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list }
  return JsonResponse(res, safe = False)
