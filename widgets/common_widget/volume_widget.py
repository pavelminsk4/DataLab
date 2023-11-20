from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from common.utils.trunc import trunc
from django.http import JsonResponse
from django.db.models import Count
import json


def volume(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = post_agregator_volume(posts, widget.aggregation_period)
    return JsonResponse(res, safe = False)

def volume_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_agregator_volume(posts, widget.aggregation_period),
        'widget': {'volume': model_to_dict(widget)},
        'module_name': 'Online'
    }  

def post_agregator_volume(posts, aggregation_period):
    posts_per_aggregation_period = posts.annotate(date=trunc('entry_published', aggregation_period)).values("date").annotate(created_count=Count('id')).order_by("date")
    return list(posts_per_aggregation_period)

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = post_agregator_volume(posts, widget.aggregation_period)
    fields = ['Date', 'Count of posts']
    rows = [[elem['date'], elem['created_count']] for elem in result]
    return fields, rows
