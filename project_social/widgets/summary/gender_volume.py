from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import json


def gender_volume(request, pk, widget_pk):
  posts, widget = project_posts_filter(pk, widget_pk)
  body = json.loads(request.body)
  aggregation_period = body['aggregation_period']
  res = calculate_for_gender_volume(posts, aggregation_period, widget.top_counts)
  return JsonResponse(res, safe = False)

def gender_volume_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_gender_volume(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'gender_volume': model_to_dict(widget)}
    }

def calculate_for_gender_volume(posts, aggregation_period, top_counts):
  top_authors = list(map(lambda x: x['user_gender'], list(posts.values('user_gender').annotate(count=Count('user_gender')).order_by('-count')[:top_counts])))
  results = [{name: list(posts.filter(user_gender=name).annotate(date_trunk=Trunc('date', aggregation_period)).values("date_trunk").annotate(created_count=Count('id')).order_by("date"))} for name in top_authors]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_authors[elem]])):
      dates.add(str(results[elem][top_authors[elem]][i]['date_trunk']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      count = 0
      if date in sorted(list({str(results[elem][top_authors[elem]][i]['date_trunk']) for i in range(len(results[elem][top_authors[elem]]))})):
        for i in range(len(results[elem][top_authors[elem]])):
          if date == str(results[elem][top_authors[elem]][i]['date_trunk']):
            count += results[elem][top_authors[elem]][i]['created_count']
        list_dates.append({"date": date, "post_count": count})
      else:
        list_dates.append({"date": date, "post_count": 0})
    res.append({top_authors[elem]: list_dates})
  return res
