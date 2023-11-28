from project_social.widgets.project_posts_filter import project_posts_filter
from common.social_keywords import get_keywords
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def keywords_by_location(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return JsonResponse(calculate_for_keywords_by_location(posts, widget.top_counts), safe=False)

def keywords_by_location_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_keywords_by_location(posts, widget.top_counts),
        'widget': {'keywords_by_location': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_keywords_by_location(posts, top_counts):
    countries = posts.values('user_location').annotate(count=Count('user_location')).order_by('-count')[:top_counts]
    results = list(map(lambda x: {x['user_location']: get_keywords(posts.filter(user_location=x['user_location']))}, countries))
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_keywords_by_location(posts, widget.top_counts)
    fields = ['Location', 'Keyword', 'Value']
    rows = []
    for elem in result:
        [rows.append([*elem.keys(), el['key'], el['value']]) for el in list(*elem.values())]
    return fields, rows
