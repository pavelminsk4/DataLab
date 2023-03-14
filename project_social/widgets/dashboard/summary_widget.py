from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.http import JsonResponse
from django.db.models import Q
from functools import reduce

def calculate_summary_widget(posts):
  posts_quantity = posts.count()
  authors_quantity = posts.values('user_name').distinct().count()
  countries_quantity = posts.values('locationString').distinct().count()
  languages_quantity = posts.values('language').distinct().count()
  pos_posts = posts.filter(sentiment_vote='positive').count()
  neg_posts = posts.filter(sentiment_vote='negative').count()
  neut_posts = posts_quantity - pos_posts - neg_posts
  likes_quantity = reduce(lambda x, y: x + y, [x['count_favorites'] for x in posts.values('count_favorites')], 0)
  replies_quantity = reduce(lambda x, y: x + y, [x['count_replies'] for x in posts.values('count_replies')], 0)
  retweets_quantity = reduce(lambda x, y: x + y, [x['count_retweets'] for x in posts.values('count_retweets')], 0)
  
  return {
    'posts':posts_quantity,
    'sources':1,
    'authors':authors_quantity,
    'countries':countries_quantity,
    'languages':languages_quantity,
    'pos':pos_posts,
    'neg':neg_posts,
    'neut':neut_posts,
    'likes':likes_quantity,
    'replies':replies_quantity,
    'retweets':retweets_quantity,
    }

def summary(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = calculate_summary_widget(posts)
  return JsonResponse(res, safe=False)
