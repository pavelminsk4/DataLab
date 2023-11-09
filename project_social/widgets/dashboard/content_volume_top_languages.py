from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from common.utils.trunc import trunc
from django.http import JsonResponse
from django.db.models import Count
import json


def content_volume_top_languages(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    res = calculate_for_content_volume_top_languages(posts, aggregation_period, widget.top_counts)
    return JsonResponse(res, safe = False)

def content_volume_top_languages_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_content_volume_top_languages(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'content_volume_top_languages': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_content_volume_top_languages(posts, aggregation_period, top_counts):
    top_languages = list(map(lambda x: x['language'], list(posts.values('language').annotate(country_count=Count('language')).order_by('-country_count')[:top_counts])))
    results = [{language: list(posts.filter(language=language).annotate(date_trunc=trunc('date', aggregation_period)).values("date_trunc").annotate(created_count=Count('id')).order_by("date"))} for language in top_languages]
    dates = set()
    for elem in range(len(results)):
      for i in range(len(results[elem][top_languages[elem]])):
        dates.add(str(results[elem][top_languages[elem]][i]['date_trunc']))
    res = []
    for elem in range(len(results)):
      list_dates = []
      for date in sorted(list(dates)):
        count = 0
        if date in sorted(list({str(results[elem][top_languages[elem]][i]['date_trunc']) for i in range(len(results[elem][top_languages[elem]]))})):
          for i in range(len(results[elem][top_languages[elem]])):
            if date == str(results[elem][top_languages[elem]][i]['date_trunc']):
              count += results[elem][top_languages[elem]][i]['created_count']
          list_dates.append({"date": date, "post_count": count})
        else:
          list_dates.append({"date": date, "post_count": 0})
      res.append({top_languages[elem]: list_dates})
    return res
