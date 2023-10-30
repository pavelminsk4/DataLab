from .. import variables
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets, generics, filters, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from widgets.models import ClippingFeedContentWidget, WidgetsList2, Dimensions, ProjectDimensions
from project.models import Project, Post, Speech, Feedlinks, ChangingOnlineSentiment
from reports.models import Templates, RegularReport
from widgets.common_widget.filters_for_widgets import posts_agregator, post_agregator_with_dimensions
from alerts.models import Alert
from accounts.models import Profile
from deep_translator import GoogleTranslator
from countries_plus.models import Country
from rest_framework.views import APIView
from sentence_transformers import util
from ml_components.models import MlCategory
from ..serializers import UserSerializer, UserUpdateSerializer
from ..serializers import CountrySerializer, SpeechSerializer, PostsSerializer
from ..serializers import FeedlinksSerializer, WidgetsListSerializer, ClippingFeedContentWidgetSerializer
from ..serializers import ProjectDimensionsListSerializer, DimensionsSerializer, ProjectDimensionsSerializer
from ..serializers import AlertCreateSerializer, AlertsSerializer, RegisterSerializer, ProfileUserSerializer
from ..serializers import TemplatesSerializer, RegularReportCreateSerializer
from api.services.search_service import SearchService
import numpy as np
import json
import re
import environ

env = environ.Env()


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class UserDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoggedInUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)


def exclude_keywords_posts(posts, exceptions):
    to_be_removed = []
    for post in posts:
        for word in exceptions:
            if word in post.entry_title:
                to_be_removed.append(post.id)
                break
    posts = posts.exclude(id__in=to_be_removed)
    return posts


def additional_keywords_posts(posts, additions):
    for word in additions:
        posts = posts.filter(entry_title__icontains=word)
    return posts


def data_range_posts_for_24(start_date, end_date):
    interval = [start_date, end_date]
    posts = Post.objects.filter(entry_published__range=interval)
    return posts


def search(request):
    res = SearchService().execute(request)
    return JsonResponse(res, safe=False)


def classification(post, themes):
    if post.summary_vector != []:
        categories_list = list(themes.values_list('category_title', flat=True))
        categories_vector = np.array([themes.values_list('category_vector', flat=True)]).reshape(len(themes), 384)
        cosine_scores = util.cos_sim(post.summary_vector[0], categories_vector)
        cosine_scores = cosine_scores.reshape(1, -1)[0]
        answer = cosine_scores.argsort(descending=True)[0]
        return categories_list[int(answer)]
    else:
        return 'The post matrix was not calculated.'


