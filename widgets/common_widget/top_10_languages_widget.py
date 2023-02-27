from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import *

def post_agregator_top_languages(posts):
  results = posts.values('feed_language__language').annotate(language_count=Count('feed_language__language')).order_by('-language_count')[:10]
  for i in range(len(results)):
    if (results[i]['feed_language__language'] == None or not results[i]['feed_language__language'] or 'img' in results[i]['feed_language__language'] or results[i]['feed_language__language'] == 'None' or results[i]['feed_language__language'] == 'null' or results[i]['feed_language__language'] == 'Language not specified'):
      results[i]['feed_language__language'] = 'Missing in source'
  return list(results)

def top_10_languages(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_top_languages(posts)
  return JsonResponse(res, safe = False)
