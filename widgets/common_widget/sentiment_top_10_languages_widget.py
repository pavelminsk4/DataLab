from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import post_agregator_with_dimensions

def post_agregator_sentiment_top_languages(posts):
  top_languages = posts.values('feed_language__language').annotate(brand_count=Count('feed_language__language')).order_by('-brand_count').values_list('feed_language__language', flat=True)[:10]
  results = {language: list(posts.filter(feed_language__language=language).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for language in top_languages}
  for i in range(len(results)):
   sentiments = ['negative', 'neutral', 'positive']
   for j in range(len(results[top_languages[i]])):
     for sen in sentiments:
       if sen in results[top_languages[i]][j].get('sentiment'):
         sentiments.remove(sen)
   for sen in sentiments:
     results[top_languages[i]].append({'sentiment': sen, 'sentiment_count': 0})
  res = {}
  for key in results:
    if key == '' or key == None or 'img' in key or key == 'None' or key == 'null' or not key or key == 'Language not specified':
      res['Missing in source'] = results[key]    
    else:  
      res[key] = results[key]
  return res       

def sentiment_top_10_languages(pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  res = post_agregator_sentiment_top_languages(posts)
  return JsonResponse(res, safe = False)
