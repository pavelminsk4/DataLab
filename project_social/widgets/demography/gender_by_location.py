from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from project_social.models import ProjectSocial
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count


def calculate(posts, widget):
    top_locations = posts.values('locationString').annotate(posts_count=Count('id')).order_by('-posts_count').values_list('locationString', flat=True)[:widget.top_counts]
    results = {}
    for location in list(top_locations):
        results[location] = {'male': posts.filter(locationString=location, user_gender='male').count(),
                             'female': posts.filter(locationString=location, user_gender='female').count(),
                             'undefined': posts.filter(locationString=location, user_gender='undefined').count()}
    return results

def gender_by_location(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return JsonResponse(calculate(posts, widget), safe = False)

def gender_by_location_report(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return {
        'data': calculate(posts, widget),
        'widget': {'gender_by_location': model_to_dict(widget)}
    }
