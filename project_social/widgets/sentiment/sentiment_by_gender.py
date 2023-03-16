from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count

def post_agregator_sentiment_by_gender(posts, aggregation_period):
  user_gender = posts.values('user_gender').annotate(user_count=Count('user_gender')).order_by('-user_count').values_list('user_gender', flat=True)
  results = {user: list(posts.filter(user_gender=user).annotate(date=Trunc('creation_date', aggregation_period)).values('sentiment_vote').annotate(sentiment_count=Count('sentiment_vote')).order_by('-sentiment_count')) for user in user_gender}
  for i in range(len(results)):
   sentiments = ['negative', 'neutral', 'positive']
   for j in range(len(results[user_gender[i]])):
     for sen in sentiments:
       if sen in results[user_gender[i]][j].get('sentiment_vote'):
         sentiments.remove(sen)
   for sen in sentiments:
     results[user_gender[i]].append({'sentiment_count': 0, 'sentiment': sen})
  return results

def sentiment_by_gender(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_sentiment_by_gender(posts, widget.aggregation_period)
  return JsonResponse(res, safe = False)
