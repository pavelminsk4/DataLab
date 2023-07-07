from project_social.widgets.influencers.overall_top_authors import get_top_authors
from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse


def calculate(posts):
    results = [
    get_top_authors(posts.filter(user_gender='male')),
    get_top_authors(posts.filter(user_gender='female')),
    ]
    return results

def top_authors_by_gender(pk, widget_pk):
  posts, widget = project_posts_filter(pk, widget_pk)
  return JsonResponse(calculate(posts), safe=False)

def top_authors_by_gender_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate(posts),
        'widget': {'top_authors_by_gender': model_to_dict(widget)}
    }
