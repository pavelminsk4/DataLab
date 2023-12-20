from ..serializers import FeedlinksSerializer, FeedlinksCountrySerializer, SpeechSerializer, PostsSerializer
from api.services.preview_service import PreviewPosts
from project.models import Post, Speech, Feedlinks
from rest_framework.generics import ListAPIView
from django.utils.timezone import now
from django.http import JsonResponse
from django.db.models import Q
from datetime import timedelta
from functools import reduce


def get_posts(request):
    return JsonResponse(PreviewPosts().get(request), safe=False)


class CountriesList(ListAPIView):
    serializer_class = FeedlinksCountrySerializer

    def get_queryset(self):
        first_letters = self.request.query_params.get('country')
        posts = Post.objects.filter(entry_published__date=now()-timedelta(days=1))
        countries = posts.filter(feedlink__country__startswith=first_letters).values('feedlink__country').distinct()[:20]
        queryset = Feedlinks.objects.filter(reduce(lambda x, y: x | y, [Q(country=country) for country in [post['feedlink__country'] for post in countries]]))
        return queryset


class SpeechesList(ListAPIView):
    serializer_class = SpeechSerializer

    def get_queryset(self):
        first_letters = self.request.query_params.get('language')
        posts = Post.objects.filter(entry_published__date=now()-timedelta(days=1))
        languages = posts.filter(feed_language__language__startswith=first_letters).values('feed_language__language').distinct()[:20]
        queryset = Speech.objects.filter(reduce(lambda x, y: x | y, [Q(language=language) for language in [post['feed_language__language'] for post in languages]]))
        return queryset


class AuthorList(ListAPIView):
    serializer_class = PostsSerializer

    def get_queryset(self):
        first_letters = self.request.query_params.get('author')
        posts = Post.objects.filter(entry_published__date=now()-timedelta(days=1))
        queryset = posts.filter(entry_author__startswith=first_letters).order_by('entry_author').distinct()[:20]
        return queryset


class SourceList(ListAPIView):
    serializer_class = FeedlinksSerializer
    queryset = Feedlinks.objects.values('source1').distinct()
    search_fields = ['^source1']

    def get_queryset(self):
        first_letters = self.request.query_params.get('source')
        posts = Post.objects.filter(entry_published__date=now()-timedelta(days=1))
        sources = posts.filter(feedlink__source1__startswith=first_letters).values('feedlink__source1').distinct()[:20]
        queryset = Feedlinks.objects.filter(reduce(lambda x, y: x | y, [Q(source1=source) for source in [post['feedlink__source1'] for post in sources]]))
        return queryset

