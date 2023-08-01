from widgets.common_widget.filters_for_widgets import missing_authors_filter
from widgets.common_widget.project_posts_filter import project_posts_filter
from django.http import JsonResponse
from django.db.models import Count


def get_overall_top_authors(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = get_top_authors(posts)
    return JsonResponse(res, safe=False)

def get_top_authors(posts):
    top_authors = missing_authors_filter(posts).values('entry_author').annotate(author_posts_count=Count('entry_author')).order_by('-author_posts_count')[:5]
    res = []
    for author in top_authors:
        author_posts = posts.filter(entry_author=author['entry_author'])
        a = author_posts.first()
        res.append({
          'name': a.entry_author,
          'url': a.feedlink.sourceurl,
          'picture': a.feed_image_href,
          'sentiments': {
            'positive': author_posts.filter(sentiment='positive').count(),
            'negative': author_posts.filter(sentiment='negative').count(),
            'neutral':  author_posts.filter(sentiment='neutral').count(),
          },
          'posts': author_posts.count(),
          'reach': 0,
          'engagements': 0,
        })
    return res
