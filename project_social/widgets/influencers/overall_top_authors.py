from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.http import JsonResponse
from django.db.models import Count, Sum, F


def overall_top_authors(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = get_top_authors(posts)
  return JsonResponse(res, safe=False)

def get_top_authors(posts):
  top_authors = posts.values('user_alias').annotate(user_count=Count('user_alias')).order_by('-user_count')[:5]
  res = []
  for author in top_authors:
    author_posts = posts.filter(user_alias=author['user_alias'])
    a = author_posts.first()
    res.append({
      'name': a.user_name,
      'alias': a.user_alias,
      'picture': a.user_picture,
      'sentiments': {
        'positive': author_posts.filter(sentiment='positive').count(),
        'negative': author_posts.filter(sentiment='negative').count(),
        'neutral': author_posts.filter(sentiment='neutral').count(),
      },
      'gender': a.user_gender,
      'posts': author_posts.count(),
      'media_type': 'Twitter',
      'reach': a.user_followers,
      'engagements': author_posts.aggregate(engagements_sum=Sum(F('count_totalretweets') + F('count_favorites')))['engagements_sum'],
    })
  return res
