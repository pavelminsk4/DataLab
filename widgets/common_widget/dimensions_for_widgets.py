from .content_volume_top_5_countries_widget import agregator_results_content_volume_top_countries
from .content_volume_top_5_authors_widget import agregator_results_content_volume_top_authors
from .content_volume_top_5_source_widget import agregator_results_content_volume_top_sources
from .sentiment_top_10_languages_widget import post_agregator_sentiment_top_languages
from .sentiment_top_10_countries_widget import post_agregator_sentiment_top_countries
from .top_10_authors_by_volume_widget import post_agregator_top_auth_by_vol_widget
from .sentiment_top_10_authors_widget import post_agregator_sentiment_top_authors
from .sentiment_top_10_sources_widget import post_agregator_sentiment_top_sources
from .sentiment_for_period_widget import post_agregator_sentiment_for_period
from .top_10_countries_widget import post_agregator_top_countries
from .top_10_languages_widget import post_agregator_top_languages
from .filters_for_widgets import post_agregator_with_dimensions
from .top_10_brands_widget import post_agregator_top_brands
from .volume_widget import post_agregator_volume
from .summary_widget import calculate_summary_widget
from widgets.models import WidgetDescription
from django.http import JsonResponse
from project.models import Project
from django.db.models import Q
from functools import reduce
import json

def author_dim_pivot(authors, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(entry_author=author) for author in authors]))
  return posts

def language_dim_pivot(languages, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(feed_language__language=language) for language in languages]))
  return posts

def country_dim_pivot(countries, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(feedlink__country=country) for country in countries]))
  return posts

def source_dim_pivot(sources, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(feedlink__source1=source) for source in sources]))
  return posts

def sentiment_dim_pivot(sentiments, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(sentiment=sentiment) for sentiment in sentiments]))
  return posts

def dimensions_for_each(request, project_pk, widget_pk):
    project = Project.objects.get(id=project_pk)
    posts = post_agregator_with_dimensions(project)
    widget = WidgetDescription.objects.get(id=widget_pk)
    body = json.loads(request.body)
    smpl_freq = body['smpl_freq']
    widget.author_dim_pivot = body['author_dim_pivot']
    widget.country_dim_pivot = body['country_dim_pivot']
    widget.source_dim_pivot = body['source_dim_pivot']
    widget.language_dim_pivot = body['language_dim_pivot']
    widget.sentiment_dim_pivot = body['sentiment_dim_pivot']
    widget.save()
    if widget.author_dim_pivot:
      posts = author_dim_pivot(widget.author_dim_pivot, posts)
    if widget.country_dim_pivot:
      posts = country_dim_pivot(widget.country_dim_pivot, posts)
    if widget.source_dim_pivot:
      posts = source_dim_pivot(widget.source_dim_pivot, posts)
    if widget.language_dim_pivot:
      posts = language_dim_pivot(widget.language_dim_pivot, posts)
    if widget.sentiment_dim_pivot:
      posts = sentiment_dim_pivot(widget.sentiment_dim_pivot, posts)
    if widget.title == "Content Volume by Top 5 authors":
      res = agregator_results_content_volume_top_authors(posts, smpl_freq)
    elif widget.title == "Content Volume by Top 5 countries":
      res = agregator_results_content_volume_top_countries(posts, smpl_freq)
    elif widget.title == "Content Volume by Top 5 sources":
      res = agregator_results_content_volume_top_sources(posts, smpl_freq)
    elif widget.title == "Sentiment for period widget":
      res = post_agregator_sentiment_for_period(posts, smpl_freq)
    elif widget.title == "Sentiment top 10 authors widget":
      res = post_agregator_sentiment_top_authors(posts)
    elif widget.title == "Sentiment top 10 countries widget":
      res = post_agregator_sentiment_top_countries(posts)
    elif widget.title == "Sentiment top 10 languages widget":
      res = post_agregator_sentiment_top_languages(posts)
    elif widget.title == "Sentiment top 10 sources widget":
      res = post_agregator_sentiment_top_sources(posts)
    elif widget.title == "Top 10 authors by volume":
      res = post_agregator_top_auth_by_vol_widget(posts)
    elif widget.title == "Top 10 countries by volume":
      res = post_agregator_top_countries(posts)
    elif widget.title == "Top 10 brands by volume":
      res = post_agregator_top_brands(posts)
    elif widget.title == "Top 10 languages":
      res = post_agregator_top_languages(posts)
    elif widget.title == "Content volume":
      res = post_agregator_volume(posts, smpl_freq)
    elif widget.title == "Summary":
      res = calculate_summary_widget(posts)
    return JsonResponse(res, safe = False)
