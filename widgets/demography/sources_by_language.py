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
  posts = list(posts.values('feed_language__language').annotate(source_count=Count('feedlink', distinct=True)).order_by('-source_count')[:widget.top_counts])
  return JsonResponse(posts, safe = False)
