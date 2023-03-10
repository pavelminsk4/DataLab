from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import *

def post_agregator_sentiment_top_sources(posts):
  top_brands = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count').values_list('feedlink__source1', flat=True)[:10]
  results = {source: list(posts.filter(feedlink__source1=source).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for source in top_brands}
  for i in range(len(results)):
    sentiments = ['negative', 'neutral', 'positive']
    for j in range(len(results[top_brands[i]])):
      for sen in sentiments:
        if sen in results[top_brands[i]][j].get('sentiment'):
          sentiments.remove(sen)
    for sen in sentiments:
      results[top_brands[i]].append({'sentiment': sen, 'sentiment_count': 0})
  return results

def sentiment_top_10_sources(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_sentiment_top_sources(posts)
  return JsonResponse(res, safe = False)
