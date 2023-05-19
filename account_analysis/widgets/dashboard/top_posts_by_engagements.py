from account_analysis.models import ProjectAccountAnalysis, AccountAnalysisWidgetDescription
from account_analysis.widgets.filter_for_posts import posts_aggregator
from django.db.models import Sum, F
from django.http import JsonResponse

def top_posts_by_engagements(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    top_posts = posts.annotate(engagement=Sum(F('count_favorites') + F('count_retweets'))).order_by('-engagement')[:widget.top_counts]
    results = []
    for elem in top_posts:
        res = {}
        res['type'] = ('retweet') if ('retweet') in elem.type else (('reply') if ('reply') in elem.type else 'tweet')
        res['text'] = elem.text
        res['sentiment'] = elem.sentiment
        res['engagement'] = elem.count_favorites + elem.count_retweets
        res['ENGMT Rate'] = (elem.count_favorites + elem.count_retweets)/elem.user_followers
        res['date'] = elem.date.strftime('%b %d, %Y %I:%M %p')
        results.append(res)
    return JsonResponse(results, safe=False)
