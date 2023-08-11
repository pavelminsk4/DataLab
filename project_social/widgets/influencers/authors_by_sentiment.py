from project_social.widgets.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def authors_by_sentiment(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return JsonResponse(calculate_for_authors_by_sentiment(posts, widget.top_counts), safe = False)

def authors_by_sentiment_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_authors_by_sentiment(posts, widget.top_counts),
        'widget': {'authors_by_sentiment': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_authors_by_sentiment(posts, top_counts):
    sentiments = ['positive', 'neutral', 'negative']
    results = {}
    for sen in sentiments:
        top_authors = list(posts.filter(sentiment=sen).values('user_name').annotate(author_post=Count('id')).order_by('-author_post')[:top_counts])
        results[sen] = descending_sort({author['user_name']: author['author_post'] for author in top_authors})
    return results
