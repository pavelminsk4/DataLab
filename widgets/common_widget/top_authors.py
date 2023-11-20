from .filters_for_widgets import missing_authors_filter
from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def top_authors(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    posts = post_agregator_top_auth_by_vol_widget(posts, widget.top_counts)
    return JsonResponse(posts, safe=False)

def top_authors_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_agregator_top_auth_by_vol_widget(posts, widget.top_counts),
        'widget': {'top_authors': model_to_dict(widget)},
        'module_name': 'Online'
    }

def post_agregator_top_auth_by_vol_widget(posts, top_counts):
    results = missing_authors_filter(posts).values('entry_author').annotate(author_posts_count=Count('entry_author')).order_by('-author_posts_count')[:top_counts]
    return list(results)

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = post_agregator_top_auth_by_vol_widget(posts, widget.top_counts)
    fields = ['Author', 'Count of posts']
    rows = [[elem['entry_author'], elem['author_posts_count']] for elem in result]
    return fields, rows
