from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def top_sources(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = post_agregator_top_sources(posts, widget.top_counts)
    return JsonResponse(res, safe=False)

def top_sources_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_agregator_top_sources(posts, widget.top_counts),
        'widget': {'top_sources': model_to_dict(widget)},
        'module_name': 'Online'
    }

def post_agregator_top_sources(posts, top_counts):
    results = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count')[:top_counts]
    return list(results)

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = post_agregator_top_sources(posts, widget.top_counts)
    fields = ['Source', 'Count of posts']
    rows = [[elem['feedlink__source1'], elem['brand_count']] for elem in result]
    return fields, rows
