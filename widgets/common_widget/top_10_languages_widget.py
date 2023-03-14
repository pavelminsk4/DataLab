from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import *

def post_agregator_top_languages(posts, top_counts):
  results = posts.values('feed_language__language').annotate(language_count=Count('feed_language__language')).order_by('-language_count')[:top_counts]
  return list(results)

def top_10_languages(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_top_languages(posts, widget.top_counts)
  return JsonResponse(res, safe = False)
