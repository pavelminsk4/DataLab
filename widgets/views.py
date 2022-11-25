from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from project.models import Project, Post
from django.db.models import Q
from functools import reduce
from .common_widget.summary_widget import summary_widget
from .common_widget.volume_widget import volume
from .common_widget.clipping_feed_content_widget import cl_fd_cont_widg
from .common_widget.top_10_authors_by_volume_widget import top_10_auth_by_vol_widget
from .common_widget.clipping_widget import clp_widget
# from .common_widget.sentiment_for_period import sentiment_for_period

# def sntmnt_for_period(request, pk):
#   return sentiment_for_period(pk)

def sum_widget(request, pk):
  return summary_widget(pk)

def vol_widget(request, pk):
  return volume(request, pk)

def clipping_feed_content_widget(request, pk):
  return cl_fd_cont_widg(request, pk)

def top_10_authors_by_volume(request, pk):
  return top_10_auth_by_vol_widget(pk)

def clipping_widget(request, pk):
  return clp_widget(pk)
