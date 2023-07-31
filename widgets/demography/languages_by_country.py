from widgets.common_widget.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort
from django.http import JsonResponse
from django.db.models import Count


def get_languages_by_country(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    results = calculate_languages_by_country(posts, widget.top_counts)
    return JsonResponse(results, safe = False)
  
def calculate_languages_by_country(posts, top_counts):
    top_countries = [i['feedlink__country'] for i in posts.values('feedlink__country').annotate(language_count=Count('feed_language__language', distinct=True)).order_by('-language_count')[:top_counts]]
    results = {}
    for country in top_countries:
      top_languages = posts.filter(feedlink__country=country).values('feed_language__language').annotate(posts_count=Count('id')).order_by('-posts_count')[:top_counts]
      results[country] = [{'language': language['feed_language__language'], 'count': language['posts_count']} for language in top_languages]
    return results
