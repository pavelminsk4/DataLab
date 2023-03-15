from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count

def post_agregator_sentiment_top_authors(posts, aggregation_period, top_counts):
  top_authors = posts.values('user_name').annotate(author_count=Count('user_name')).order_by('-author_count').values_list('user_name', flat=True)[:top_counts]
  results = {author: list(posts.filter(user_name=author).annotate(date=Trunc('creation_date', aggregation_period)).values('sentiment_vote').annotate(sentiment_count=Count('sentiment_vote')).order_by('-sentiment_count')) for author in top_authors}
  for i in range(len(results)):
   sentiments = ['negative', 'neutral', 'positive']
   for j in range(len(results[top_authors[i]])):
     for sen in sentiments:
       if sen in results[top_authors[i]][j].get('sentiment_vote'):
         sentiments.remove(sen)
   for sen in sentiments:
     results[top_authors[i]].append({'sentiment_count': 0, 'sentiment': sen})
  return results

def sentiment_authors(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_sentiment_top_authors(posts, widget.aggregation_period, widget.top_counts)
  return JsonResponse(res, safe = False)
