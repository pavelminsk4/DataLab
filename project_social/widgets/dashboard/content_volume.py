from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from project_social.models import ProjectSocial
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import json

def calculate(posts, aggregation_period):
  posts = posts.annotate(date_trunc=Trunc('date', aggregation_period)).values("date_trunc").annotate(created_count=Count('id')).order_by("date")
  dates = set()
  for elem in range(len(posts)):
    dates.add(str(posts[elem]['date_trunc']))
  list_dates = []
  for date in sorted(list(dates)):
    count = 0
    for elem in range(len(posts)):
      if date == str(posts[elem]['date_trunc']):
        count += posts[elem]['created_count']
    list_dates.append({"date": date, "created_count": count})
  return list_dates

def content_volume(request, pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  body = json.loads(request.body)
  aggregation_period = body['aggregation_period']
  res = calculate(posts, aggregation_period)
  return JsonResponse(res, safe = False)

def content_volume_report(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return {
        'data': calculate(posts, widget.aggregation_period),
        'widget': {'content_volume_top_locations': model_to_dict(widget)}
    }
