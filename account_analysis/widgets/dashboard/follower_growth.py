from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from django.db.models.functions import Trunc
from django.db.models import Count, Sum
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse

def follower_growth(request, pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    res = post_aggregator_follower_growth(posts, aggregation_period)
    return JsonResponse(res, safe=False)


def post_aggregator_follower_growth(posts, aggregation_period):
    posts_total = posts.annotate(date_trunc=Trunc('date', aggregation_period)).values('date_trunc').distinct().order_by('date')
    dates = [str(posts_total[elem]['date_trunc']) for elem in range(len(posts_total))]
    results = [{ d: list(posts.filter(date=d))[-1].user_followers} for d in dates]
    return results
