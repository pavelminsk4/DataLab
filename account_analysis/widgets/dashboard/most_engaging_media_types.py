from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Sum, F, Q
from django.http import JsonResponse


def most_engaging_media_types(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
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
    engagement = Sum(F('count_favorites') + F('count_totalretweets'))
    return {'link_engaging': link_posts.aggregate(count=engagement)['count'],
            'text_engaging': text_posts.aggregate(count=engagement)['count'],
            'video_engaging': video_posts.aggregate(count=engagement)['count'],
            'photo_engaging': photo_posts.aggregate(count=engagement)['count'],
            'combination_engaging': combination_posts.aggregate(count=engagement)['count']}
