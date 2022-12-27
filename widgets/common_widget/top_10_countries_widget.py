from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import posts_agregator

def top_10_countries(pk):
  project = Project.objects.get(id=pk)
  posts = posts_agregator(project)
  results = posts.values('feedlink__country').annotate(country_count=Count('feedlink__country')).order_by('-country_count')[:10]
  for i in range(len(results)):
    if (results[i]['feedlink__country'] == None or not results[i]['feedlink__country'] or 'img' in results[i]['feedlink__country'] or results[i]['feedlink__country'] == 'None' or results[i]['feedlink__country'] == 'null'):
      results[i]['feedlink__country'] = 'Missing in source'
  res = list(results)
  return JsonResponse(res, safe = False)
