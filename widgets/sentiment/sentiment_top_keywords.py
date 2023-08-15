from widgets.common_widget.project_posts_filter import project_posts_filter
from common.online_keywords import get_keywords
from django.forms.models import model_to_dict
from django.http import JsonResponse


def sentiment_top_keywords(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = post_agg_sentiment_top_keywords(posts)
    return JsonResponse(res, safe = False)
  
def sentiment_top_keywords_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_agg_sentiment_top_keywords(posts),
        'widget': {'sentiment_top_keywords': model_to_dict(widget)},
        'module_name': 'Online'
    }  

def post_agg_sentiment_top_keywords(posts):
    return { 
            'negative': get_keywords(posts.filter(sentiment='negative')),
            'neutral':  get_keywords(posts.filter(sentiment='neutral')),
            'positive': get_keywords(posts.filter(sentiment='positive')),
          }
