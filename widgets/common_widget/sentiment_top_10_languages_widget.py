from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import *

def post_agregator_sentiment_top_languages(posts, top_counts):
  top_languages = posts.values('feed_language__language').annotate(brand_count=Count('feed_language__language')).order_by('-brand_count').values_list('feed_language__language', flat=True)[:top_counts]
  results = {language: list(posts.filter(feed_language__language=language).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for language in top_languages}
  for i in range(len(results)):
   sentiments = ['negative', 'neutral', 'positive']
   for j in range(len(results[top_languages[i]])):
     for sen in sentiments:
       if sen in results[top_languages[i]][j].get('sentiment'):
         sentiments.remove(sen)
   for sen in sentiments:
     results[top_languages[i]].append({'sentiment': sen, 'sentiment_count': 0})
  return results      

def sentiment_top_10_languages(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_sentiment_top_languages(posts, widget.top_counts)
  return JsonResponse(res, safe = False)
