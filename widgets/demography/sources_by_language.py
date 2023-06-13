from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from widgets.common_widget.filters_for_widgets import *

def get_sources_by_language(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  top_languages = [i['feed_language__language'] for i in posts.values('feed_language__language').annotate(sources_count=Count('feedlink__source1', distinct=True)).order_by('-sources_count')[:5]]
  results = []
  for language in top_languages:
    top_sources = posts.filter(feed_language__language=language).values('feedlink__source1').annotate(posts_count=Count('id'))[:5]
    results.append({language: dict(reversed({source['feedlink__source1']: source['posts_count'] for source in top_sources}.items()))})
  return JsonResponse(results, safe = False)
