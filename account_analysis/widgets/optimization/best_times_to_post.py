from account_analysis.models import ProjectAccountAnalysis, AccountAnalysisWidgetDescription
from account_analysis.widgets.filter_for_posts import posts_aggregator
from django.db.models import Sum, F
from django.http import JsonResponse

def best_times_to_post(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    results = []
    for day_of_week in range(1, 8):
        for hour in range(0, 24):
            posts_of_day = posts.filter(date__week_day=day_of_week).filter(date__hour=hour)
            results.append({
                        'weekday': posts_of_day.first().date.strftime('%A') if posts_of_day.first() else None,
                        'time': posts_of_day.first().date.strftime('%-I %p') if posts_of_day.first() else None,
                        'engagements': (posts_of_day.aggregate(engagement=Sum(F('count_favorites') + F('count_retweets')))['engagement'])/posts_of_day.count() if posts_of_day.count() else 0,
                        'likes': posts_of_day.aggregate(Sum('count_favorites'))['count_favorites__sum'] if posts_of_day.count() else 0,
                        'retweets': posts_of_day.aggregate(Sum('count_retweets'))['count_retweets__sum'] if posts_of_day.count() else 0,
                        'replies': posts_of_day.aggregate(Sum('count_replies'))['count_replies__sum'] if posts_of_day.count() else 0})
    results = sorted(results, key=lambda engagements: engagements['engagements'], reverse=True)[:widget.top_counts]
    return JsonResponse(results, safe=False)
