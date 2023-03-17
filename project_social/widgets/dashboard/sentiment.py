from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count

def post_agregator_sentiment_for_period(posts, aggregation_period):
  negative_posts = posts.annotate(date=Trunc('creation_date', aggregation_period)).values("creation_date").filter(sentiment_vote='negative').annotate(count_negative=Count('sentiment_vote')).order_by("creation_date")
  neutral_posts = posts.annotate(date=Trunc('creation_date', aggregation_period)).values("creation_date").filter(sentiment_vote='neutral').annotate(count_neutral=Count('sentiment_vote')).order_by("creation_date")
  positive_posts = posts.annotate(date=Trunc('creation_date', aggregation_period)).values("creation_date").filter(sentiment_vote='positive').annotate(count_positive=Count('sentiment_vote')).order_by("creation_date")
  post_by_sentiment = list(negative_posts) + list(neutral_posts) + list(positive_posts)
  results = []
  for date in sorted(list(set(d['creation_date'] for d in post_by_sentiment))):
    negative, neutral, positive = 0, 0, 0
    for count_post in post_by_sentiment:
      if date == count_post['creation_date']:
        negative += (count_post.get("count_negative") if count_post.get("count_negative") else 0)
        neutral += (count_post.get("count_neutral") if count_post.get("count_neutral") else 0)
        positive += (count_post.get("count_positive") if count_post.get("count_positive") else 0)
    results.append({str(date): {"negative": negative, "neutral": neutral, "positive": positive}})
  return results

def sentiment(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  results = post_agregator_sentiment_for_period(posts, widget.aggregation_period)
  return JsonResponse(results, safe = False)  