from account_analysis.widgets.filter_for_posts import *
from account_analysis.widgets.dimensions import *
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse
from django.db.models import Sum, F


def most_engaging_media_types(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    res = post_aggregator_most_engaging_media_types(posts)
    return JsonResponse(res, safe=False)


def post_aggregator_most_engaging_media_types(posts):
    link_posts = posts.filter(count_links__gt=0)
    text_posts = posts.filter(count_textlength__gt=0)
    video_posts = posts.filter(videos__isnull=False)
    photo_posts = posts.filter(count_images__gt=0)
    combination_posts = posts.filter((Q(count_links__gt=0) & Q(count_textlength__gt=0)) | 
                                     (Q(count_links__gt=0) & Q(videos__isnull=False)) | 
                                     (Q(count_links__gt=0) & Q(count_images__gt=0)) | 
                                     (Q(count_textlength__gt=0) & Q(videos__isnull=False)) | 
                                     (Q(count_textlength__gt=0) & Q(count_images__gt=0)) | 
                                     (Q(videos__isnull=False) & Q(count_images__gt=0)))
    engagement = Sum(F('count_favorites') + F('count_retweets'))
    return {'count_link': link_posts.count(),
            'link_engaging': link_posts.aggregate(count=engagement)['count'],
            'count_text': text_posts.count(),
            'text_engaging': text_posts.aggregate(count=engagement)['count'],
            'count_video': video_posts.count(),
            'video_engaging': video_posts.aggregate(count=engagement)['count'],
            'count_photo': photo_posts.count(),
            'photo_engaging': photo_posts.aggregate(count=engagement)['count'],
            'count_combination': combination_posts.count(),
            'combination_engaging': combination_posts.aggregate(count=engagement)['count']}
