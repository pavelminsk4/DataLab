from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from django.db.models.functions import Trunc
from django.db.models import Count, Sum
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse


def profile_timeline(request, pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    res = post_aggregator_profile_timeline(posts, aggregation_period)
    return JsonResponse(res, safe=False)


def post_aggregator_profile_timeline(posts, aggregation_period):
    posts_total = posts.annotate(date_trunc=Trunc('date', aggregation_period)).values("date_trunc").annotate(created_count=Count('id')).order_by("date")
    posts_favorites = posts.annotate(date_trunc=Trunc('date', aggregation_period)).values("date_trunc").annotate(count_favorites=Sum("count_favorites")).order_by("date")
    posts_retweets = posts.annotate(date_trunc=Trunc('date', aggregation_period)).values("date_trunc").annotate(count_retweets=Sum("count_retweets")).order_by("date")
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
