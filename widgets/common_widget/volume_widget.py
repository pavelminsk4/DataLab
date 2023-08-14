from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import json


def volume(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    res = post_agregator_volume(posts, aggregation_period)
    return JsonResponse(res, safe = False)

def volume_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_agregator_volume(posts, widget.aggregation_period),
        'widget': {'volume': model_to_dict(widget)},
        'module_name': 'Online'
    }  

def post_agregator_volume(posts, aggregation_period):
    posts_per_aggregation_period = posts.annotate(date=Trunc('entry_published', aggregation_period)).values("date").annotate(created_count=Count('id')).order_by("date")
    return list(posts_per_aggregation_period)
