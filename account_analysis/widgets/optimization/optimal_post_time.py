from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Sum, F
from django.http import JsonResponse

def optimal_post_time(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    return calculation(posts)

def calculation(posts):    
    results = []
    for day_of_week in range(1, 8):
        res = []
        for hour in range(0, 24):
            posts_of_day = posts.filter(date__week_day=day_of_week).filter(date__hour=hour)
            res.append({'engagements': (posts_of_day.aggregate(engagement=Sum(F('count_favorites') + F('count_totalretweets')))['engagement'])/posts_of_day.count() if posts_of_day.count() else 0,
                        'likes': posts_of_day.aggregate(Sum('count_favorites'))['count_favorites__sum'] if posts_of_day.count() else 0,
                        'retweets': posts_of_day.aggregate(Sum('count_totalretweets'))['count_totalretweets__sum'] if posts_of_day.count() else 0,
                        'tweets': posts_of_day.count()})
        results.append(res)
    res = {
           'Saturday': results[6],
           'Friday': results[5],
           'Thursday': results[4],
           'Wednesday': results[3],
           'Tuesday': results[2],
           'Monday': results[1],
           'Sunday': results[0]
           }
    return JsonResponse(res, safe=False)
