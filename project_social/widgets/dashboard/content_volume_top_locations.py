from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import json

def calculate(posts, aggregation_period, top_counts):
  top_locations = list(map(lambda x: x['locationString'], list(posts.values('locationString').annotate(country_count=Count('locationString')).order_by('-country_count')[:top_counts])))
  results = [{location: list(posts.filter(locationString=location).annotate(date_trunc=Trunc('date', aggregation_period)).values("date_trunc").annotate(created_count=Count('id')).order_by("date"))} for location in top_locations]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_locations[elem]])):
      dates.add(str(results[elem][top_locations[elem]][i]['date_trunc']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      count = 0
      if date in sorted(list({str(results[elem][top_locations[elem]][i]['date_trunc']) for i in range(len(results[elem][top_locations[elem]]))})):
        for i in range(len(results[elem][top_locations[elem]])):
          if date == str(results[elem][top_locations[elem]][i]['date_trunc']):
            count += results[elem][top_locations[elem]][i]['created_count']
        list_dates.append({"date": date, "post_count": count})
      else:
        list_dates.append({"date": date, "post_count": 0})
    res.append({top_locations[elem]: list_dates})
  return res

def content_volume_top_locations(request, pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  body = json.loads(request.body)
  aggregation_period = body['aggregation_period']
  res = calculate(posts, aggregation_period, widget.top_counts)
  return JsonResponse(res, safe = False)

def content_volume_top_locations_report(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return {
        'data': calculate(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'content_volume_top_locations': model_to_dict(widget)}
    }
