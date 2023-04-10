from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from widgets.common_widget.filters_for_widgets import *

def get_authors_by_sentiment(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  posts = list(posts.values('sentiment').annotate(author_count=Count('entry_author', distinct=True)).order_by('-author_count')[:widget.top_counts])
  return JsonResponse(posts, safe = False)
