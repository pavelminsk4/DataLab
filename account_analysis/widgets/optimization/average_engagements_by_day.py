from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Sum, F
from django.http import JsonResponse


def average_engagements_by_day(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    return calculate(posts)

def calculate(posts):
    posts_sunday = posts.filter(date__week_day=1).aggregate(engagement=Sum(F('count_favorites') + F('count_totalretweets')))
    posts_monday = posts.filter(date__week_day=2).aggregate(engagement=Sum(F('count_favorites') + F('count_totalretweets')))
    posts_tuesday = posts.filter(date__week_day=3).aggregate(engagement=Sum(F('count_favorites') + F('count_totalretweets')))
    posts_wednesday = posts.filter(date__week_day=4).aggregate(engagement=Sum(F('count_favorites') + F('count_totalretweets')))
    posts_thursday = posts.filter(date__week_day=5).aggregate(engagement=Sum(F('count_favorites') + F('count_totalretweets')))
    posts_friday = posts.filter(date__week_day=6).aggregate(engagement=Sum(F('count_favorites') + F('count_totalretweets')))
    posts_saturday = posts.filter(date__week_day=7).aggregate(engagement=Sum(F('count_favorites') + F('count_totalretweets')))
    res = {'Monday': posts_monday['engagement'] / posts.filter(date__week_day=2).count(), 
           'Tuesday': posts_tuesday['engagement'] / posts.filter(date__week_day=3).count(),
           'Wednesday': posts_wednesday['engagement'] / posts.filter(date__week_day=4).count(),
           'Thursday': posts_thursday['engagement'] / posts.filter(date__week_day=5).count(),
           'Friday': posts_friday['engagement'] / posts.filter(date__week_day=6).count(),
           'Saturday': posts_saturday['engagement'] / posts.filter(date__week_day=7).count(),
           'Sunday': posts_sunday['engagement'] / posts.filter(date__week_day=1).count()}
    return JsonResponse(res, safe=False)
