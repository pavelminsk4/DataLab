from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def top_countries(pk, widget_pk):
  posts, widget = project_posts_filter(pk, widget_pk)
  res = post_agregator_top_countries(posts, widget.top_counts)
  return JsonResponse(res, safe = False)

def top_countries_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_agregator_top_countries(posts, widget.top_counts),
        'widget': {'top_countries': model_to_dict(widget)},
        'module_name': 'Online'
    }

def post_agregator_top_countries(posts, top_counts):
    results = posts.values('feedlink__country').annotate(country_count=Count('feedlink__country')).order_by('-country_count')[:top_counts]
    return list(results)
