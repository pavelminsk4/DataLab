from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from django.http import JsonResponse


def mention_sentiment(pk, widget_pk):
    posts, project, widget = filter_for_mentions_posts(pk, widget_pk)
    res = calculate(posts)
    return JsonResponse(res, safe=False)

def calculate(posts):
    positive, negative, neutral = 0, 0, 0
    for post in posts:
        if post.sentiment == 'positive':
            positive += 1
        elif post.sentiment == 'negative':
            negative += 1
        elif post.sentiment == 'neutral':
            neutral += 1 
    res = {
            'positive': positive,
            'negative': negative,
            'neutral': neutral
          }
    return res

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_mentions_posts(pk, widget_pk)
    result = calculate(posts)
    fields = ['Negative', 'Neutral', 'Positive']
    rows = [[result['negative'], result['neutral'], result['positive']]]
    return fields, rows
