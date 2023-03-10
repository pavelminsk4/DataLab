from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import Trunc
from .filters_for_widgets import *

def post_agregator_sentiment_for_period(posts, smpl_freq):
  negative_posts = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").filter(sentiment='negative').annotate(count_negative=Count('sentiment')).order_by("date")
  neutral_posts = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").filter(sentiment='neutral').annotate(count_neutral=Count('sentiment')).order_by("date")
  positive_posts = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").filter(sentiment='positive').annotate(count_positive=Count('sentiment')).order_by("date")
  post_by_sentiment = list(negative_posts) + list(neutral_posts) + list(positive_posts)
  results = []
  for date in sorted(list(set(d['date'] for d in post_by_sentiment))):
    negative, neutral, positive = 0, 0, 0
    for count_post in post_by_sentiment:
      if date == count_post['date']:
        negative += (count_post.get("count_negative") if count_post.get("count_negative") else 0)
        neutral += (count_post.get("count_neutral") if count_post.get("count_neutral") else 0)
        positive += (count_post.get("count_positive") if count_post.get("count_positive") else 0)
    results.append({str(date): {"negative": negative, "neutral": neutral, "positive": positive}})
  return results

def sentiment_for_period(request, pk, widget_pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  smpl_freq = widget.aggregation_period
  results = post_agregator_sentiment_for_period(posts, smpl_freq)
  return JsonResponse(results, safe = False)  
