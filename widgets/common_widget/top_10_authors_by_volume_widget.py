from project.models import Project
from django.http import JsonResponse
from django.db.models import Count, Q
from .filters_for_widgets import posts_agregator

def top_10_auth_by_vol_widget(pk):
  project = Project.objects.get(id=pk)
  posts = posts_agregator(project)
  results = posts.values('entry_author').annotate(author_posts_count=Count('entry_author')).order_by('-author_posts_count')[:10]
  for i in range(len(results)):
    if (results[i]['entry_author'] == None or not results[i]['entry_author'] or 'img' in results[i]['entry_author'] or results[i]['entry_author'] == 'None' or results[i]['entry_author'] == 'null'):
      results[i]['entry_author'] = 'Missing in source'  
  res = list(results)
  return JsonResponse(res, safe = False)
