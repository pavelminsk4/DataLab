from widgets.common_widget.project_posts_filter import project_posts_filter
from django.http import JsonResponse


def number_of_results(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = get_sentiment_number_of_results(posts)
    return JsonResponse(res, safe=False)

def get_sentiment_number_of_results(posts):
    return {
        'positive': posts.filter(sentiment='positive').count(),
        'negative': posts.filter(sentiment='negative').count(),
        'neutral':  posts.filter(sentiment='neutral').count(),
    }
