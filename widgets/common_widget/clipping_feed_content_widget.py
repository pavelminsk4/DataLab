from project.models import Post, Project
from widgets.models import ClippingFeedContentWidget
from django.http import JsonResponse

def cl_fd_cont_widg(request, pk):
  posts = ClippingFeedContentWidget.objects.filter(project_id=pk).order_by('id')
  posts = posts.values('post__id', 'post__entry_title', 'post__entry_published', 'post__entry_summary', 'post__entry_media_thumbnail_url', 'post__feed_language__language', 'post__entry_author', 'post__feedlink__country', 'post__feedlink__source1', 'post__sentiment')
  res = list(posts)
  return JsonResponse(res, safe = False)