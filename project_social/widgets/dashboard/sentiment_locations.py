from project_social.widgets.project_posts_filter import project_posts_filter
from common.utils.trunc_function import trunc_function
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count


def sentiment_locations(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_for_sentiment_locations(posts, widget.aggregation_period, widget.top_counts)
    return JsonResponse(res, safe = False)

def sentiment_locations_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_sentiment_locations(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'sentiment_locations': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_sentiment_locations(posts, aggregation_period, top_counts):
    top_locations = posts.values('locationString').annotate(language_count=Count('locationString')).order_by('-language_count').values_list('locationString', flat=True)[:top_counts]
    results = {location: list(posts.filter(locationString=location).annotate(date_trunc=trunc_function('date', aggregation_period)).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for location in top_locations}
    for i in range(len(results)):
        sentiments = ['negative', 'neutral', 'positive']
        for j in range(len(results[top_locations[i]])):
            for sen in sentiments:
                if sen in results[top_locations[i]][j].get('sentiment'):
                    sentiments.remove(sen)
        for sen in sentiments:
            results[top_locations[i]].append({'sentiment_count': 0, 'sentiment': sen})
    return results
