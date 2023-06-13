from widgets.common_widget.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from common.descending_sort import descending_sort 
from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count

def get_authors_by_country(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  top_countries = [i['feedlink__country'] for i in posts.values('feedlink__country').annotate(author_count=Count('entry_author', distinct=True)).order_by('-author_count')[:5]]
  results = []
  for country in top_countries:
    top_authors = posts.filter(feedlink__country=country).values('entry_author').annotate(posts_count=Count('id')).order_by('-posts_count')[:5]
    results.append({country: descending_sort({author['entry_author']: author['posts_count'] for author in top_authors})})
  return JsonResponse(results, safe = False)
