from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def languages_by_location(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return JsonResponse(calculate_for_languages_by_location(posts, widget.top_counts), safe = False)

def languages_by_location_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_languages_by_location(posts, widget.top_counts),
        'widget': {'languages_by_location': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_languages_by_location(posts, top_counts):
    top_countries = [i['user_location'] for i in posts.values('user_location').annotate(language_count=Count('language', distinct=True)).order_by('-language_count')[:top_counts]]
    results = {}
    for country in top_countries:
        top_languages = posts.filter(user_location=country).values('language').annotate(posts_count=Count('id')).order_by('-posts_count')[:top_counts]
        results[country] = [{'language': language['language'], 'count': language['posts_count']} for language in top_languages]
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_languages_by_location(posts, widget.top_counts)
    fields = ['Location', 'Language', 'Count of posts']
    countries = list(result.keys())
    rows = []
    for country in countries:
        [rows.append([country, el['language'], el['count']]) for el in result[country]]
    return fields, rows
