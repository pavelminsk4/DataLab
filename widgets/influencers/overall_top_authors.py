from widgets.common_widget.filters_for_widgets import missing_authors_filter
from widgets.common_widget.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def get_overall_top_authors(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = get_top_authors(posts)
    return JsonResponse(res, safe=False)
  
def get_overall_top_authors_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': get_top_authors(posts),
        'widget': {'overall_top_authors': model_to_dict(widget)},
        'module_name': 'Online'
    }  

def get_top_authors(posts):
    top_authors = missing_authors_filter(posts).values('entry_author').annotate(author_posts_count=Count('entry_author')).order_by('-author_posts_count')[:5]
    res = []
    for author in top_authors:
        author_posts = posts.filter(entry_author=author['entry_author'])
        count_positive, count_negative, count_neutral, count_posts = 0, 0, 0, 0
        a = author_posts.first()
        for post in author_posts:
            if post.sentiment == 'positive':
                count_positive += 1
            elif post.sentiment == 'negative':
                count_negative += 1
            elif post.sentiment == 'neutral':
                count_neutral += 1
            count_posts += 1
        res.append({
                    'name': a.entry_author,
                    'url': a.feedlink.sourceurl,
                    'picture': a.feed_image_href,
                    'sentiments': {
                                    'positive': count_positive,
                                    'negative': count_negative,
                                    'neutral':  count_neutral,
                                  },
                    'posts': count_posts,
                    'reach': 0,
                    'engagements': 0,
                  })
    return res
