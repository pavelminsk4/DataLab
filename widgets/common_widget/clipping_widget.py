from project.models import Project, Post
from .volume_widget import *
from django.shortcuts import get_object_or_404

def clp_widget(pk):
  project = get_object_or_404(Project, pk=pk)
  posts = posts_agregator(project)
  posts = posts.values(
    'entry_title',
    'entry_published',
    'entry_summary',
    'entry_author',
    'entry_links_href',
    '_entry_media_thumbnail_url',
    'entry_media_content_url',
    'feed_image_href',
    'feed_image_link',
    'feed_language__language',
    'feedlink__country',
    'feedlink__source1',
    'feedlink__sourceurl',
    'sentiment',
    )
  res = list(posts)
  return JsonResponse(res, safe = False)
