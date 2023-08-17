from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import json


def content_volume_top_countries(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    res = aggregator_results_content_volume_top_countries(posts, aggregation_period, widget.top_counts)
    return JsonResponse(res, safe = False)

def content_volume_top_countries_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': aggregator_results_content_volume_top_countries(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'content_volume_top_countries': model_to_dict(widget)},
        'module_name': 'Online'
    }

def aggregator_results_content_volume_top_countries(posts, aggregation_period, top_counts):
    top_countries = list(map(lambda x: x['feedlink__country'], list(posts.values('feedlink__country').annotate(country_count=Count('feedlink__country')).order_by('-country_count')[:top_counts])))
    results = [{country: list(posts.filter(feedlink__country=country).annotate(date=Trunc('entry_published', aggregation_period)).values("date").annotate(created_count=Count('id')).order_by("date"))} for country in top_countries]
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
