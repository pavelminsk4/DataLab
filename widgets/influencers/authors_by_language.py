from widgets.common_widget.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def get_authors_by_language(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    results = calculate_authors_by_language(posts, widget.top_counts)
    return JsonResponse(results, safe=False)

def get_authors_by_language_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_authors_by_language(posts, widget.top_counts),
        'widget': {'authors_by_language': model_to_dict(widget)},
        'module_name': 'Online'
    }  

def calculate_authors_by_language(posts, top_counts):
    top_languages = [i['feed_language__language'] for i in posts.values('feed_language__language').annotate(author_count=Count('entry_author', distinct=True)).order_by('-author_count')[:top_counts]]
    results = []
    for language in top_languages:
        top_authors = posts.filter(feed_language__language=language).values('entry_author').annotate(posts_count=Count('id')).order_by('-posts_count')[:top_counts]
        results.append({language: descending_sort({author['entry_author']: author['posts_count'] for author in top_authors})})
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_authors_by_language(posts, widget.top_counts)
    fields = ['Language', 'Author', 'Count of posts']
    rows = []
    for elem in result:
        [rows.append([*elem.keys(), el[0], el[1]]) for el in list(*elem.values())]
    return fields, rows
