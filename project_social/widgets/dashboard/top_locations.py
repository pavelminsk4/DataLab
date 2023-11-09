from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from common.utils.trunc import trunc
from django.http import JsonResponse
from django.db.models import Count


def top_locations(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_for_top_locations(posts, widget.aggregation_period, widget.top_counts)
    return JsonResponse(res, safe = False)

def top_locations_report(pk, widget_pk, name_widget):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_top_locations(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'top_locations': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_top_locations(posts, aggregation_period, top_counts):
    results = list(posts.annotate(date_trunc=trunc('date', aggregation_period)).values('locationString').annotate(locations_count=Count('locationString')).order_by('-locations_count')[:top_counts])
    for res in results:
        if not res['locationString']:
            results.remove(res)
    return results
