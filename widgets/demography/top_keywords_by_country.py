
from widgets.common_widget.project_posts_filter import project_posts_filter
from common.online_keywords import get_keywords
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def get_top_keywords_by_country(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return JsonResponse(calculate_top_keywords_by_country(posts), safe=False)

def get_keywords_by_country_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_top_keywords_by_country(posts),
        'widget': {'top_keywords_by_country': model_to_dict(widget)},
        'module_name': 'Online'
    }

def calculate_top_keywords_by_country(posts):
    countries = posts.values('feedlink__country').annotate(count=Count('feedlink__country')).order_by('-count')[:5]
    results = list(map(lambda x: {x['feedlink__country']: get_keywords(posts.filter(feedlink__country=x['feedlink__country']))}, countries))
    return results
