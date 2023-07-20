from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count


def calculate(posts, top_counts):
    top_locations = posts.values('locationString').annotate(posts_count=Count('id')).order_by('-posts_count').values_list('locationString', flat=True)[:top_counts]
    results = {location: {'male': 0, 'female': 0, 'undefined': 0} for location in list(top_locations)}
    for post in posts:
        if results.get(post.locationString):
            results[post.locationString][post.user_gender] += 1
    return results

def gender_by_location(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return JsonResponse(calculate(posts, widget.top_counts), safe = False)

def gender_by_location_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate(posts, widget.top_counts),
        'widget': {'gender_by_location': model_to_dict(widget)}
    }
