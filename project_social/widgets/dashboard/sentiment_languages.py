from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from common.utils.trunc import trunc
from django.http import JsonResponse
from django.db.models import Count


def sentiment_languages(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_for_sentiment_languages(posts, widget.aggregation_period, widget.top_counts)
    return JsonResponse(res, safe = False)

def sentiment_languages_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_sentiment_languages(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'sentiment_languages': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_sentiment_languages(posts, aggregation_period, top_counts):
    top_languages = posts.values('language').annotate(language_count=Count('language')).order_by('-language_count').values_list('language', flat=True)[:top_counts]
    results = {language: list(posts.filter(language=language).annotate(date_trunc=trunc('date', aggregation_period)).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for language in top_languages}
    for i in range(len(results)):
        sentiments = ['negative', 'neutral', 'positive']
        for j in range(len(results[top_languages[i]])):
            for sen in sentiments:
                if sen in results[top_languages[i]][j].get('sentiment'):
                    sentiments.remove(sen)
        for sen in sentiments:
            results[top_languages[i]].append({'sentiment_count': 0, 'sentiment': sen})
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_sentiment_languages(posts, widget.aggregation_period, widget.top_counts)
    languages = result.keys()
    fields = ['Language', 'Negative', 'Neutral', 'Positive']

    def count_of_sentiment(array, source, sentiment):
        for elem in array[source]:
            if elem['sentiment'] == sentiment:
                return elem['sentiment_count']
            
    rows = [[elem] + [count_of_sentiment(result, elem, sen) for sen in['negative', 'neutral', 'positive']] for elem in languages]
    return fields, rows
