from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from tweet_binder.models import TweetBinderPost
from .widgets.dashboard.most_engaging_media_types import *
from .widgets.dashboard.most_frequent_media_types import *
from .widgets.dashboard.most_frequent_post_types import *
from .widgets.dashboard.most_engaging_post_types import *
from .widgets.optimization.optimal_post_length import *
from .widgets.dashboard.profile_timeline import *
from .widgets.dashboard.follower_growth import *
from .widgets.dashboard.summary import *
from django.shortcuts import render
from rest_framework import viewsets
from .widgets.dimensions import *
from .serializers import *
from .models import *


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

def optimal_post_length_widgets(request, pk, widget_pk):
    return optimal_post_length(pk, widget_pk)

def list_of_profile_handle(request):
    profile_handles = TweetBinderPost.objects.order_by(
        "user_alias").values("user_alias", "user_picture").distinct()
    return JsonResponse(list(profile_handles), safe=False)
