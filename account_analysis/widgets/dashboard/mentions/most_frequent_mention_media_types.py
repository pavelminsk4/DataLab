from account_analysis.widgets.dashboard.most_frequent_media_types import post_aggregator_most_frequent_media_types
from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse


def most_frequent_mention_media_types(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    posts = posts.filter(text__icontains=f'@{project.profile_handle}')
    res = post_aggregator_most_frequent_media_types(posts)
    return JsonResponse(res, safe=False)
