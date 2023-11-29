from account_analysis.widgets.dashboard.most_frequent_media_types import post_aggregator_most_frequent_media_types
from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from django.http import JsonResponse


def most_frequent_mention_media_types(pk, widget_pk):
    posts, project, widget = filter_for_mentions_posts(pk, widget_pk)
    res = post_aggregator_most_frequent_media_types(posts)
    return JsonResponse(res, safe=False)

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_mentions_posts(pk, widget_pk)
    result = post_aggregator_most_frequent_media_types(posts)
    fields = ['Links', 'Text', 'Video', 'Photo', 'Combination']
    rows = [[result['count_link'], result['count_text'], result['count_video'], result['count_photo'], result['count_combination']]]
    return fields, rows
