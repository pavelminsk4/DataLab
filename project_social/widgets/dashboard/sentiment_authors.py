from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from project_social.models import ProjectSocial
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count

def calculate(posts, aggregation_period, top_counts):
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

def sentiment_authors(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = calculate(posts, widget.aggregation_period, widget.top_counts)
  return JsonResponse(res, safe = False)

def sentiment_authors_report(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return {
        'data': calculate(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'content_volume_top_locations': model_to_dict(widget)}
    }
