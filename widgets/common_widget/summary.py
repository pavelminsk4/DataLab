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
    sources_quantity, authors_quantity, countries_quantity, languages_quantity = set(), set(), set(), set()
    positive, negative, neutral, count_posts = 0, 0, 0, 0
    for post in posts:
        if post.sentiment == 'positive':
            positive += 1
        if post.sentiment == 'negative':
            negative += 1
        if post.sentiment == 'neutral':
            neutral += 1
        sources_quantity.add('feedlink__source1')
        authors_quantity.add('entry_author')
        countries_quantity.add('feedlink__country')
        languages_quantity.add('feed_language') 
        count_posts += 1
    potential_reach = posts.order_by('-feedlink__alexaglobalrank')[0].feedlink.alexaglobalrank if posts else 0
    return {
      'posts': count_posts,
      'sources': len(sources_quantity),
      'authors': len(authors_quantity),
      'countries': len(countries_quantity),
      'languages': len(languages_quantity),
      'positive': positive,
      'negative': negative,
      'neutral': neutral,
      'reach': potential_reach
      }
