from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from account_analysis.models import *
from tweet_binder.models import *
from django.db.models import Sum
from django.http import JsonResponse

def mention_summary(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    posts = posts.filter(text__icontains=f'@{project.profile_handle}')
    res = {
        'mention': posts.count(),
        'language': posts.values('language').distinct().count(),
        'countries': posts.values('locationString').distinct().count(),
        'authors': posts.values('user_alias').distinct().count(),
        'neutral': posts.filter(sentiment='neutral').count(),
        'negative': posts.filter(sentiment='negative').count(),
        'positive': posts.filter(sentiment='positive').count(),
        'potential_rates': posts.aggregate(value=Sum('user_value'))['value'],
    }
    return JsonResponse(res, safe=False)
