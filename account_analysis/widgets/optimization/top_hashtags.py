from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from account_analysis.models import AccountAnalysisWidgetDescription
from django.db.models import Sum, F
from django.http import JsonResponse


def top_hashtags(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    posts = posts.filter(count_hashtags__gte=1).annotate(engagement=Sum(F('count_favorites') + F('count_totalretweets'))).values('engagement', 'hashtags').order_by('-engagement')
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
