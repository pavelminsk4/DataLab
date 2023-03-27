from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.http import JsonResponse

def sentiment_number_of_results(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = {
    'positive': posts.filter(sentiment_vote='positive').count(),
    'negative': posts.filter(sentiment_vote='negative').count(),
    'neutral':  posts.filter(sentiment_vote='neutral').count(),
    }
  return JsonResponse(res, safe=False)
