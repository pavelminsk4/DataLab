from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from widgets.common_widget.filters_for_widgets import *

def get_sources_by_country(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  top_countries = [i['feedlink__country'] for i in posts.values('feedlink__country').annotate(source_count=Count('feedlink', distinct=True)).order_by('-source_count')[:5]]
  results =[]
  for country in top_countries:
    top_sources = posts.filter(feedlink__country=country).values('feedlink__source1').annotate(posts_count=Count('id'))[:5]
    results.append({country: dict(reversed({i['feedlink__source1']:i['posts_count'] for i in top_sources}.items()))})
  return JsonResponse(results, safe = False)
