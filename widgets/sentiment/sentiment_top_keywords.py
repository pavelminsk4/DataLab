from widgets.common_widget.project_posts_filter import project_posts_filter
from common.online_keywords import get_keywords
from django.http import JsonResponse


def sentiment_top_keywords(pk, widget_pk):
  posts, widget = project_posts_filter(pk, widget_pk)
  res = post_agg_sentiment_top_keywords(posts)
  return JsonResponse(res, safe = False)

def post_agg_sentiment_top_keywords(posts):
  return { 
          'negative': get_keywords(posts.filter(sentiment='negative')),
          'neutral':  get_keywords(posts.filter(sentiment='neutral')),
          'positive': get_keywords(posts.filter(sentiment='positive')),
         }
