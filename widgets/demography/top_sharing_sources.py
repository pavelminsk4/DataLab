from widgets.models import WidgetDescription
from widgets.common_widget.filters_for_widgets import *
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count

def get_mosts(posts):
  most_active_source = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count').first()
  most_active_source_posts = posts.filter(feedlink__source1=most_active_source['feedlink__source1'])

  return [
    {
      'type': 'Most active site',
      'name': most_active_source_posts.first().feedlink.source1,
      'url': most_active_source_posts.first().feedlink.sourceurl,
      'value': f'{most_active_source_posts.count()} post',
      'sentiments': {
        'positive': most_active_source_posts.filter(sentiment='positive').count(),
        'negative': most_active_source_posts.filter(sentiment='negative').count(),
        'neutral': most_active_source_posts.filter(sentiment='neutral').count(),
      },
      'picture': most_active_source_posts.first().feed_image_href,
    },
    {
      'type': 'Most influential site',
      'name': most_active_source_posts.first().feedlink.source1,
      'url': most_active_source_posts.first().feedlink.sourceurl,
      'value': '90210 engagement',
      'sentiments': {
        'positive': most_active_source_posts.filter(sentiment='positive').count(),
        'negative': most_active_source_posts.filter(sentiment='negative').count(),
        'neutral': most_active_source_posts.filter(sentiment='neutral').count(),
      },
      'picture': most_active_source_posts.first().feed_image_href,
    },
  ]

def get_top_sharing_sources(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = get_mosts(posts)
  return JsonResponse(res, safe=False)
