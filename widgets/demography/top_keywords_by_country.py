
from widgets.common_widget.project_posts_filter import project_posts_filter
from common.online_keywords import get_keywords
from django.http import JsonResponse
from django.db.models import Count


def get_top_keywords_by_country(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    countries = posts.values('feedlink__country').annotate(count=Count('feedlink__country')).order_by('-count')[:5]
    res = list(map(lambda x: {x['feedlink__country']: get_keywords(posts.filter(feedlink__country=x['feedlink__country']))}, countries))
    return JsonResponse(res, safe=False)
