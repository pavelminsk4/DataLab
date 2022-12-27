from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from project.models import Project
from django.db.models.functions import Trunc
from django.db.models import Count
import json
from .filters_for_widgets import posts_agregator

def volume(request, pk):
  project = get_object_or_404(Project, pk=pk)
  posts = posts_agregator(project)
  #smpl_freq = 'month'
  #smpl_freq = 'year'
  body = json.loads(request.body)
  smpl_freq = body['smpl_freq']
  author_dim_pivot = body['author_dim_pivot']
  country_dim_pivot = body['country_dim_pivot']
  source_dim_pivot = body['source_dim_pivot']
  language_dim_pivot = body['language_dim_pivot']
  sentiment_dim_pivot = body['sentiment_dim_pivot']
  if author_dim_pivot!=None:
    posts = posts.filter(entry_author=author_dim_pivot)
  if country_dim_pivot!=None:
    posts = posts.filter(feedlink__country=country_dim_pivot)
  if source_dim_pivot!=None:
    posts = posts.filter(feedlink__source1=source_dim_pivot)
  if language_dim_pivot!=None:
    posts = posts.filter(feed_language__language=language_dim_pivot)
  if sentiment_dim_pivot!=None:
    posts = posts.filter(sentiment=sentiment_dim_pivot)
  posts_per_smpl_freq = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date")
  res = list(posts_per_smpl_freq)
  return JsonResponse(res, safe = False)
