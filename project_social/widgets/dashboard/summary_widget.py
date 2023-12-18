from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from functools import reduce


def summary(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_summary_widget(posts)
    return JsonResponse(res, safe=False)


def summary_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_summary_widget(posts),
        'widget': {'summary': model_to_dict(widget)},
        'module_name': 'Social'
    }


def calculate_summary_widget(posts):
    posts_quantity = posts.count()
    authors_quantity = posts.values('user_name').distinct().count()
    countries_quantity = posts.values('country').distinct().count()
    languages_quantity = posts.values('language').distinct().count()
    pos_posts = posts.filter(sentiment='positive').count()
    neg_posts = posts.filter(sentiment='negative').count()
    neut_posts = posts.filter(sentiment='neutral').count()
    likes_quantity = reduce(lambda x, y: x + y, [x['count_favorites'] for x in posts.values('count_favorites')], 0)
    replies_quantity = reduce(lambda x, y: x + y, [x['count_replies'] for x in posts.values('count_replies')], 0)
    retweets_quantity = reduce(lambda x, y: x + y, [x['count_totalretweets'] for x in posts.values('count_totalretweets')], 0)

    return {
        'posts': posts_quantity,
        'sources': 1,
        'authors': authors_quantity,
        'countries': countries_quantity,
        'languages': languages_quantity,
        'positive': pos_posts,
        'negative': neg_posts,
        'neutral': neut_posts,
        'likes': likes_quantity,
        'replies': replies_quantity,
        'retweets': retweets_quantity,
    }


def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_summary_widget(posts)
    fields = ['posts', 'sources', 'authors', 'countries', 'languages', 'positive', 'negative', 'neutral', 'likes', 'replies', 'retweets']
    row = []
    for elem in fields:
        row.append(res[elem])
    return fields, [row]
