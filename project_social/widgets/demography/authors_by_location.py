from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from common.descending_sort import descending_sort 
from project_social.models import ProjectSocial
from django.http import JsonResponse
from django.db.models import Count

def authors_by_location(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  results =  list(posts.values('locationString').annotate(user_count=Count('user_alias', distinct=True)).order_by('-user_count')[:widget.top_counts])
  top_countries = [i['locationString'] for i in posts.values('locationString').annotate(author_count=Count('user_alias', distinct=True)).order_by('-author_count')[:5]]
  results = []
  for country in top_countries:
    top_authors = posts.filter(locationString=country).values('user_alias').annotate(posts_count=Count('id')).order_by('-posts_count')[:5]
    results.append({country: descending_sort({author['user_alias']: author['posts_count'] for author in top_authors})})
  return JsonResponse(results, safe = False)
