from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.http import JsonResponse
from django.db.models import Q


def most_frequent_media_types(pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    res = post_aggregator_most_frequent_media_types(posts)
    return JsonResponse(res, safe=False)

def post_aggregator_most_frequent_media_types(posts):
    count_link, count_text, count_video, count_photo = 0, 0, 0, 0
    for post in posts:
        if post.count_links > 0:
            count_link += 1
        if post.count_textlength > 0:
            count_text += 1
        if post.videos:
            count_video += 1
        if post.count_images > 0:
            count_photo += 1
    return {'count_link': count_link,
            'count_text': count_text,
            'count_video': count_video,
            'count_photo': count_photo,
            'count_combination': posts.filter((Q(count_links__gt=0) & Q(count_textlength__gt=0)) | 
                                     (Q(count_links__gt=0) & Q(videos__isnull=False)) | 
                                     (Q(count_links__gt=0) & Q(count_images__gt=0)) | 
                                     (Q(count_textlength__gt=0) & Q(videos__isnull=False)) | 
                                     (Q(count_textlength__gt=0) & Q(count_images__gt=0)) | 
                                     (Q(videos__isnull=False) & Q(count_images__gt=0))).count()}

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    result = post_aggregator_most_frequent_media_types(posts)
    fields = ['Links', 'Text', 'Video', 'Photo', 'Combination']
    rows = [[result['count_link'], result['count_text'], result['count_video'], result['count_photo'], result['count_combination']]]
    return fields, rows
