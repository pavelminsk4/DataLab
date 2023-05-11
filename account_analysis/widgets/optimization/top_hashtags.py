from account_analysis.widgets.filter_for_posts import posts_aggregator
from account_analysis.models import ProjectAccountAnalysis, AccountAnalysisWidgetDescription
from django.db.models import Sum, F, Q
from django.http import JsonResponse


def top_hashtags(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    posts = posts.filter(count_hashtags__gte=1).annotate(engagement=Sum(F('count_favorites') + F('count_retweets'))).values('engagement', 'hashtags').order_by('-engagement')
    hashtags = set()
    for p in posts:
        for h in p['hashtags']:
            hashtags.add(h)
    results = {hashtag: 0 for hashtag in hashtags}
    for p in posts:
        for h in p['hashtags']:
            results[h] += p['engagement']        
    results = sorted(results.items(), reverse=True)[:widget.top_counts]
    return JsonResponse(results, safe=False)
