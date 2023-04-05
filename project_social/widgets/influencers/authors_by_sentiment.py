from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.http import JsonResponse
from django.db.models import Count

def authors_by_sentiment(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res =  list(posts.values('sentiment').annotate(user_count=Count('user_alias', distinct=True)).order_by('-user_count')[:widget.top_counts])
  return JsonResponse(res, safe=False)
