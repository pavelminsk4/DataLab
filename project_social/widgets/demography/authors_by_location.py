from project_social.widgets.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort 
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def authors_by_location(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return JsonResponse(calculate_for_authors_by_location(posts, widget.top_counts), safe = False)

def authors_by_location_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_authors_by_location(posts, widget.top_counts),
        'widget': {'authors_by_location': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_authors_by_location(posts, top_counts):
    posts = posts.exclude(user_location=None)
    results =  list(posts.values('user_location').annotate(user_count=Count('user_alias', distinct=True)).order_by('-user_count')[:top_counts])
    top_countries = [i['user_location'] for i in posts.values('user_location').annotate(author_count=Count('user_alias', distinct=True)).order_by('-author_count')[:5]]
    results = []
    for country in top_countries:
        top_authors = posts.filter(user_location=country).values('user_alias').annotate(posts_count=Count('id')).order_by('-posts_count')[:5]
        results.append({country: descending_sort({author['user_alias']: author['posts_count'] for author in top_authors})})
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_authors_by_location(posts, widget.top_counts)
    fields = ['Location', 'Author', 'Count of posts']
    rows = []
    for elem in result:
        [rows.append([*elem.keys(), el[0], el[1]]) for el in list(*elem.values())]
    return fields, rows
