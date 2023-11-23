from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from common.utils.trunc import trunc
from django.http import JsonResponse
import json

def follower_growth(request, pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    res = post_aggregator_follower_growth(posts, widget.aggregation_period)
    return JsonResponse(res, safe=False)


def post_aggregator_follower_growth(posts, aggregation_period):
    posts_total = posts.annotate(date_trunc=trunc('date', aggregation_period)).values('user_followers', 'date_trunc').order_by('date')
    results = {str(post['date_trunc']): post['user_followers'] for post in posts_total}
    return results

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    result = post_aggregator_follower_growth(posts, widget.aggregation_period)
    fields = ['Date', 'Followers']
    rows = [[str(elem), result[elem]] for elem in result.keys()]
    return fields, rows
