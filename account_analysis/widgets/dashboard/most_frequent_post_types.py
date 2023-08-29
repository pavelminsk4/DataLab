from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.http import JsonResponse


def most_frequent_post_types(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    res = post_aggregator_most_frequent_post_types(posts)
    return JsonResponse(res, safe=False)


def post_aggregator_most_frequent_post_types(posts):
    count_tweets, count_replies, count_retweets = 0, 0, 0
    for post in posts:
        if 'original' in post.type:
            count_tweets += 1
        if 'reply' in post.type:
            count_replies += 1
        if 'retweet' in post.type:
            count_retweets += 1
    return {'count_tweets': count_tweets,
            'count_replies': count_replies,
            'count_retweets': count_retweets}
