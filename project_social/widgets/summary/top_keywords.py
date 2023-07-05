from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions
from project_social.widgets.filters_for_widgets import post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from project_social.models import ProjectSocial
from common.social_keywords import get_keywords
from django.forms.models import model_to_dict
from django.http import JsonResponse

def top_keywords(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = get_keywords(posts)
  return JsonResponse(res, safe = False)

def top_keywords_report(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return {
        'data': get_keywords(posts),
        'widget': {'top_keywords': model_to_dict(widget)}
    }
