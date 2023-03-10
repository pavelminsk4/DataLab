from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import json

def post_agregator_top_locations(posts, top_counts, aggregation_period):
  results = list(posts.annotate(date=Trunc('creation_date', aggregation_period)).values('locationString').annotate(locations_count=Count('locationString')).order_by('-locations_count')[:top_counts])
  for res in results:
    if not res['locationString']:
      results.remove(res)
  return results

def top_locations(request, pk, widget_pk):
  body = json.loads(request.body)
  top_counts = body['top_counts']
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_top_locations(posts, top_counts, widget.aggregation_period)
  return JsonResponse(res, safe = False)
