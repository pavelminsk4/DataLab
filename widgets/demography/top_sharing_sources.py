from widgets.common_widget.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def get_top_sharing_sources(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = get_mosts(posts)
    return JsonResponse(res, safe=False)
  
def get_top_sharing_sources_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': get_mosts(posts),
        'widget': {'top_sharing_sources': model_to_dict(widget)},
        'module_name': 'Online'
    }  

def get_mosts(posts):
    most_active_source = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count').first()
    most_active_source_posts = posts.filter(feedlink__source1=most_active_source['feedlink__source1'])
    most_active_source = most_active_source_posts.first()
    positive, negative, neutral, count_posts = 0, 0, 0, 0
    for post in most_active_source_posts:
        if post.sentiment == 'positive':
            positive += 1
        if post.sentiment == 'negative':
            negative += 1
        if post.sentiment == 'neutral':
            neutral += 1
        count_posts += 1
    return [
        {
          'type': 'Most active site',
          'name': most_active_source.feedlink.source1,
          'url': most_active_source.feedlink.sourceurl,
          'value': f"{count_posts} posts",
          'sentiments': {
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
          },
          'picture': most_active_source.feed_image_href,
        },
        {
          'type': 'Most influential site',
          'name': most_active_source.feedlink.source1,
          'url': most_active_source.feedlink.sourceurl,
          'value': '90210 engagement',
          'sentiments': {
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
          },
          'picture': most_active_source.feed_image_href,
        },
      ]
