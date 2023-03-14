from widgets.models import WidgetDescription
from django.http import JsonResponse
from django.db.models import Q
from functools import reduce
import json

def dimensions_for_each(request, widget_pk):
    widget = WidgetDescription.objects.get(id=widget_pk)
    body = json.loads(request.body)
    widget.author_dim_pivot = body['author_dim_pivot']
    widget.country_dim_pivot = body['country_dim_pivot']
    widget.source_dim_pivot = body['source_dim_pivot']
    widget.language_dim_pivot = body['language_dim_pivot']
    widget.sentiment_dim_pivot = body['sentiment_dim_pivot']
    widget.save()
    return JsonResponse({}, safe = False)

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
