from widgets.models import WidgetDescription
from django.http import JsonResponse
from project.models import Project
from widgets.common_widget.filters_for_widgets import *

def number_of_results(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = {
    'positive': posts.filter(sentiment='positive').count(),
    'negative': posts.filter(sentiment='negative').count(),
    'neutral':  posts.filter(sentiment='neutral').count(),
    }
  return JsonResponse(res, safe=False)
