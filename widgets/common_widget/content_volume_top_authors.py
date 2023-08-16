from .filters_for_widgets import missing_authors_filter
from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import json


def content_volume_top_authors(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    res = aggregator_results_content_volume_top_authors(posts, aggregation_period, widget.top_counts)
    return JsonResponse(res, safe = False)

def content_volume_top_authors_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': aggregator_results_content_volume_top_authors(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'content_volume_top_authors': model_to_dict(widget)},
        'module_name': 'Online'
    }

def aggregator_results_content_volume_top_authors(posts, aggregation_period, top_counts):
  filtred_posts = missing_authors_filter(posts)
  top_authors = list(map(lambda x: x['entry_author'], list(filtred_posts.values('entry_author').annotate(author_count=Count('entry_author')).order_by('-author_count')[:top_counts])))
  results = [{author: list(filtred_posts.filter(entry_author=author).annotate(date=Trunc('entry_published', aggregation_period)).values("date").annotate(created_count=Count('id')).order_by("date"))} for author in top_authors]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_authors[elem]])):
      dates.add(str(results[elem][top_authors[elem]][i]['date']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      if date in sorted(list({str(results[elem][top_authors[elem]][i]['date']) for i in range(len(results[elem][top_authors[elem]]))})):
        for i in range(len(results[elem][top_authors[elem]])):
          if date == str(results[elem][top_authors[elem]][i]['date']): 
            list_dates.append({"date": date, "post_count": results[elem][top_authors[elem]][i]['created_count']})
      else:
        list_dates.append({"date": date, "post_count": 0})
    res.append({top_authors[elem]: list_dates})
  return res

