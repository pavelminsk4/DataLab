from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse


def summary_widget(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_summary_widget(posts)
    return JsonResponse(res, safe=False)
  
def summary_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_summary_widget(posts),
        'widget': {'summary': model_to_dict(widget)},
        'module_name': 'Online'
    }

def calculate_summary_widget(posts):
    posts_quantity = posts.count()
    sources_quantity = posts.values('feedlink__source1').distinct().count()
    authors_quantity = posts.values('entry_author').distinct().count()
    countries_quantity = posts.values('feedlink__country').distinct().count()
    languages_quantity = posts.values('feed_language').distinct().count()
    pos_posts = posts.filter(sentiment='positive').count()
    neg_posts = posts.filter(sentiment='negative').count()
    neut_posts = posts_quantity - pos_posts - neg_posts
    potential_reach = posts.order_by('-feedlink__alexaglobalrank')[0].feedlink.alexaglobalrank if posts else 0 
    return {
      'posts':posts_quantity,
      'sources':sources_quantity,
      'authors':authors_quantity,
      'countries':countries_quantity,
      'languages':languages_quantity,
      'positive':pos_posts,
      'negative':neg_posts,
      'neutral':neut_posts,
      'reach':potential_reach
      }
