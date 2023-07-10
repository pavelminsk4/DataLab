from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions
from project_social.widgets.filters_for_widgets import post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from project_social.models import ProjectSocial
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count
import json

def calculate(posts, aggregation_period):
  negative_posts = posts.annotate(date_trunc=Trunc('date', aggregation_period)).values("date_trunc").filter(sentiment='negative').annotate(count_negative=Count('sentiment')).order_by("date")
  neutral_posts = posts.annotate(date_trunc=Trunc('date', aggregation_period)).values("date_trunc").filter(sentiment='neutral').annotate(count_neutral=Count('sentiment')).order_by("date")
  positive_posts = posts.annotate(date_trunc=Trunc('date', aggregation_period)).values("date_trunc").filter(sentiment='positive').annotate(count_positive=Count('sentiment')).order_by("date")
  post_by_sentiment = list(negative_posts) + list(neutral_posts) + list(positive_posts)
  results = []
  for date_trunc in sorted(list(set(d['date_trunc'] for d in post_by_sentiment))):
    negative, neutral, positive = 0, 0, 0
    for count_post in post_by_sentiment:
      if date_trunc == count_post['date_trunc']:
        negative += (count_post.get("count_negative") if count_post.get("count_negative") else 0)
        neutral += (count_post.get("count_neutral") if count_post.get("count_neutral") else 0)
        positive += (count_post.get("count_positive") if count_post.get("count_positive") else 0)
    results.append({str(date_trunc): {"negative": negative, "neutral": neutral, "positive": positive}})
  return results

def sentiment(request, pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  body = json.loads(request.body)
  aggregation_period = body['aggregation_period']
  results = calculate(posts, aggregation_period)
  return JsonResponse(results, safe = False)

def sentiment_report(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return {
        'data': calculate(posts, widget.aggregation_period),
        'widget': {'sentiment': model_to_dict(widget)}
    }
