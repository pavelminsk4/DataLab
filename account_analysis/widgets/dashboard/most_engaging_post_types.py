from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.http import JsonResponse
from django.db.models import Sum, F


def most_engaging_post_types(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    res = post_aggregator_most_engaging_post_types(posts)
    return JsonResponse(res, safe=False)


def post_aggregator_most_engaging_post_types(posts):
    tweets_engagements, replies_engagements, retweets_engagements = 0, 0, 0
    for post in posts:
        if 'original' in post.type:
            tweets_engagements += (post.count_favorites + post.count_totalretweets)
        if 'reply' in post.type:
            replies_engagements += (post.count_favorites + post.count_totalretweets)
        if 'retweet' in post.type:
            retweets_engagements += (post.count_favorites + post.count_totalretweets)
    return {
            'tweets_engagement': tweets_engagements,
            'replies_engagement': replies_engagements,
            'retweets_engagement': retweets_engagements
            }
