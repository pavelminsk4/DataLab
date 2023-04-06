from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from widgets.common_widget.filters_for_widgets import *

def get_top_sources(posts):
  top_sources = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count')[:5]
  res = []
  for source in top_sources:
    source_posts = posts.filter(feedlink__source1=source['feedlink__source1'])
    s = source_posts.first()
    res.append({
      'name': s.feedlink.source1,
      'url': s.feedlink.sourceurl,
      'picture': s.feed_image_href,
      'sentiments': {
        'positive': source_posts.filter(sentiment='positive').count(),
        'negative': source_posts.filter(sentiment='negative').count(),
        'neutral': source_posts.filter(sentiment='neutral').count(),
      },
      'posts': source_posts.count(),
      'reach': 0,
      'engagements': 0,
    })
  return res

def get_overall_top_sources(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = get_top_sources(posts)
  return JsonResponse(res, safe=False)
