from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from project_social.models import ProjectSocial
from common.social_keywords import get_keywords
from django.http import JsonResponse
from django.db.models import Count


def keywords_by_location(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    countries = posts.values('locationString').annotate(count=Count('locationString')).order_by('-count')[:5]
    res = list(map(lambda x: {x['locationString']: get_keywords(posts.filter(locationString=x['locationString']))}, countries))
    return JsonResponse(res, safe=False)

