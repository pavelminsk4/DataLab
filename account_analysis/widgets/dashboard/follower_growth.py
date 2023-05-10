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
    posts_total = posts.annotate(date_trunc=Trunc('date', aggregation_period)).values('user_followers', 'date_trunc').order_by('date')
    dates = set([str(posts_total[elem]['date_trunc']) for elem in range(len(posts_total))])
    results = [{date: post['user_followers'] for post in posts_total} for date in sorted(list(dates))]
    return results
