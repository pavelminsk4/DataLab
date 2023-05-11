from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import *

def post_agregator_top_countries(posts, top_counts):
  results = posts.values('feedlink__country').annotate(country_count=Count('feedlink__country')).order_by('-country_count')[:top_counts]
  return list(results)

def top_countries(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_top_countries(posts, widget.top_counts)
  return JsonResponse(res, safe = False)
