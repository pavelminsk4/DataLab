from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from common.utils.trunc import trunc
from django.http import JsonResponse
from django.db.models import Count


def sentiment_by_gender(pk, widget_pk):
  posts, widget = project_posts_filter(pk, widget_pk)
  res = calculate_for_sentiment_by_gender(posts, widget.aggregation_period)
  return JsonResponse(res, safe = False)

def sentiment_by_gender_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_sentiment_by_gender(posts, widget.aggregation_period),
        'widget': {'sentiment_by_gender': model_to_dict(widget)},
        'module_name': 'Social'
    }
    
def calculate_for_sentiment_by_gender(posts, aggregation_period):
  user_gender = posts.values('user_gender').annotate(user_count=Count('user_gender')).order_by('-user_count').values_list('user_gender', flat=True)
  results = {user: list(posts.filter(user_gender=user).annotate(date_trunk=trunc('date', aggregation_period)).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for user in user_gender}
  for i in range(len(results)):
   sentiments = ['negative', 'neutral', 'positive']
   for j in range(len(results[user_gender[i]])):
     for sen in sentiments:
       if sen in results[user_gender[i]][j].get('sentiment'):
         sentiments.remove(sen)
   for sen in sentiments:
     results[user_gender[i]].append({'sentiment_count': 0, 'sentiment': sen})
  return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_sentiment_by_gender(posts, widget.aggregation_period)
    languages = result.keys()
    fields = ['Gender', 'Negative', 'Neutral', 'Positive']

    def count_of_sentiment(array, source, sentiment):
        for elem in array[source]:
            if elem['sentiment'] == sentiment:
                return elem['sentiment_count']
            
    rows = [[elem] + [count_of_sentiment(result, elem, sen) for sen in['negative', 'neutral', 'positive']] for elem in languages]
    return fields, rows
