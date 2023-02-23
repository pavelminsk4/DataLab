from widgets.models import WidgetDescription
from .filters_for_widgets import *
from django.shortcuts import get_object_or_404
from django.db.models.functions import Trunc
from django.http import JsonResponse
from project.models import Project
from django.db.models import Count
import json

def post_agregator_volume(posts, smpl_freq):
  posts_per_smpl_freq = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date")
  return list(posts_per_smpl_freq)

def volume(request, pk, widget_pk):
  project = get_object_or_404(Project, pk=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget)
  body = json.loads(request.body)
  smpl_freq = body['smpl_freq']
  res = post_agregator_volume(posts, smpl_freq)
  return JsonResponse(res, safe = False)
