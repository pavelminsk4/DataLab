from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from common.descending_sort import descending_sort
from project_social.models import ProjectSocial
from django.http import JsonResponse
from django.db.models import Count


def authors_by_gender(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    genders = ['male', 'female', 'undefined']
    results = {}
    for gender in genders:
        top_authors = list(posts.filter(user_gender=gender).values('user_name').annotate(author_post=Count('id')).order_by('-author_post')[:widget.top_counts])
        results[gender] = descending_sort({author['user_name']: author['author_post'] for author in top_authors})
    return JsonResponse(results, safe=False)
