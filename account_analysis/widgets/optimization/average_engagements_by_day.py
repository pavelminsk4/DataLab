from account_analysis.models import ProjectAccountAnalysis, AccountAnalysisWidgetDescription
from account_analysis.widgets.filter_for_posts import posts_aggregator
from django.db.models import Sum, F
from django.http import JsonResponse


def average_engagements_by_day(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    return calculate(posts)

def calculate(posts):
    posts_sunday = posts.filter(date__week_day=1).aggregate(engagement=Sum(F('count_favorites') + F('count_retweets')))
    posts_monday = posts.filter(date__week_day=2).aggregate(engagement=Sum(F('count_favorites') + F('count_retweets')))
    posts_tuesday = posts.filter(date__week_day=3).aggregate(engagement=Sum(F('count_favorites') + F('count_retweets')))
    posts_wednesday = posts.filter(date__week_day=4).aggregate(engagement=Sum(F('count_favorites') + F('count_retweets')))
    posts_thursday = posts.filter(date__week_day=5).aggregate(engagement=Sum(F('count_favorites') + F('count_retweets')))
    posts_friday = posts.filter(date__week_day=6).aggregate(engagement=Sum(F('count_favorites') + F('count_retweets')))
    posts_saturday = posts.filter(date__week_day=7).aggregate(engagement=Sum(F('count_favorites') + F('count_retweets')))
    res = {'Monday': posts_monday['engagement'], 
           'Tuesday': posts_tuesday['engagement'],
           'Wednesday': posts_wednesday['engagement'],
           'Thursday': posts_thursday['engagement'],
           'Friday': posts_friday['engagement'],
           'Saturday': posts_saturday['engagement'],
           'Sunday': posts_sunday['engagement']}
    return JsonResponse(res, safe=False)
