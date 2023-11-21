from widgets.common_widget.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def sentiment_top_sources(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = post_agregator_sentiment_top_sources(posts, widget.top_counts)
    return JsonResponse(res, safe=False)

def sentiment_top_sources_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_agregator_sentiment_top_sources(posts, widget.top_counts),
        'widget': {'sentiment_top_sources': model_to_dict(widget)},
        'module_name': 'Online'
    }

def post_agregator_sentiment_top_sources(posts, top_counts):
    top_sources = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count').values_list('feedlink__source1', flat=True)[:top_counts]
    results = {source: list(posts.filter(feedlink__source1=source).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for source in top_sources}
    for i in range(len(results)):
        sentiments = ['negative', 'neutral', 'positive']
        for j in range(len(results[top_sources[i]])):
            for sen in sentiments:
                if sen in results[top_sources[i]][j].get('sentiment'):
                    sentiments.remove(sen)
        for sen in sentiments:
            results[top_sources[i]].append({'sentiment': sen, 'sentiment_count': 0})
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = post_agregator_sentiment_top_sources(posts, widget.top_counts)
    sources = result.keys()
    fields = ['Source', 'Negative', 'Neutral', 'Positive']

    def count_of_sentiment(array, source, sentiment):
        for elem in array[source]:
            if elem['sentiment'] == sentiment:
                return elem['sentiment_count']
            
    rows = [[elem] + [count_of_sentiment(result, elem, sen) for sen in['negative', 'neutral', 'positive']] for elem in sources]
    return fields, rows
