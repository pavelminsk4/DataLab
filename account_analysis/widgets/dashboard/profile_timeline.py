from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Count, Sum
from common.utils.trunc import trunc
from django.http import JsonResponse
import json


def profile_timeline(request, pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    res = post_aggregator_profile_timeline(posts, widget.aggregation_period)
    return JsonResponse(res, safe=False)


def post_aggregator_profile_timeline(posts, aggregation_period):
    date = trunc('date', aggregation_period)
    posts_total = posts.annotate(date_trunc=date).values("date_trunc").annotate(created_count=Count('id')).order_by("date")
    posts_favorites = posts.annotate(date_trunc=date).values("date_trunc").annotate(count_favorites=Sum("count_favorites")).order_by("date")
    posts_retweets = posts.annotate(date_trunc=date).values("date_trunc").annotate(count_retweets=Sum("count_totalretweets")).order_by("date")
    dates = set()
    for elem in range(len(posts_total)):
        dates.add(str(posts_total[elem]['date_trunc']))
    results = []
    for date in sorted(list(dates)):
        count_post = 0
        count_likes = 0
        count_retweets = 0
        for elem in range(len(posts_total)):
            if date == str(posts_total[elem]['date_trunc']):
                count_post += posts_total[elem]['created_count']
                count_likes += posts_favorites[elem]['count_favorites']
                count_retweets += posts_retweets[elem]['count_retweets']
        results.append({"date": date, "created_count": count_post, "engagement": count_likes +
                       count_retweets, "likes": count_likes, "retweets": count_retweets})
    return results

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    result = post_aggregator_profile_timeline(posts, widget.aggregation_period)
    fields = ['Date', 'Count of posts', 'Engagement', 'Likes', 'Retweets']
    rows = [[elem['date'], elem['created_count'], elem['engagement'], elem['likes'], elem['retweets']] for elem in result]
    return fields, rows
