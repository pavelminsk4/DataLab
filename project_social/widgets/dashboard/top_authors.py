from project_social.widgets.project_posts_filter import project_posts_filter
from common.utils.trunc import trunc
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def top_authors(pk, widget_pk):
  res = precalculate_result(pk, widget_pk)
  return JsonResponse(res, safe = False)

def top_authors_report(pk, widget_pk, name_widget):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_top_authors(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'top_authors': model_to_dict(widget)},
        'module_name': 'Social'
    }

def precalculate_result(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return calculate_for_top_authors(posts, widget.aggregation_period, widget.top_counts)

def calculate_for_top_authors(posts, aggregation_period, top_counts):
    results = list(posts.annotate(date_trunc=trunc('date', aggregation_period)).values('user_name').annotate(user_count=Count('user_name')).order_by('-user_count')[:top_counts])
    for res in results:
        if not res['user_name']:
            results.remove(res)
    return results

def to_csv(request, pk, widget_pk):
    result = precalculate_result(pk, widget_pk)
    fields = ['Author', 'Count of posts']
    rows = [[elem['user_name'], elem['user_count']] for elem in result]
    return fields, rows
