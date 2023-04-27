from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count

def post_agregator_top_authors(posts, aggregation_period, top_counts):
  results = list(posts.annotate(date_trunc=Trunc('date', aggregation_period)).values('user_name').annotate(user_count=Count('user_name')).order_by('-user_count')[:top_counts])
  for res in results:
    if not res['user_name']:
      results.remove(res)
  return results

def precalculate_result(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  return post_agregator_top_authors(posts, widget.aggregation_period, widget.top_counts)

def top_authors(pk, widget_pk):
  res = precalculate_result(pk, widget_pk)
  return JsonResponse(res, safe = False)

def top_authors_report(pk, widget_pk):
  res = precalculate_result(pk, widget_pk)  
  context = {}
  labels = []
  data = []
  for r in res:
    labels.append(r['user_name'])
    data.append(int(r['user_count']))
  context['labels'] = labels
  context['data'] = data
  return context
