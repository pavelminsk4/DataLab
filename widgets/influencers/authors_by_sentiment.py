from widgets.common_widget.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from common.descending_sort import descending_sort 
from widgets.models import WidgetDescription
from project.models import Project
from django.http import JsonResponse
from django.db.models import Count


def get_authors_by_sentiment(pk, widget_pk):
    project = Project.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = WidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    sentiments = ['positive', 'neutral', 'negative']
    results = {}
    for sen in sentiments:
        top_authors = list(posts.filter(sentiment=sen).values('entry_author').annotate(author_post=Count('id')).order_by('-author_post')[:widget.top_counts])
        results[sen] = descending_sort({author['entry_author']: author['author_post'] for author in top_authors})
    return JsonResponse(results, safe = False)
