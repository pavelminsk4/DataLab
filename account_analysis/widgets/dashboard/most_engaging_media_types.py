from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Sum, F, Q
from django.http import JsonResponse


def most_engaging_media_types(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    res = post_aggregator_most_engaging_media_types(posts)
    return JsonResponse(res, safe=False)


def post_aggregator_most_engaging_media_types(posts):
    combination_posts = posts.filter((Q(count_links__gt=0) & Q(count_textlength__gt=0)) | 
                                     (Q(count_links__gt=0) & Q(videos__isnull=False)) | 
                                     (Q(count_links__gt=0) & Q(count_images__gt=0)) | 
                                     (Q(count_textlength__gt=0) & Q(videos__isnull=False)) | 
                                     (Q(count_textlength__gt=0) & Q(count_images__gt=0)) | 
                                     (Q(videos__isnull=False) & Q(count_images__gt=0)))
    link_engagements, text_engagements, video_engagements, photo_engagements = 0, 0, 0, 0
    for post in posts:
        if post.count_links > 0:
            link_engagements += (post.count_favorites + post.count_totalretweets)
        if post.count_textlength > 0:
            text_engagements += (post.count_favorites + post.count_totalretweets)
        if post.videos:
            video_engagements += (post.count_favorites + post.count_totalretweets)
        if post.count_images > 0:
            photo_engagements += (post.count_favorites + post.count_totalretweets)
    engagement = Sum(F('count_favorites') + F('count_totalretweets'))
    return {'link_engaging': link_engagements,
            'text_engaging': text_engagements,
            'video_engaging': video_engagements,
            'photo_engaging': photo_engagements,
            'combination_engaging': combination_posts.aggregate(count=engagement)['count']}
