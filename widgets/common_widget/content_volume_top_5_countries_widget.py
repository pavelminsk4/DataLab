from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import Trunc
import json
from .filters_for_widgets import *

def agregator_results_content_volume_top_countries(posts, smpl_freq):
  top_countries = list(map(lambda x: x['feedlink__country'], list(posts.values('feedlink__country').annotate(country_count=Count('feedlink__country')).order_by('-country_count')[:5])))
  results = [{country: list(posts.filter(feedlink__country=country).annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date"))} for country in top_countries]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_countries[elem]])):
      dates.add(str(results[elem][top_countries[elem]][i]['date']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      if date in sorted(list({str(results[elem][top_countries[elem]][i]['date']) for i in range(len(results[elem][top_countries[elem]]))})):
        for i in range(len(results[elem][top_countries[elem]])):
          if date == str(results[elem][top_countries[elem]][i]['date']):
            list_dates.append({"date": date, "post_count": results[elem][top_countries[elem]][i]['created_count']})
      else:
        list_dates.append({"date": date, "post_count": 0})
    res.append({top_countries[elem]: list_dates})
  return res

def content_volume_top_5_countries(request, pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  smpl_freq = widget.aggregation_period
  res = agregator_results_content_volume_top_countries(posts, smpl_freq)
  return JsonResponse(res, safe = False)
