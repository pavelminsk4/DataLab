from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from project.models import Project, Post
from django.db.models import Q
from functools import reduce
from .common_widget.summary_widget import summary_widget
from .common_widget.volume_widget import volume
from .common_widget.clipping_feed_content_widget import cl_fd_cont_widg
from .common_widget.top_10_authors_by_volume_widget import top_10_auth_by_vol_widget
from .common_widget.top_10_brands_widget import top_10_brands
from .common_widget.top_10_countries_widget import top_10_countries
from .common_widget.top_10_languages_widget import top_10_languages
from .common_widget.content_volume_top_5_source_widget import content_volume_top_5_source
from .common_widget.sentiment_top_10_sources_widget import sentiment_top_10_sources
from .common_widget.sentiment_top_10_countries_widget import sentiment_top_10_countries
from .common_widget.sentiment_top_10_authors_widget import sentiment_top_10_authors
from .common_widget.sentiment_top_10_languages_widget import sentiment_top_10_languages
from .common_widget.content_volume_top_5_authors_widget import content_volume_top_5_authors
from .common_widget.content_volume_top_5_countries_widget import content_volume_top_5_countries
from .common_widget.sentiment_for_period_widget import sentiment_for_period
from .common_widget.dimensions_for_widgets import dimensions_for_each

def sum_widget(request, pk):
  return summary_widget(pk)

def vol_widget(request, pk):
  return volume(request, pk)

def clipping_feed_content_widget(request, pk):
  return cl_fd_cont_widg(request, pk)

def top_10_authors_by_volume(request, pk):
  return top_10_auth_by_vol_widget(pk)

def top_10_brands_widget(request, pk):
  return top_10_brands(pk)

def top_10_countries_widget(request, pk):
  return top_10_countries(pk)

def top_10_languages_widget(request, pk):
  return top_10_languages(pk)

def content_volume_top_5_source_widget(request, pk):
  return content_volume_top_5_source(request, pk)  

def sentiment_top_10_sources_widget(request, pk):
  return sentiment_top_10_sources(pk)

def sentiment_top_10_countries_widget(request, pk):
  return sentiment_top_10_countries(pk)

def sentiment_top_10_authors_widget(request, pk):
  return sentiment_top_10_authors(pk)

def sentiment_top_10_languages_widget(request, pk):
  return sentiment_top_10_languages(pk)

def sentiment_for_period_widget(request, pk):
  return sentiment_for_period(request, pk)

def content_volume_top_5_authors_widget(request, pk):
  return content_volume_top_5_authors(request, pk)

def content_volume_top_5_countries_widget(request, pk):
  return content_volume_top_5_countries(request, pk)

def dimensions_for_each_widgets(request, project_pk, widget_pk):
  return dimensions_for_each(request, project_pk, widget_pk)
