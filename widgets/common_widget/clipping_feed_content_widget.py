from widgets.models import ClippingFeedContentWidget
from django.http import JsonResponse
import re

def cl_fd_cont_widg(request, pk):
  posts = ClippingFeedContentWidget.objects.filter(project_id=pk).order_by('id')
  posts = posts.values(
    'post__id',
    'post__entry_title',
    'post__entry_published',
    'post__entry_summary',
    'post__entry_author',
    'post__entry_links_href',
    'post__entry_media_thumbnail_url',
    'post__entry_media_content_url',
    'post__feed_image_href',
    'post__feed_image_link',
    'post__feed_language__language',
    'post__feedlink__country',
    'post__feedlink__source1',
    'post__feedlink__sourceurl',
    'post__feedlink__alexaglobalrank',
    'post__sentiment',
    )

  for post in posts:
    src = post['post__feedlink__source1']
    post['post__feedlink__source1'] = src if '<img' not in str(src) else re.findall('alt="(.*)"', src)[0]

  res = list(posts)
  return JsonResponse(res, safe = False)
