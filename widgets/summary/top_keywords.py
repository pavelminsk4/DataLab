from widgets.models import WidgetDescription
from widgets.common_widget.filters_for_widgets import *
from project.models import Project
from django.http import JsonResponse
import collections
import itertools
from common.stopwords import STOPWORDS

def post_agg_top_keywords(posts):
  words = list(itertools.chain(
    *[list(set(post.entry_summary.lower().split())) for post in posts]))
  tokens = sorted(collections.Counter(words).items(), key=lambda x:x[1], reverse=True)
  keywords = []
  for token in tokens:
    if (token[0] not in STOPWORDS and token[0].isalpha()):
      keywords.append(token)
    if (len(keywords) == 20):
      break
  keywords = dict(keywords)
  return [{'key' : kw, 'value' : keywords[kw]/len(posts)} for kw in keywords]

def top_keywords(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agg_top_keywords(posts)
  return JsonResponse(res, safe = False)
