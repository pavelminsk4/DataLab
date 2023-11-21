
from widgets.common_widget.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def get_overall_top_sources(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = get_top_sources(posts)
    return JsonResponse(res, safe=False)

def get_overall_top_sources_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': get_top_sources(posts),
        'widget': {'overall_top_sources': model_to_dict(widget)},
        'module_name': 'Online'
    }  

def get_top_sources(posts):
    top_sources = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count')[:5]
    res = []
    for source in top_sources:
        source_posts = posts.filter(feedlink__source1=source['feedlink__source1'])
        count_positive, count_negative, count_neutral, count_posts = 0, 0, 0, 0
        s = source_posts.first()
        for post in source_posts:
            if post.sentiment == 'positive':
                count_positive += 1
            elif post.sentiment == 'negative':
                count_negative += 1
            elif post.sentiment == 'neutral':
                count_neutral += 1
            count_posts += 1
        res.append({
            'name': s.feedlink.source1,
            'url': s.feedlink.sourceurl,
            'picture': s.feed_image_href,
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
