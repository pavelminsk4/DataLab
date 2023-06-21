from widgets.common_widget.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from common.descending_sort import descending_sort
from widgets.models import WidgetDescription
from django.http import JsonResponse
from project.models import Project
from django.db.models import Count

def get_languages_by_country(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  top_countries = [i['feedlink__country'] for i in posts.values('feedlink__country').annotate(language_count=Count('feed_language__language', distinct=True)).order_by('-language_count')[:5]]
  results = {}
  for country in top_countries:
    top_languages = posts.filter(feedlink__country=country).values('feed_language__language').annotate(posts_count=Count('id')).order_by('-posts_count')[:5]
    results[country] = descending_sort({language['feed_language__language']: language['posts_count'] for language in top_languages})
  return JsonResponse(results, safe = False)
