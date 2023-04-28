from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from django.db.models.functions import Trunc
from django.db.models import Count, Sum
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse


def most_engaging_post_types(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    res = post_aggregator_most_engaging_post_types(posts)
    return JsonResponse(res, safe=False)


def post_aggregator_most_engaging_post_types(posts):
    count_tweets = posts.filter(type__contains=['original']).count()
    count_replies = posts.filter(type__contains=['reply']).count()
    count_retweets = posts.filter(type__contains=['retweet']).count()

    return {'count_tweets': count_tweets,
            'tweets_engagement': posts.filter(type__contains=['original']).aggregate(count=Sum('count_favorites'))['count'] + posts.filter(type__contains=['original']).aggregate(count=Sum('count_retweets'))['count'],
            'count_replies': count_replies,
            'replies_engagement': posts.filter(type__contains=['reply']).aggregate(count=Sum('count_favorites'))['count'] + posts.filter(type__contains=['reply']).aggregate(count=Sum('count_retweets'))['count'],
            'count_retweets': count_retweets,
            'retweets_engagement': posts.filter(type__contains=['retweet']).aggregate(count=Sum('count_favorites'))['count'] + posts.filter(type__contains=['retweet']).aggregate(count=Sum('count_retweets'))['count']
            }
