from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import post_agregator_with_dimensions

def post_agregator_top_brands(posts):
  results = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count')[:10]
  for i in range(len(results)):
    if (not results[i]['feedlink__source1'] or 'img' in results[i]['feedlink__source1'] or results[i]['feedlink__source1'] == 'None' or results[i]['feedlink__source1'] == 'null'):
      results[i]['feedlink__source1'] = 'Missing in source'
  return list(results)

def top_10_brands(pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  res = post_agregator_top_brands(posts)
  return JsonResponse(res, safe = False)
