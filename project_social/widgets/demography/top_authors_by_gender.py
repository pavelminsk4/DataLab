from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.widgets.influencers.overall_top_authors import get_top_authors
from project_social.models import SocialWidgetDescription
from project_social.models import ProjectSocial
from django.forms.models import model_to_dict
from django.http import JsonResponse


def calculate(posts):
    results = [
    get_top_authors(posts.filter(user_gender='male')),
    get_top_authors(posts.filter(user_gender='female')),
    ]
    return results

def top_authors_by_gender(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  return JsonResponse(calculate(posts), safe=False)

def top_authors_by_gender_report(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return {
        'data': calculate(posts),
        'widget': {'top_authors_by_gender': model_to_dict(widget)}
    }
