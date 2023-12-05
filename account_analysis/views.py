from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from tweet_binder.models import TweetBinderPost
from django.core.paginator import Paginator
from .widgets.optimization.mentions.average_engagements_by_day_for_mentions import *
from .widgets.dashboard.mentions.most_frequent_mention_media_types import *
from .widgets.dashboard.mentions.top_mentions_by_engagements import *
from .widgets.optimization.mentions.audience_mention_time import *
from .widgets.optimization.optimal_number_of_hashtags import *
from .widgets.optimization.average_engagements_by_day import *
from .widgets.dashboard.mentions.mention_sentiment import *
from .widgets.dashboard.mentions.mention_timeline import *
from .widgets.dashboard.most_engaging_media_types import *
from .widgets.dashboard.most_frequent_media_types import *
from .widgets.dashboard.mentions.mention_summary import *
from .widgets.dashboard.top_posts_by_engagements import *
from .widgets.dashboard.most_frequent_post_types import *
from .widgets.dashboard.most_engaging_post_types import *
from .widgets.optimization.optimal_post_length import *
from .widgets.optimization.best_times_to_post import *
from .widgets.optimization.optimal_post_time import *
from .widgets.optimization.top_hashtags import *
from .widgets.dashboard.profile_timeline import *
from .widgets.dashboard.follower_growth import *
from .widgets.dashboard.summary import *
from rest_framework import viewsets
from .widgets.dimensions import *
from .serializers import *
from .models import *
from .widgets.interactive_widgets import interactive_widgets
from project_social.services.social_search_service import SocialSearchService
from project_social.models import ChangingTweetbinderSentiment
from common.utils.change_social_sentiment import ChangeSocialSentiment


class ProjectsAccountAnalysisViewSet(viewsets.ModelViewSet):
    queryset = ProjectAccountAnalysis.objects.all()
    serializer_class = ProjectAccountAnalysisSerializer


class WorkspaceAccountAnalysisList(ListAPIView):
    serializer_class = WorkspaceAccountAnalysisSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return WorkspaceAccountAnalysis.objects.filter(members=user)

        return WorkspaceAccountAnalysis.objects.none()


class AccountAnalysisProjectWidgetsAPIView(RetrieveAPIView):
    serializer_class = WidgetsListSerializer

    def get_object(self):
        return AccountAnalysisWidgetsList.objects.get(project_id=self.kwargs['pk'])


class UpdateAccountAnalysisProjectsWidgetsAPIView(UpdateAPIView):
    serializer_class = WidgetsListSerializer

    def get_object(self):
        return AccountAnalysisWidgetsList.objects.get(project_id=self.kwargs['pk'])


class WorkspaceAccountAnalysisCreate(CreateAPIView):
    queryset = WorkspaceAccountAnalysis.objects.all()
    serializer_class = WorkspaceCreateSerializer


class WorkspaceAccountAnalysisUpdate(UpdateAPIView):
    queryset = WorkspaceAccountAnalysis.objects.all()
    serializer_class = WorkspaceAccountAnalysisSerializer


class WorkspaceAccountAnalysisDelete(DestroyAPIView):
    queryset = WorkspaceAccountAnalysis.objects.all()
    serializer_class = WorkspaceAccountAnalysisSerializer


def account_analysis_summary_widget(request, pk, widget_pk):
    return account_analysis_summary(pk, widget_pk)


def dimensions_for_each_widgets(request, pk, widget_pk):
    return dimensions_for_each(pk, widget_pk)


def profile_timeline_widget(request, pk, widget_pk):
    return profile_timeline(request, pk, widget_pk)


def most_frequent_post_types_widget(request, pk, widget_pk):
    return most_frequent_post_types(pk, widget_pk)


def most_engaging_post_types_widget(request, pk, widget_pk):
    return most_engaging_post_types(pk, widget_pk)

def most_frequent_media_types_widget(request, pk, widget_pk):
    return most_frequent_media_types(pk, widget_pk)

def most_engaging_media_types_widget(request, pk, widget_pk):
    return most_engaging_media_types(pk, widget_pk)

def follower_growth_widget(request, pk, widget_pk):
    return follower_growth(request, pk, widget_pk)

def optimal_post_length_widget(request, pk, widget_pk):
    return optimal_post_length(pk, widget_pk)

def top_hashtags_widget(request, pk, widget_pk):
    return top_hashtags(pk, widget_pk)

