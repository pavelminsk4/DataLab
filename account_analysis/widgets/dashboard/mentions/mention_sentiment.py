from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from django.http import JsonResponse


def mention_sentiment(pk, widget_pk):
    posts, project = filter_for_mentions_posts(pk, widget_pk)
    res = {
            'positive': posts.filter(sentiment='positive').count(),
            'negative': posts.filter(sentiment='negative').count(),
            'neutral': posts.filter(sentiment='neutral').count()
          }
    return JsonResponse(res, safe=False)
