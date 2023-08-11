from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from common.social_keywords import get_keywords


def sentiment_top_keywords(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_for_sentiment_top_keywords(posts)
    return JsonResponse(res, safe=False)
    
def sentiment_top_keywords_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_sentiment_top_keywords(posts),
        'widget': {'sentiment_top_keywords': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_sentiment_top_keywords(posts):
    return {
        'negative': get_keywords(posts.filter(sentiment='negative')),
        'neutral':  get_keywords(posts.filter(sentiment='neutral')),
        'positive': get_keywords(posts.filter(sentiment='positive')),
    }
