from widgets.common_widget.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort 
from django.http import JsonResponse
from django.db.models import Count

def get_authors_by_country(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    results = calculate_authors_by_country(posts, widget.top_counts)
    return JsonResponse(results, safe = False)

def calculate_authors_by_country(posts, top_counts):
    top_countries = [i['feedlink__country'] for i in posts.values('feedlink__country').annotate(author_count=Count('entry_author', distinct=True)).order_by('-author_count')[:top_counts]]
    results = []
    for country in top_countries:
        top_authors = posts.filter(feedlink__country=country).values('entry_author').annotate(posts_count=Count('id')).order_by('-posts_count')[:top_counts]
        results.append({country: descending_sort({author['entry_author']: author['posts_count'] for author in top_authors})})
    return results
