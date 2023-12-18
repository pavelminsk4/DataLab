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
    countries = posts.values('country').annotate(count=Count('country')).order_by('-count')[:top_counts]
    results = list(map(lambda x: {x['country']: get_keywords(posts.filter(country=x['country']))}, countries))
    return results


def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_keywords_by_location(posts, widget.top_counts)
    fields = ['Location', 'Keyword', 'Value']
    rows = []
    for elem in result:
        [rows.append([*elem.keys(), el['key'], el['value']]) for el in list(*elem.values())]
    return fields, rows
