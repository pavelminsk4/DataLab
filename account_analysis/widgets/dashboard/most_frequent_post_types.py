from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.http import JsonResponse


def most_frequent_post_types(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    res = post_aggregator_most_frequent_post_types(posts)
    return JsonResponse(res, safe=False)


def post_aggregator_most_frequent_post_types(posts):
    count_tweets = posts.filter(type__contains=['original']).count()
    count_replies = posts.filter(type__contains=['reply']).count()
    count_retweets = posts.filter(type__contains=['retweet']).count()
    return {'count_tweets': count_tweets,
            'count_replies': count_replies,
            'count_retweets': count_retweets}
