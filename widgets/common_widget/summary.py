from widgets.models import WidgetDescription
from django.http import JsonResponse
from project.models import Project
from .filters_for_widgets import *

def calculate_summary_widget(posts):
  posts_quantity = posts.count()
  sources_quantity = posts.values('feedlink__source1').distinct().count()
  authors_quantity = posts.values('entry_author').distinct().count()
  countries_quantity = posts.values('feedlink__country').distinct().count()
  languages_quantity = posts.values('feed_language').distinct().count()
  pos_posts = posts.filter(sentiment='positive').count()
  neg_posts = posts.filter(sentiment='negative').count()
  neut_posts = posts_quantity - pos_posts - neg_posts
  potential_reach = posts.order_by('-feedlink__alexaglobalrank')[0].feedlink.alexaglobalrank if posts else 0 
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

def summary_widget(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = calculate_summary_widget(posts)
  return JsonResponse(res, safe=False)
