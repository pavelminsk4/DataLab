from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from widgets.common_widget.filters_for_widgets import *

def get_authors_by_language(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  top_languages = [i['feed_language__language'] for i in posts.values('feed_language__language').annotate(author_count=Count('entry_author', distinct=True)).order_by('-author_count')[:5]]
  results = []
  for language in top_languages:
    top_authors = posts.filter(feed_language__language=language).values('entry_author').annotate(posts_count=Count('id')).order_by('-posts_count')[:5]
    results.append({language: {author['entry_author']: author['posts_count'] for author in top_authors}})
  return JsonResponse(results, safe = False)
