from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from common.descending_sort import descending_sort
from project_social.models import ProjectSocial
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def calculate(posts, widget):
    genders = ['male', 'female', 'undefined']
    results = {}
    for gender in genders:
        top_authors = list(posts.filter(user_gender=gender).values('user_name').annotate(author_post=Count('id')).order_by('-author_post')[:widget.top_counts])
        results[gender] = descending_sort({author['user_name']: author['author_post'] for author in top_authors})
    return results

def authors_by_gender(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return JsonResponse(calculate(posts, widget), safe=False)

def authors_by_gender_report(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return {
        'data': calculate(posts, widget),
        'widget': {'authors_by_gender': model_to_dict(widget)}
    }
