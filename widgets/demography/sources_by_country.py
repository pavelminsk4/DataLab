from widgets.common_widget.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort 
from django.http import JsonResponse
from django.db.models import Count


def get_sources_by_country(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    results = calculate_sources_by_country(posts, widget.top_counts)
    return JsonResponse(results, safe = False)

def calculate_sources_by_country(posts, top_counts):
    top_countries = [i['feedlink__country'] for i in posts.values('feedlink__country').annotate(source_count=Count('feedlink', distinct=True)).order_by('-source_count')[:top_counts]]
    results =[]
    for country in top_countries:
        top_sources = posts.filter(feedlink__country=country).values('feedlink__source1').annotate(posts_count=Count('id')).order_by('-posts_count')[:top_counts]
        results.append({country: descending_sort({i['feedlink__source1']:i['posts_count'] for i in top_sources})})
    return results
