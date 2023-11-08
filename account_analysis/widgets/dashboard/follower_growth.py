from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from common.utils.trunc_function import trunc_function
from django.db.models.functions import Trunc
from django.http import JsonResponse
import json

def follower_growth(request, pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    res = post_aggregator_follower_growth(posts, aggregation_period)
    return JsonResponse(res, safe=False)


def post_aggregator_follower_growth(posts, aggregation_period):
    posts_total = posts.annotate(date_trunc=trunc_function('date', aggregation_period)).values('user_followers', 'date_trunc').order_by('date')
    results = {str(post['date_trunc']): post['user_followers'] for post in posts_total}
    return results
