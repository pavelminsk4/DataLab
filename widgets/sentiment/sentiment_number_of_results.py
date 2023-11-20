from widgets.common_widget.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse


def number_of_results(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = get_sentiment_number_of_results(posts)
    return JsonResponse(res, safe=False)

def number_of_results_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': get_sentiment_number_of_results(posts),
        'widget': {'sentiment_number_of_results': model_to_dict(widget)},
        'module_name': 'Online'
    }
    
def sentiment_diagram_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': get_sentiment_number_of_results(posts),
        'widget': {'sentiment_diagram': model_to_dict(widget)},
        'module_name': 'Online'
    }

def get_sentiment_number_of_results(posts):
    positive, negative, neutral = 0, 0, 0
    for post in posts:
        if post.sentiment == 'positive':
            positive += 1
        if post.sentiment == 'negative':
            negative += 1
        if post.sentiment == 'neutral':
            neutral += 1
    return {
        'positive': positive,
        'negative': negative,
        'neutral':  neutral,
    }

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = get_sentiment_number_of_results(posts)
    fields = ['Negative', 'Neutral', 'Positive']
    rows = [[result['negative'], result['neutral'], result['positive']]]
    return fields, rows
