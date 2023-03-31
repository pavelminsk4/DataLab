from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.http import JsonResponse
from project_social.widgets.influencers.overall_top_authors import get_top_authors

def top_authors_by_gender(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = [
    get_top_authors(posts.filter(user_gender='male')),
    get_top_authors(posts.filter(user_gender='female')),
  ]
  return JsonResponse(res, safe=False)
