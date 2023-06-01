from account_analysis.models import ProjectAccountAnalysis, AccountAnalysisWidgetDescription
from account_analysis.widgets.filter_for_posts import posts_aggregator
from django.db.models import Sum, F
from django.http import JsonResponse

def top_mentions_by_engagements(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    posts = posts.filter(text__icontains=f'@{project.profile_handle}')
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    top_posts = posts.annotate(engagement=Sum(F('count_favorites') + F('count_retweets'))).order_by('-engagement')[:widget.top_counts]
    results = []
    for elem in top_posts:
        res = {}
        res['alias'] = elem.user_alias
        res['engagement'] = elem.count_favorites + elem.count_retweets
        res['date'] = elem.date.strftime('%b %d, %Y %I:%M %p')
        res['name'] = elem.user_name
        res['likes'] = elem.count_favorites
        res['text'] = elem.text
        res['picture'] = elem.user_picture
        res['retweets'] = elem.count_retweets
        res['sentiment'] = elem.sentiment
        results.append(res)
    return JsonResponse(results, safe=False)
