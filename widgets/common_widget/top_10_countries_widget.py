from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from .filters_for_widgets import post_agregator_with_dimensions

def post_agregator_top_countries(posts):
  results = posts.values('feedlink__country').annotate(country_count=Count('feedlink__country')).order_by('-country_count')[:10]
  for i in range(len(results)):
    if (results[i]['feedlink__country'] == None or not results[i]['feedlink__country'] or 'img' in results[i]['feedlink__country'] or results[i]['feedlink__country'] == 'None' or results[i]['feedlink__country'] == 'null'):
      results[i]['feedlink__country'] = 'Missing in source'
  return list(results)

def top_10_countries(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_top_countries(posts)
  return JsonResponse(res, safe = False)
