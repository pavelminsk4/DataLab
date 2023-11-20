from widgets.common_widget.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def get_sources_by_country(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    results = calculate_sources_by_country(posts, widget.top_counts)
    return JsonResponse(results, safe=False)

def get_sources_by_country_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_sources_by_country(posts, widget.top_counts),
        'widget': {'sources_by_country': model_to_dict(widget)},
        'module_name': 'Online'
    }

def calculate_sources_by_country(posts, top_counts):
    top_countries = [i['feedlink__country'] for i in posts.values('feedlink__country').annotate(source_count=Count('feedlink', distinct=True)).order_by('-source_count')[:top_counts]]
    results =[]
    for country in top_countries:
        top_sources = posts.filter(feedlink__country=country).values('feedlink__source1').annotate(posts_count=Count('id')).order_by('-posts_count')[:top_counts]
        results.append({country: descending_sort({i['feedlink__source1']:i['posts_count'] for i in top_sources})})
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_sources_by_country(posts, widget.top_counts)
    fields = ['Country', 'Source', 'Count of posts']
    rows = []
    for elem in result:
        [rows.append([*elem.keys(), el[0], el[1]]) for el in list(*elem.values())]
    return fields, rows
