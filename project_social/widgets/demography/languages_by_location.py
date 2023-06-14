from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from common.descending_sort import descending_sort 
from project_social.models import ProjectSocial
from django.http import JsonResponse
from django.db.models import Count


def languages_by_location(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    top_countries = [i['locationString'] for i in posts.values('locationString').annotate(language_count=Count('language', distinct=True)).order_by('-language_count')[:5]]
    results =[]
    for country in top_countries:
        top_languages = posts.filter(locationString=country).values('language').annotate(posts_count=Count('id')).order_by('-posts_count')[:5]
        results.append({country: descending_sort({language['language']: language['posts_count'] for language in top_languages})})
    return JsonResponse(results, safe = False)
