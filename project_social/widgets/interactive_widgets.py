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
  first_value = body['first_value']
  second_value = body['second_value']
  dates = body['dates']
  if widget.default_title == 'Top languages':
    posts = language_filter_posts(first_value, posts)
  elif widget.default_title == 'Top locations':
    posts = country_filter_posts(first_value, posts)
  elif widget.default_title == 'Top authors':
    posts = author_filter_posts(first_value, posts)
  elif widget.default_title == 'Social sentiment locations':
    posts = sentiment_filter_posts(first_value, posts)
    posts = country_filter_posts(second_value, posts)
  elif widget.default_title == 'Social sentiment authors':
    posts = sentiment_filter_posts(first_value, posts)
    posts = author_filter_posts(second_value, posts)
  elif widget.default_title == 'Social sentiment by gender':
    posts = sentiment_filter_posts(first_value, posts)
    posts = posts.filter(reduce(lambda x,y: x | y, [Q(user_gender=gender) for gender in second_value]))
  elif widget.default_title == 'Social sentiment locations':
    posts = sentiment_filter_posts(first_value, posts)
    posts = country_filter_posts(second_value, posts)
  elif widget.default_title == 'Content volume by top authors':
    posts = author_dimensions_posts(first_value, posts).filter(creation_date__range=dates)
  elif widget.default_title == "Content volume by top locations":
    posts = country_dimensions_posts(first_value, posts).filter(creation_date__range=dates)
  elif widget.default_title == "Content volume by top languages":
    posts = language_dimensions_posts(first_value, posts).filter(creation_date__range=dates)
  elif widget.default_title == "Content volume":
    posts = posts.filter(creation_date__range=dates)
  elif widget.default_title == 'Social sentiment':
    posts = sentiment_filter_posts(first_value, posts).filter(creation_date__range=dates)
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
