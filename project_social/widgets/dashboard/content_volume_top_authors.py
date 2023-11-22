from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from common.utils.trunc import trunc
from django.http import JsonResponse
from django.db.models import Count
import json


def content_volume_top_authors(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_for_content_volume_top_authors(posts, widget.aggregation_period, widget.top_counts)
    return JsonResponse(res, safe = False)

def content_volume_top_authors_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_content_volume_top_authors(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'content_volume_top_authors': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_content_volume_top_authors(posts, aggregation_period, top_counts):
    top_authors = list(map(lambda x: x['user_name'], list(posts.values('user_name').annotate(authors_count=Count('user_name')).order_by('-authors_count')[:top_counts])))
    results = [{name: list(posts.filter(user_name=name).annotate(date_trunc=trunc('date', aggregation_period)).values("date_trunc").annotate(created_count=Count('id')).order_by("date"))} for name in top_authors]
    dates = set()
    for elem in range(len(results)):
      for i in range(len(results[elem][top_authors[elem]])):
        dates.add(str(results[elem][top_authors[elem]][i]['date_trunc']))
    res = []
    for elem in range(len(results)):
      list_dates = []
      for date in sorted(list(dates)):
        count = 0
        if date in sorted(list({str(results[elem][top_authors[elem]][i]['date_trunc']) for i in range(len(results[elem][top_authors[elem]]))})):
          for i in range(len(results[elem][top_authors[elem]])):
            if date == str(results[elem][top_authors[elem]][i]['date_trunc']):
              count += results[elem][top_authors[elem]][i]['created_count']
          list_dates.append({"date": date, "post_count": count})
        else:
          list_dates.append({"date": date, "post_count": 0})
      res.append({top_authors[elem]: list_dates})
    return res

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_content_volume_top_authors(posts, widget.aggregation_period, widget.top_counts)
    dates = [str(elem['date']) for elem in list(*result[0].values())]
    fields = ['Author'] + dates
    rows = [[*elem.keys()] + [e['post_count'] for e in list(*elem.values())] for elem in result]
    return fields, rows
