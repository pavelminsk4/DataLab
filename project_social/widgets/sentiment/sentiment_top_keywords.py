from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from widgets.common_widget.stopwords import STOPWORDS
from project_social.models import ProjectSocial
from django.http import JsonResponse
from collections import Counter
import itertools

def post_agg_sentiment_top_keywords(posts):
  return { 
          'negative': get_keywords(posts.filter(sentiment_vote='negative')),
          'neutral':  get_keywords(posts.filter(sentiment_vote='neutral')),
          'positive': get_keywords(posts.filter(sentiment_vote='positive')),
         }


def get_keywords(posts):
  words = list(itertools.chain(
    *[list(set(post.text.lower().split())) for post in posts]))
  tokens = sorted(Counter(words).items(), key=lambda x:x[1], reverse=True)
  keywords = []
  for token in tokens:
    if (token[0] not in STOPWORDS and token[0].isalpha()):
      keywords.append(token)
    if (len(keywords) == 20):
      break
  keywords = dict(keywords)
  return [{'key' : kw, 'value' : keywords[kw]/len(posts)} for kw in keywords]

def sentiment_top_keywords(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agg_sentiment_top_keywords(posts)
  return JsonResponse(res, safe = False)