def optimal_number_of_hashtags_widget(request, pk, widget_pk):
    return optimal_number_of_hashtags(pk, widget_pk)

def average_engagements_by_day_widget(request, pk, widget_pk):
    return average_engagements_by_day(pk, widget_pk)

def optimal_post_time_widget(request, pk, widget_pk):
    return optimal_post_time(pk, widget_pk)

def top_posts_by_engagements_widget(request, pk, widget_pk):
    return top_posts_by_engagements(pk, widget_pk)

def best_times_to_post_widget(request, pk, widget_pk):
    return best_times_to_post(pk, widget_pk)

def mention_timeline_widget(request, pk, widget_pk):
    return mention_timeline(request, pk, widget_pk)

def most_frequent_mention_media_types_widget(request, pk, widget_pk):
    return most_frequent_mention_media_types(pk, widget_pk)

def mention_sentiment_widget(request, pk, widget_pk):
    return mention_sentiment(pk, widget_pk)

def top_mentions_by_engagements_widget(request, pk, widget_pk):
    return top_mentions_by_engagements(pk, widget_pk)

def mention_summary_widget(request, pk, widget_pk):
    return mention_summary(pk, widget_pk)

def audience_mention_time_widget(request, pk, widget_pk):
    return audience_mention_time(pk, widget_pk)

def average_engagements_by_day_for_mentions_widget(request, pk, widget_pk):
    return average_engagements_by_day_for_mentions(pk, widget_pk)

def interactive_data_for_widgets(request, project_pk, widget_pk):
  return interactive_widgets(request, project_pk, widget_pk)

def search_posts(request, project_pk):
    body = json.loads(request.body)
    posts_per_page = body['posts_per_page']
    page_number = body['page_number']
    project = ProjectAccountAnalysis.objects.get(id=project_pk)
    department_id = request.user.user_profile.department
    department_changing = ChangingTweetbinderSentiment.objects.filter(department_id=department_id).values()
    dict_changing = {x['tweet_post_id']: x['sentiment'] for x in department_changing}
    posts = posts_aggregator(project).filter(user_alias=project.profile_handle)
    return calculate(posts, posts_per_page, page_number, dict_changing)

def search_posts_mentions(request, project_pk):
    body = json.loads(request.body)
    posts_per_page = body['posts_per_page']
    page_number = body['page_number']
    project = ProjectAccountAnalysis.objects.get(id=project_pk)
    department_id = request.user.user_profile.department
    department_changing = ChangingTweetbinderSentiment.objects.filter(department_id=department_id).values()
    dict_changing = {x['tweet_post_id']: x['sentiment'] for x in department_changing}
    posts = posts_aggregator(project)
    posts = posts.filter(text__icontains=f'@{project.profile_handle}')
    return calculate(posts, posts_per_page, page_number, dict_changing)

def calculate(posts, posts_per_page, page_number, dict_changing):
    posts = posts.annotate(engagements=Sum(F('count_favorites') + F('count_totalretweets')))
    posts = posts.values('id',
                         'post_id',
                         'type',
                         'inreplyto',
                         'images',
                         'user_picture',
                         'text',
                         'sentiment',
                         'date',
                         'count_totalretweets',
                         'count_replies',
                         'count_favorites',
                         'engagements',
                         'user_alias',
                         'user_name',
                         'images')
    posts = list(posts)
    for p in posts:
        p['link'] = f'https://twitter.com/user/status/{p["post_id"]}'
        p = ChangeSocialSentiment().change_sentiment(p, dict_changing)
    p = Paginator(posts, posts_per_page)
    posts_list=list(p.page(page_number))
    res = { 'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list }
    return JsonResponse(res, safe=False)

def list_of_profile_handle(request):
    body = json.loads(request.body)
    profile_per_page = body['profile_per_page']
    page_number = body['page_number']
    profiles_query = body['profiles_query']
    profile_handles = TweetBinderPost.objects.order_by(
        "user_alias").filter(user_alias__startswith=profiles_query).values("user_alias", "user_picture").distinct()
    p = Paginator(profile_handles, profile_per_page)
    profile_list=list(p.page(page_number))
    res = {'num_pages': p.num_pages, 'num_profiles': p.count, 'profiles_query': profiles_query,  'profiles': profile_list}
    return JsonResponse(res, safe=False)
