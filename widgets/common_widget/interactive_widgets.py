from django.http import JsonResponse
from widgets.models import WidgetDescription
from project.models import Project
from .filters_for_widgets import *
from django.core.paginator import Paginator
import json

def interactive_widgets(request, project_pk, widget_pk):
  project = Project.objects.get(id=project_pk)
  posts = post_agregator_with_dimensions(project)
  widget = WidgetDescription.objects.get(id=widget_pk)
  body = json.loads(request.body)
  posts_per_page = body['posts_per_page']
  page_number = body['page_number']
  if widget.default_title == 'Top 10 languages':
    posts = language_filter_posts(body['language'], posts)
  elif widget.default_title == 'Top 10 brands by volume':
    posts = source_filter_posts(body['source'], posts)
  elif widget.default_title == 'Top 10 countries by volume':
    posts = country_filter_posts(body['country'], posts)
  elif widget.default_title == 'Top 10 authors by volume':
    posts = author_filter_posts(body['author'], posts)
  elif widget.default_title == 'Sentiment top 10 sources widget':
    posts = posts.filter(sentiment=body['sentiment'], feedlink__source1=body['s_value'])
  elif widget.default_title == 'Sentiment top 10 countries widget':
    posts = posts.filter(sentiment=body['sentiment'], feedlink__country=body['s_value'])
  elif widget.default_title == 'Sentiment top 10 authors widget':
    posts = posts.filter(sentiment=body['sentiment'], entry_author=body['s_value'])
  elif widget.default_title == 'Sentiment top 10 languages widget':
    posts = posts.filter(sentiment=body['sentiment'], feed_language__language=body['s_value'])
  elif widget.default_title == 'Content Volume by Top 5 authors':
    posts = author_dimensions_posts(body['value'], posts).filter(entry_published__range=body['dates'])
  elif widget.default_title == "Content Volume by Top 5 countries":
    posts = country_dimensions_posts(body['value'], posts).filter(entry_published__range=body['dates'])
  elif widget.default_title == "Content Volume by Top 5 sources":
    posts = source_dimensions_posts(body['value'], posts).filter(entry_published__range=body['dates'])
  posts = posts.values(
    'id',
    'entry_title',
    'entry_published',
    'entry_summary',
    'entry_media_thumbnail_url',
    'entry_media_content_url',
    'feed_image_href',
    'feed_image_link',
    'feed_language__language',
    'entry_author', 'entry_links_href',
    'feedlink__country',
    'feedlink__source1',
    'feedlink__sourceurl',
    'feedlink__alexaglobalrank',
    'sentiment',
    )
  p = Paginator(posts, posts_per_page)
  posts_list=list(p.page(page_number))
  res = { 'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list }
  return JsonResponse(res, safe = False)
