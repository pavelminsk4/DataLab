from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count


def sentiment_authors(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_for_sentiment_authors(posts, widget.aggregation_period, widget.top_counts)
    return JsonResponse(res, safe = False)

def sentiment_authors_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_sentiment_authors(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'sentiment_authors': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_sentiment_authors(posts, aggregation_period, top_counts):
  top_authors = posts.values('user_name').annotate(author_count=Count('user_name')).order_by('-author_count').values_list('user_name', flat=True)[:top_counts]
  results = {author: list(posts.filter(user_name=author).annotate(date_trunc=Trunc('date', aggregation_period)).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for author in top_authors}
  for i in range(len(results)):
      sentiments = ['negative', 'neutral', 'positive']
      for j in range(len(results[top_authors[i]])):
          for sen in sentiments:
              if sen in results[top_authors[i]][j].get('sentiment'):
                  sentiments.remove(sen)
      for sen in sentiments:
          results[top_authors[i]].append({'sentiment_count': 0, 'sentiment': sen})
  return results
