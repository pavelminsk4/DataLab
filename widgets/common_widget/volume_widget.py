from widgets.models import WidgetDescription
from .filters_for_widgets import *
from django.shortcuts import get_object_or_404
from django.db.models.functions import Trunc
from django.http import JsonResponse
from project.models import Project
from django.db.models import Count
import json

def post_agregator_volume(posts, aggregation_period):
  posts_per_aggregation_period = posts.annotate(date=Trunc('entry_published', aggregation_period)).values("date").annotate(created_count=Count('id')).order_by("date")
  return list(posts_per_aggregation_period)

def volume(request, pk, widget_pk):
  project = get_object_or_404(Project, pk=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  body = json.loads(request.body)
  aggregation_period = body['aggregation_period']
  res = post_agregator_volume(posts, aggregation_period)
  return JsonResponse(res, safe = False)
