from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import posts_agregator

def top_10_languages(pk):
  project = Project.objects.get(id=pk)
  posts = posts_agregator(project)
  results = posts.values('feed_language__language').annotate(language_count=Count('feed_language__language')).order_by('-language_count')[:10]
  for i in range(len(results)):
    if (results[i]['feed_language__language'] == None or not results[i]['feed_language__language'] or 'img' in results[i]['feed_language__language'] or results[i]['feed_language__language'] == 'None' or results[i]['feed_language__language'] == 'null' or results[i]['feed_language__language'] == 'Language not specified'):
      results[i]['feed_language__language'] = 'Missing in source'
  res = list(results)
  return JsonResponse(res, safe = False)
