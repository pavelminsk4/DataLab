from project_social.models import SocialClippingWidget
from django.http import JsonResponse
import re

def clipping_feed(pk, widget_pk):
    posts = SocialClippingWidget.objects.filter(project_id=pk).order_by('id')
    posts = posts.values(
        'post__id',
        'post__post_id',
        'post__user_name',
        'post__user_alias',
        'post__text',
        'post__sentiment',
        'post__date',
        'post__locationString',
        'post__language',
        'post__count_favorites',
        'post__count_totalretweets',
        'post__count_replies',
        'post__user_picture',
        'post__images',
        )

    res = list(posts)
    return JsonResponse(res, safe = False)
