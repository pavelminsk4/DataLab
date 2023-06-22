from widgets.common_widget.filters_for_widgets import post_agregator_with_dimensions
from widgets.common_widget.filters_for_widgets import post_agregetor_for_each_widget
from widgets.models import WidgetDescription
from django.http import JsonResponse
from project.models import Project


def get_sentiment_number_of_results(posts):
    return {
        'positive': posts.filter(sentiment='positive').count(),
        'negative': posts.filter(sentiment='negative').count(),
        'neutral':  posts.filter(sentiment='neutral').count(),
    }


def number_of_results(pk, widget_pk):
    project = Project.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = WidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    res = get_sentiment_number_of_results(posts)
    return JsonResponse(res, safe=False)
