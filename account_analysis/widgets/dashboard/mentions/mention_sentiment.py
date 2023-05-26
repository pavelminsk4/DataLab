from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse


def mention_sentiment(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    posts = posts.filter(text__icontains=f'@{project.profile_handle}')
    res = {
            'positive': posts.filter(sentiment='positive').count(),
            'negative': posts.filter(sentiment='negative').count(),
            'neutral': posts.filter(sentiment='neutral').count()
          }
    return JsonResponse(res, safe=False)
