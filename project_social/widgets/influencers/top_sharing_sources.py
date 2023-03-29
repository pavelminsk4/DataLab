from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.http import JsonResponse
from django.db.models import Count, F, Sum

def get_mosts(posts):
  most_active_author = posts.annotate(author_count=Count("user_alias")).order_by("-author_count").first()
  most_active_author_posts = posts.filter(user_alias=most_active_author.user_alias)

  most_influental_author_posts = posts.annotate(engagements=Sum(F("count_retweets") + F("count_favorites"))).order_by("-engagements")
  most_influental_author_posts = most_influental_author_posts.filter(user_alias=most_influental_author_posts.first().user_alias)
  most_influental_author = most_influental_author_posts.first()

  return [
    {
      "type": "Most active author",
      "name": most_active_author.user_name,
      "alias": most_active_author.user_alias,
      "value": f"{most_active_author_posts.count()} post",
      "sentiments": {
        "positive": most_active_author_posts.filter(sentiment="positive").count(),
        "negative": most_active_author_posts.filter(sentiment="negative").count(),
        "neutral": most_active_author_posts.filter(sentiment="neutral").count(),
      },
      "picture": most_active_author.user_picture,
      "gender": most_active_author.user_gender,
      "source": "Twitter",
    },
    {
      "type": "Most influential author",
      "name": most_influental_author.user_name,
      "alias": most_influental_author.user_alias,
      "value": f"{most_influental_author_posts.aggregate(Sum('engagements'))['engagements__sum']} engagement",
      "sentiments": {
        "positive": most_influental_author_posts.filter(sentiment="positive").count(),
        "negative": most_influental_author_posts.filter(sentiment="negative").count(),
        "neutral": most_influental_author_posts.filter(sentiment="neutral").count(),
      },
      "picture": most_influental_author.user_picture,
      "gender": most_influental_author.user_gender,
      "source": "Twitter",
    },
  ]

def top_sharing_sources(pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = get_mosts(posts)
  return JsonResponse(res, safe=False)
