from account_analysis.widgets.dashboard.most_frequent_media_types import post_aggregator_most_frequent_media_types
from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from django.http import JsonResponse


def most_frequent_mention_media_types(pk, widget_pk):
    posts, project = filter_for_mentions_posts(pk, widget_pk)
    res = post_aggregator_most_frequent_media_types(posts)
    return JsonResponse(res, safe=False)
