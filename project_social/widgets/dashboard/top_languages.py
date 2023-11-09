from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from common.utils.trunc import trunc
from django.http import JsonResponse
from django.db.models import Count


def top_languages(pk, widget_pk):
    res = precalculate_result(pk, widget_pk)
    return JsonResponse(res, safe=False)

def top_languages_report(pk, widget_pk, name_widget):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_top_languages(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'top_languages': model_to_dict(widget)},
        'module_name': 'Social'
    }

def precalculate_result(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return calculate_for_top_languages(posts, widget.aggregation_period, widget.top_counts)

def calculate_for_top_languages(posts, aggregation_period, top_counts):
    results = list(posts.annotate(date_trunc=trunc('date', aggregation_period)).values(
        'language').annotate(language_count=Count('language')).order_by('-language_count')[:top_counts])
    for res in results:
        if not res['language']:
            results.remove(res)
    return results
