from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from django.db.models.functions import Trunc
from django.db.models import Count, Sum
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse


def most_frequent_post_types(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    res = post_aggregator_most_frequent_post_types(posts)
    return JsonResponse(res, safe=False)


def post_aggregator_most_frequent_post_types(posts):
    count_tweets = posts.filter(type__contains=['original']).count()
    count_replies = posts.filter(type__contains=['reply']).count()
    count_retweets = posts.filter(type__contains=['retweet']).count()
    return {'count_tweets': count_tweets,
            'count_replies': count_replies,
            'count_retweets': count_retweets}
