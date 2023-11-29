from account_analysis.models import AccountAnalysisWidgetDescription
from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Sum, F
from django.http import JsonResponse

def top_posts_by_engagements(pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    top_posts = posts.annotate(engagement=Sum(F('count_favorites') + F('count_totalretweets'))).order_by('-engagement')[:widget.top_counts]
    results = []
    for elem in top_posts:
        res = {}
        res['id'] = elem.post_id
        res['alias'] = elem.user_alias
        res['type'] = ('retweet') if ('retweet') in elem.type else (('reply') if ('reply') in elem.type else 'text')
        res['text'] = elem.text
        res['sentiment'] = elem.sentiment
        res['engagements'] = elem.count_favorites + elem.count_totalretweets
        res['engmt_rate'] = ((elem.count_favorites + elem.count_totalretweets)/elem.user_followers) * 100
        res['date'] = elem.date.strftime('%b %d, %Y %I:%M %p')
        results.append(res)
    return JsonResponse(results, safe=False)
