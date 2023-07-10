from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.http import JsonResponse
from django.db.models import Sum, F


def most_engaging_post_types(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    res = post_aggregator_most_engaging_post_types(posts)
    return JsonResponse(res, safe=False)


def post_aggregator_most_engaging_post_types(posts):
    count_tweets = posts.filter(type__contains=['original'])
    count_replies = posts.filter(type__contains=['reply'])
    count_retweets = posts.filter(type__contains=['retweet'])
    engagement = Sum(F('count_favorites') + F('count_retweets'))

    return {'tweets_engagement': count_tweets.aggregate(count=engagement)['count'],
            'replies_engagement': count_replies.aggregate(count=engagement)['count'],
            'retweets_engagement': count_retweets.aggregate(count=engagement)['count']
            }
