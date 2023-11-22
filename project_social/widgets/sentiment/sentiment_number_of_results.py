from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse


def sentiment_number_of_results(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_for_sentiment_number_of_results(posts)
    return JsonResponse(res, safe=False)

def sentiment_number_of_results_report(pk, widget_pk, name_widget):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_sentiment_number_of_results(posts),
        'widget': {name_widget: model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_sentiment_number_of_results(posts):
    return {
        'positive': posts.filter(sentiment='positive').count(),
        'negative': posts.filter(sentiment='negative').count(),
        'neutral':  posts.filter(sentiment='neutral').count(),
    }

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_sentiment_number_of_results(posts)
    fields = ['Negative', 'Neutral', 'Positive']
    rows = [[result['negative'], result['neutral'], result['positive']]]
    return fields, rows
