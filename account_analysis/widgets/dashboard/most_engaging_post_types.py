from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from django.db.models.functions import Trunc
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse
from django.db.models import Sum, F


def most_engaging_post_types(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    res = post_aggregator_most_engaging_post_types(posts)
    return JsonResponse(res, safe=False)


def post_aggregator_most_engaging_post_types(posts):
    count_tweets = posts.filter(type__contains=['original'])
    count_replies = posts.filter(type__contains=['reply'])
    count_retweets = posts.filter(type__contains=['retweet'])
    engagement = Sum(F('count_favorites') + F('count_retweets'))

    return {'count_tweets': count_tweets.count(),
            'tweets_engagement': count_tweets.aggregate(count=engagement)['count'],
            'count_replies': count_replies.count(),
            'replies_engagement': count_replies.aggregate(count=engagement)['count'],
            'count_retweets': count_retweets.count(),
            'retweets_engagement': count_retweets.aggregate(count=engagement)['count']
            }
