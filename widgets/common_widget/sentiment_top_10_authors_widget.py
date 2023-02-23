from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import *

def post_agregator_sentiment_top_authors(posts):
  top_authors = posts.values('entry_author').annotate(brand_count=Count('entry_author')).order_by('-brand_count').values_list('entry_author', flat=True)[:10]
  results = {author: list(posts.filter(entry_author=author).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for author in top_authors}
  for i in range(len(results)):
   sentiments = ['negative', 'neutral', 'positive']
   for j in range(len(results[top_authors[i]])):
     for sen in sentiments:
       if sen in results[top_authors[i]][j].get('sentiment'):
         sentiments.remove(sen)
   for sen in sentiments:
     results[top_authors[i]].append({'sentiment': sen, 'sentiment_count': 0})
  res = {}
  for key in results:
    if key == '' or key == None or 'img' in key or key == 'None' or key == 'null' or not key:
      res['Missing in source'] = results[key]    
    else:  
      res[key] = results[key]     
  return res    


def sentiment_top_10_authors(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_sentiment_top_authors(posts)
  return JsonResponse(res, safe = False)
