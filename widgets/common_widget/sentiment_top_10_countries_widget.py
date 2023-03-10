from widgets.models import WidgetDescription
from project.models import Post, Project
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import Trunc
import json
from .filters_for_widgets import *

def post_agregator_sentiment_top_countries(posts):
  top_countries = posts.values('feedlink__country').annotate(brand_count=Count('feedlink__country')).order_by('-brand_count').values_list('feedlink__country', flat=True)[:10]
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

def sentiment_top_10_countries(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_sentiment_top_countries(posts) 
  return JsonResponse(res, safe = False)
