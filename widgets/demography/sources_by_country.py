from widgets.common_widget.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from common.descending_sort import descending_sort 
from widgets.models import WidgetDescription
from django.http import JsonResponse
from project.models import Project
from django.db.models import Count

def get_sources_by_country(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  top_countries = [i['feedlink__country'] for i in posts.values('feedlink__country').annotate(source_count=Count('feedlink', distinct=True)).order_by('-source_count')[:5]]
  results =[]
  for country in top_countries:
    top_sources = posts.filter(feedlink__country=country).values('feedlink__source1').annotate(posts_count=Count('id')).order_by('-posts_count')[:5]
    results.append({country: descending_sort({i['feedlink__source1']:i['posts_count'] for i in top_sources})})
  return JsonResponse(results, safe = False)
