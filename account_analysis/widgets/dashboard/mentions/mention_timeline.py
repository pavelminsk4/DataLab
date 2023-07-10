from account_analysis.widgets.dashboard.profile_timeline import post_aggregator_profile_timeline
from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from django.http import JsonResponse
import json


def mention_timeline(request, pk, widget_pk):
    posts, project = filter_for_mentions_posts(pk, widget_pk)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    res = post_aggregator_profile_timeline(posts, aggregation_period)
    return JsonResponse(res, safe=False)
