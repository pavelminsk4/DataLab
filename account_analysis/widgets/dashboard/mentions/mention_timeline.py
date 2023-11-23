from account_analysis.widgets.dashboard.profile_timeline import post_aggregator_profile_timeline
from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from django.http import JsonResponse
import json


def mention_timeline(request, pk, widget_pk):
    posts, project, widget = filter_for_mentions_posts(pk, widget_pk)
    res = post_aggregator_profile_timeline(posts, widget.aggregation_period)
    return JsonResponse(res, safe=False)

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_mentions_posts(pk, widget_pk)
    result = post_aggregator_profile_timeline(posts, widget.aggregation_period)
    fields = ['Date', 'Count of posts', 'Engagement', 'Likes', 'Retweets']
    rows = [[elem['date'], elem['created_count'], elem['engagement'], elem['likes'], elem['retweets']] for elem in result]
    return fields, rows