class CountriesList(ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']


class SpeechesList(ListAPIView):
    serializer_class = SpeechSerializer
    queryset = Speech.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^language']


class AuthorList(ListAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.values('entry_author').distinct()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^entry_author']


class SourceList(ListAPIView):
    serializer_class = FeedlinksSerializer
    queryset = Feedlinks.objects.values('source1').distinct()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^source1']


class ProjectWidgetsAPIView(RetrieveAPIView):
    serializer_class = WidgetsListSerializer

    def get_object(self):
        return WidgetsList2.objects.get(project_id=self.kwargs['pk'])


class UpdateProjectsWidgetsAPIView(UpdateAPIView):
    serializer_class = WidgetsListSerializer

    def get_object(self):
        return WidgetsList2.objects.get(project_id=self.kwargs['pk'])


class ClippingFeedContentWidgetDelete(DestroyAPIView):
    serializes_class = ClippingFeedContentWidgetSerializer

    def get_object(self):
        return ClippingFeedContentWidget.objects.filter(post_id=self.kwargs['post_pk'], project_id=self.kwargs['proj_pk'])


class ClippingFeedContentWidgetCreate(ListCreateAPIView):
    serializer_class = ClippingFeedContentWidgetSerializer
    queryset = ClippingFeedContentWidget.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProjectDimensionsList(ListAPIView):
    serializer_class = ProjectDimensionsListSerializer

    def get_queryset(self):
        return ProjectDimensions.objects.filter(project_id=self.kwargs['pk'])


class DimensionsViewSet(viewsets.ModelViewSet):
    serializer_class = DimensionsSerializer
    queryset = Dimensions.objects.all().order_by('title')


class ProjectDimensionsCreate(ListCreateAPIView):
    serializer_class = ProjectDimensionsSerializer
    queryset = ProjectDimensions.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data, many=True)
        ProjectDimensions.objects.filter(project_id=kwargs['pk']).delete()
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TemplatesViewSet(viewsets.ModelViewSet):
    serializer_class = TemplatesSerializer
    queryset = Templates.objects.all()


def dimension_authors(request, pk):
    first_letters = request.body
    project = get_object_or_404(Project, pk=pk)
    posts = posts_agregator(project)
    authors = posts.filter(entry_author__startswith=first_letters).order_by('entry_author').values('entry_author').distinct()
    authors_list = list(authors)
    return JsonResponse(authors_list, safe=False)


def dimension_languages(request, pk):
    project = get_object_or_404(Project, pk=pk)
    posts = posts_agregator(project)
    languages = posts.values('feed_language__language').distinct()
    languages_list = list(languages)
    return JsonResponse(languages_list, safe=False)


def dimension_countries(requset, pk):
    project = get_object_or_404(Project, pk=pk)
    posts = posts_agregator(project)
    countries = posts.values('feedlink__country').distinct()
    countries_list = list(countries)
    return JsonResponse(countries_list, safe=False)


def dimension_sources(requset, pk):
    project = get_object_or_404(Project, pk=pk)
    posts = posts_agregator(project)
    sources = posts.values('feedlink__source1').distinct()
    sources_list = list(sources)
    return JsonResponse(sources_list, safe=False)


class ListAuthorsInProject(generics.ListAPIView):
    serializer_class = PostsSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        project = get_object_or_404(Project, pk=pk)
        posts = posts_agregator(project)
        queryset = posts.values('entry_author').order_by('entry_author').distinct()
        return queryset


class AlertsViewSet(viewsets.ModelViewSet):
    serializer_class = AlertCreateSerializer
    queryset = Alert.objects.all()


class DepAlertsViewSet(ListAPIView):
    serializer_class = AlertsSerializer

    def get_queryset(self):
        return Alert.objects.filter(department_id=self.kwargs['pk'])


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class CompanyUsersView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(user_profile__department=self.kwargs['pk']).order_by('first_name')


class ProfileViewSet(RetrieveUpdateAPIView):
    serializer_class = ProfileUserSerializer
    lookup_field = 'user__email'

    def get_queryset(self):
        return Profile.objects.filter(user__email=self.kwargs['user__email'])


class RegularReportCreateViewSet(viewsets.ModelViewSet):
    serializer_class = RegularReportCreateSerializer
    queryset = RegularReport.objects.all()


class ProfilesViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileUserSerializer
    queryset = Profile.objects.all()


def widgets_map(request):
    res = variables.WIDGETS_MAP
    return JsonResponse(res)


def change_online_sentiment(request, pk, department_pk, sentiment):
    try:
        updated_values = {'sentiment': sentiment}
        ChangingOnlineSentiment.objects.update_or_create(post_id=pk, department_id=department_pk, defaults=updated_values)
    except:
        return HttpResponse(status=406)
    return HttpResponse(status=201)


def change_post_sentiment(post, dict_changing):
    if post['id'] in dict_changing:
        new_sentiment = dict_changing[post['id']]
        post['sentiment'] = new_sentiment
    return post


def change_post_source_name(post):
    src = post['feedlink__source1']
    post['feedlink__source1'] = src if '<img' not in str(src) else re.findall('alt="(.*)"', src)[0]
    return post


def add_post_category(post, themes):
    category = classification(Post.objects.get(pk=post['id']), themes)
    target_lang = post['feed_language__language'].lower()
    try:
        category = GoogleTranslator(source='en', target=target_lang).translate(category)
    except:
        pass
    post['category'] = category
    return post


def posts_values(posts):
    return posts.values(
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
        'category',
    )


def project_posts(request, pk):
    body = json.loads(request.body)
    posts_per_page = body['posts_per_page']
    page_number = body['page_number']
    dep_id = body['department_id']
    posts = post_agregator_with_dimensions(Project.objects.get(id=pk))
    posts = posts_values(posts)
    p = Paginator(posts, posts_per_page)
    posts_list = list(p.page(page_number))
    department_changing = ChangingOnlineSentiment.objects.filter(department_id=dep_id).values()
    dict_changing = {x['post_id']: x['sentiment'] for x in department_changing}
    themes = MlCategory.objects.all()
    for post in posts_list:
        post = change_post_sentiment(post, dict_changing)
        post = change_post_source_name(post)
        post = add_post_category(post, themes)
    res = {'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list}
    return JsonResponse(res, safe=False)


def keywords_posts(keys, posts):
    keys = [f'%%{key.upper()}%%' for key in keys]
    posts = posts.extra(
        where=['UPPER(entry_title) LIKE ANY(%s) OR UPPER(entry_summary) LIKE ANY(%s)'],
        params=[keys, keys]
    )
    return posts


def filter_with_dimensions(posts, body):
    country_dimensions = body['country_dimensions']
    language_dimensions = body['language_dimensions']
    source_dimensions = body['source_dimensions']
    author_dimensions = body['author_dimensions']
    sentiment_dimensions = body['sentiment_dimensions']

    if country_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__country=country) for country in country_dimensions]))
    if language_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(feed_language__language=language) for language in language_dimensions]))
    if source_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__source1=source) for source in source_dimensions]))
    if author_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(entry_author=author) for author in author_dimensions]))
    if sentiment_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sentiment) for sentiment in sentiment_dimensions]))

    return posts


def posts_values(posts):
    return posts.values(
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
        'category',
    )


def change_post_sentiment(post, dict_changing):
    if post['id'] in dict_changing:
        new_sentiment = dict_changing[post['id']]
        post['sentiment'] = new_sentiment
    return post


def filter_with_constructor(body, posts):
    keys = body['keywords']
    exceptions = body['exceptions']
    additions = body['additions']
    country = body['country']
    language = body['language']
    source = body['source']
    author = body['author']
    sentiment = body['sentiment']
    posts = keywords_posts(keys, posts)

    if additions:
        posts = additional_keywords_posts(posts, additions)
    if exceptions:
        posts = exclude_keywords_posts(posts, exceptions)
    if country:
        posts = posts.filter(feedlink__country=country)
    if language:
        posts = posts.filter(feed_language__language=language)
    if source:
        posts = posts.filter(feedlink__source1=source)
    if author:
        posts = posts.filter(entry_author=author)
    if sentiment:
        posts = posts.filter(sentiment=sentiment)

    return posts
