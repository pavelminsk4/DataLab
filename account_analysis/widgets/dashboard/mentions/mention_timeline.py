from account_analysis.widgets.dashboard.profile_timeline import post_aggregator_profile_timeline
from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse


def mention_timeline(request, pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    posts = posts.filter(text__icontains=f'@{project.profile_handle}')
    res = post_aggregator_profile_timeline(posts, aggregation_period)
    return JsonResponse(res, safe=False)
