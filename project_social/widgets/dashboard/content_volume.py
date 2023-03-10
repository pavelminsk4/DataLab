from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import json

def post_agregator_volume(posts, aggregation_period):
  posts = posts.annotate(date=Trunc('creation_date', aggregation_period)).values("creation_date").annotate(created_count=Count('id')).order_by("creation_date")
  return list(posts)

def content_volume(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_volume(posts, widget.aggregation_period)
  return JsonResponse(res, safe = False)
