from project.models import Project
from .volume_widget import *
from django.shortcuts import get_object_or_404

def clp_widget(pk):
  project = get_object_or_404(Project, pk=pk)
  author_dim_pivot = project.widgets_list_2.clipping_widget.author_dim_pivot
  country_dim_pivot = project.widgets_list_2.clipping_widget.country_dim_pivot
  language_dim_pivot = project.widgets_list_2.clipping_widget.language_dim_pivot
  source_dim_pivot = project.widgets_list_2.clipping_widget.source_dim_pivot
  sentiment_dim_pivot =project.widgets_list_2.clipping_widget.sentiment_dim_pivot
  posts = posts_agregator(project)
  if author_dim_pivot:
   posts = posts.filter(entry_author=author_dim_pivot)
  if country_dim_pivot:
   posts = posts.filter(feedlink__country=country_dim_pivot)
  if language_dim_pivot:
   posts = posts.filter(feed_language__language=language_dim_pivot)
  if source_dim_pivot:
   posts = posts.filter(feedlink__source1=source_dim_pivot)
  if sentiment_dim_pivot:
   posts = posts.filter(sentiment=sentiment_dim_pivot)
  posts = posts.values(
    'entry_title',
    'entry_published',
    'entry_summary',
    'entry_author',
    'entry_links_href',
    'entry_media_thumbnail_url',
    'entry_media_content_url',
    'feed_image_href',
    'feed_image_link',
    'feed_language__language',
    'feedlink__country',
    'feedlink__source1',
    'feedlink__sourceurl',
    'feedlink_alexaglobalrank',
    'sentiment',
    )
  res = list(posts)
  return JsonResponse(res, safe = False)
