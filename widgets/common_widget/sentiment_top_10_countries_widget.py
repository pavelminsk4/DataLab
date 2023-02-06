from project.models import Post, Project
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import Trunc
import json
from .filters_for_widgets import post_agregator_with_dimensions

def sentiment_top_10_countries(pk):
  project = Project.objects.get(id=pk)

  posts = post_agregator_with_dimensions(project)
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
  res = {}
  for key in results:
    if key == '' or key == None or 'img' in key or key == 'None' or key == 'null' or not key:
      res['Missing in source'] = results[key]    
    else:  
      res[key] = results[key]      
  return JsonResponse(res, safe = False)
