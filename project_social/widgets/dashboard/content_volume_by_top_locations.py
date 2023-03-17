from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count

def post_agregator_content_volume_top_locations(posts, aggregation_period, top_counts):
  top_locations = list(map(lambda x: x['locationString'], list(posts.values('locationString').annotate(country_count=Count('locationString')).order_by('-country_count')[:top_counts])))
  results = [{location: list(posts.filter(locationString=location).annotate(date=Trunc('creation_date', aggregation_period)).values("creation_date").annotate(created_count=Count('id')).order_by("date"))} for location in top_locations]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_locations[elem]])):
      dates.add(str(results[elem][top_locations[elem]][i]['creation_date']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      if date in sorted(list({str(results[elem][top_locations[elem]][i]['creation_date']) for i in range(len(results[elem][top_locations[elem]]))})):
        for i in range(len(results[elem][top_locations[elem]])):
          if date == str(results[elem][top_locations[elem]][i]['creation_date']):
            list_dates.append({"creation_date": date, "post_count": results[elem][top_locations[elem]][i]['created_count']})
      else:
        list_dates.append({"creation_date": date, "post_count": 0})
    res.append({top_locations[elem]: list_dates})
  return res

def content_volume_by_top_locations(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_content_volume_top_locations(posts, widget.aggregation_period, widget.top_counts)
  return JsonResponse(res, safe = False)