from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def top_languages(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = post_aggregator_top_languages(posts, widget.top_counts)
    return JsonResponse(res, safe=False)

def top_languages_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_aggregator_top_languages(posts, widget.top_counts),
        'widget': {'top_languages': model_to_dict(widget)},
        'module_name': 'Online'
    }

def post_aggregator_top_languages(posts, top_counts):
  results = posts.values('feed_language__language').annotate(language_count=Count('feed_language__language')).order_by('-language_count')[:top_counts]
  return list(results)

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = post_aggregator_top_languages(posts, widget.top_counts)
    fields = ['Language', 'Count of posts']
    rows = [[elem['feed_language__language'], elem['language_count']] for elem in result]
    return fields, rows
