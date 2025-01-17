from widgets.common_widget.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def get_sources_by_language(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    results = calculate_sources_by_language(posts, widget.top_counts)
    return JsonResponse(results, safe=False)

def get_sources_by_language_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_sources_by_language(posts, widget.top_counts),
        'widget': {'sources_by_language': model_to_dict(widget)},
        'module_name': 'Online'
    } 

def calculate_sources_by_language(posts, top_counts):
    top_languages = [i['feed_language__language'] for i in posts.values('feed_language__language').annotate(sources_count=Count('feedlink__source1', distinct=True)).order_by('-sources_count')[:top_counts]]
    results = []
    for language in top_languages:
        top_sources = posts.filter(feed_language__language=language).values('feedlink__source1').annotate(posts_count=Count('id')).order_by('-posts_count')[:top_counts]
        results.append({language: descending_sort({source['feedlink__source1']: source['posts_count'] for source in top_sources})})
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_sources_by_language(posts, widget.top_counts)
    fields = ['Language', 'Source', 'Count of posts']
    rows = []
    for elem in result:
        [rows.append([*elem.keys(), el[0], el[1]]) for el in list(*elem.values())]
    return fields, rows
