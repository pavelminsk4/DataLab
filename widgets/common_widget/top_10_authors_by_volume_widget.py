from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import *

def post_agregator_top_auth_by_vol_widget(posts, top_counts):
  results = missing_authors_filter(posts).values('entry_author').annotate(author_posts_count=Count('entry_author')).order_by('-author_posts_count')[:top_counts]
  return list(results)

def top_10_auth_by_vol_widget(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  posts = post_agregator_top_auth_by_vol_widget(posts, widget.top_counts)
  return JsonResponse(posts, safe = False)
