from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.http import JsonResponse
from django.db.models import Q


def most_frequent_media_types(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    res = post_aggregator_most_frequent_media_types(posts)
    return JsonResponse(res, safe=False)

def post_aggregator_most_frequent_media_types(posts):
    count_link = posts.filter(count_links__gt=0).count()
    count_text = posts.filter(count_textlength__gt=0).count()
    count_video = posts.filter(videos__isnull=False).count()
    count_photo = posts.filter(count_images__gt=0).count()
    count_combination = posts.filter((Q(count_links__gt=0) & Q(count_textlength__gt=0)) | 
                                     (Q(count_links__gt=0) & Q(videos__isnull=False)) | 
                                     (Q(count_links__gt=0) & Q(count_images__gt=0)) | 
                                     (Q(count_textlength__gt=0) & Q(videos__isnull=False)) | 
                                     (Q(count_textlength__gt=0) & Q(count_images__gt=0)) | 
                                     (Q(videos__isnull=False) & Q(count_images__gt=0))).count()
    return {'count_link': count_link,
            'count_text': count_text,
            'count_video': count_video,
            'count_photo': count_photo,
            'count_combination': count_combination}
