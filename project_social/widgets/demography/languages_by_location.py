from project_social.widgets.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def calculate(posts, top_counts):
    top_countries = [i['locationString'] for i in posts.values('locationString').annotate(language_count=Count('language', distinct=True)).order_by('-language_count')[:top_counts]]
    results = {}
    for country in top_countries:
        top_languages = posts.filter(locationString=country).values('language').annotate(posts_count=Count('id')).order_by('-posts_count')[:top_counts]
        results[country] = [{'language': language['language'], 'count': language['posts_count']} for language in top_languages]
    return results

def languages_by_location(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return JsonResponse(calculate(posts, widget.top_counts), safe = False)

def languages_by_location_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate(posts, widget.top_counts),
        'widget': {'languages_by_location': model_to_dict(widget)}
    }
