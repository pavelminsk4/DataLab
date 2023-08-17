
from widgets.common_widget.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def get_overall_top_sources(pk, widget_pk):
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
        s = source_posts.first()
        res.append({
            'name': s.feedlink.source1,
            'url': s.feedlink.sourceurl,
            'picture': s.feed_image_href,
            'sentiments': {
                'positive': source_posts.filter(sentiment='positive').count(),
                'negative': source_posts.filter(sentiment='negative').count(),
                'neutral': source_posts.filter(sentiment='neutral').count(),
            },
            'posts': source_posts.count(),
            'reach': 0,
            'engagements': 0,
          })
    return res
