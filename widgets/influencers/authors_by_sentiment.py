from widgets.common_widget.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort 
from django.http import JsonResponse
from django.db.models import Count


def get_authors_by_sentiment(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    results = calculate_authors_by_sentiment(posts, widget.top_counts)
    return JsonResponse(results, safe = False)

def calculate_authors_by_sentiment(posts, top_counts):
    sentiments = ['positive', 'neutral', 'negative']
    results = {}
    for sen in sentiments:
        top_authors = list(posts.filter(sentiment=sen).values('entry_author').annotate(author_post=Count('id')).order_by('-author_post')[:top_counts])
        results[sen] = descending_sort({author['entry_author']: author['author_post'] for author in top_authors})
    return results
