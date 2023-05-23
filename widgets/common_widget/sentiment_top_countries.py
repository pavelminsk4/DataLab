from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import *

def post_aggregator_sentiment_top_countries(posts, top_counts):
  top_countries = posts.values('feedlink__country').annotate(brand_count=Count('feedlink__country')).order_by('-brand_count').values_list('feedlink__country', flat=True)[:top_counts]
  results = {country: list(posts.filter(feedlink__country=country).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for country in top_countries}
  for i in range(len(results)):
    sentiments = ['negative', 'neutral', 'positive']
    for j in range(len(results[top_countries[i]])):
      for sen in sentiments:
        if sen in results[top_countries[i]][j].get('sentiment'):
          sentiments.remove(sen)
    for sen in sentiments:
      results[top_countries[i]].append({'sentiment': sen, 'sentiment_count': 0})
  return results

def sentiment_top_countries(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_aggregator_sentiment_top_countries(posts, widget.top_counts)
  return JsonResponse(res, safe = False)