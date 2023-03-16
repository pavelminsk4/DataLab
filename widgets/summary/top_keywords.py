from widgets.models import WidgetDescription
from widgets.common_widget.filters_for_widgets import *
from project.models import Project
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import collections
from wordcloud import STOPWORDS

def post_agg_top_keywords(posts):
  words = ' '.join([q.entry_summary.lower() for q in posts]).split()
  counter = collections.Counter(words)
  counter = sorted(counter.items(), key=lambda x:x[1],reverse=True)
  sum=0
  kw=[]
  for i in counter:
    if (i[0] not in STOPWORDS and i[0].isalpha() and len(i[0])>3):
      sum+=1
      kw.append(i)
    if (sum == 20):
      break
  kw = dict(kw)
  return [{'key' : i, 'value' : kw[i]/len(words) * 10000} for i in kw]

def top_keywords(pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agg_top_keywords(posts)
  return JsonResponse(res, safe = False)
