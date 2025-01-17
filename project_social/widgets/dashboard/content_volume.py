from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from common.utils.trunc import trunc
from django.http import JsonResponse
from django.db.models import Count
import json


def content_volume(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_for_content_volume(posts, widget.aggregation_period)
    return JsonResponse(res, safe = False)

def content_volume_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_content_volume(posts, widget.aggregation_period),
        'widget': {'content_volume': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_content_volume(posts, aggregation_period):
    posts = posts.annotate(date_trunc=trunc('date', aggregation_period)).values("date_trunc").annotate(created_count=Count('id')).order_by("date")
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

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_content_volume(posts, widget.aggregation_period)
    fields = ['Date', 'Count of posts']
    rows = [[elem['date'], elem['created_count']] for elem in result]
    return fields, rows
