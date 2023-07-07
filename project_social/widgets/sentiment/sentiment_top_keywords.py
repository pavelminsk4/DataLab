from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.http import JsonResponse
from common.social_keywords import get_keywords


def calculate(posts):
    return {
        'negative': get_keywords(posts.filter(sentiment='negative')),
        'neutral':  get_keywords(posts.filter(sentiment='neutral')),
        'positive': get_keywords(posts.filter(sentiment='positive')),
    }


def sentiment_top_keywords(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    res = calculate(posts)
    return JsonResponse(res, safe=False)
