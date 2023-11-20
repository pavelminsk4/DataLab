from widgets.common_widget.filters_for_widgets import missing_authors_filter
from widgets.common_widget.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def sentiment_top_authors(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = post_agregator_sentiment_top_authors(posts, widget.top_counts)
    return JsonResponse(res, safe=False)

def sentiment_top_authors_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_agregator_sentiment_top_authors(posts, widget.top_counts),
        'widget': {'sentiment_top_authors': model_to_dict(widget)},
        'module_name': 'Online'
    }

def post_agregator_sentiment_top_authors(posts, top_counts):
    top_authors = missing_authors_filter(posts).values('entry_author').annotate(brand_count=Count('entry_author')).order_by('-brand_count').values_list('entry_author', flat=True)[:top_counts]
    results = {author: list(posts.filter(entry_author=author).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for author in top_authors}
    for i in range(len(results)):
        sentiments = ['negative', 'neutral', 'positive']
        for j in range(len(results[top_authors[i]])):
            for sen in sentiments:
                if sen in results[top_authors[i]][j].get('sentiment'):
                    sentiments.remove(sen)
        for sen in sentiments:
            results[top_authors[i]].append({'sentiment': sen, 'sentiment_count': 0})
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = post_agregator_sentiment_top_authors(posts, widget.top_counts)
    authors = result.keys()
    fields = ['Author', 'Negative', 'Neutral', 'Positive']

    def count_of_sentiment(array, source, sentiment):
        for elem in array[source]:
            if elem['sentiment'] == sentiment:
                return elem['sentiment_count']
            
    rows = [[elem] + [count_of_sentiment(result, elem, sen) for sen in['negative', 'neutral', 'positive']] for elem in authors]
    return fields, rows
