from rest_framework import routers
from account_analysis import views
from django.urls import path
from .models import *
from .views import *

app_name = 'account_analysis'

router = routers.SimpleRouter()

urlpatterns = [
    # ========Workspaces and Progects=========
    path('workspaces/', views.WorkspaceAccountAnalysisList.as_view(), name='account_analysis_workspaces_list'),
    path('workspaces/create/', views.WorkspaceAccountAnalysisCreate.as_view(), name='account_analysis_workspaces_create'),
    path('workspaces/update/<int:pk>/', views.WorkspaceAccountAnalysisUpdate.as_view(), name='account_analysis_workspaces_update'),
    path('workspaces/delete/<int:pk>/', views.WorkspaceAccountAnalysisDelete.as_view(), name='account_analysis_workspaces_delete'),
    # Widgets List
    path('account_analysis_projects/<int:pk>/widgets_list', views.AccountAnalysisProjectWidgetsAPIView.as_view(), name='account_analysis_widgets_list'),
    path('account_analysis_projects/<int:pk>/widgets_list/update', views.UpdateAccountAnalysisProjectsWidgetsAPIView.as_view(), name='update_account_analysis_widgets_list'),
    # =======Widgets======
    path('account_analysis_summary_widget/<int:pk>/<int:widget_pk>', views.account_analysis_summary_widget, name='account_analysis_summary_widget'),
    path('profile_timeline_widget/<int:pk>/<int:widget_pk>', views.profile_timeline_widget, name='profile_timeline_widget'),
    path('most_frequent_post_types_widget/<int:pk>/<int:widget_pk>', views.most_frequent_post_types_widget, name='most_frequent_post_types_widget'),
    path('most_engaging_post_types_widget/<int:pk>/<int:widget_pk>', views.most_engaging_post_types_widget, name='most_engaging_post_types_widget'),
    path('most_frequent_media_types_widget/<int:pk>/<int:widget_pk>', views.most_frequent_media_types_widget, name='most_frequent_media_types_widget'),
    path('most_engaging_media_types_widget/<int:pk>/<int:widget_pk>', views.most_engaging_media_types_widget, name='most_engaging_media_types_widget'),
    path('follower_growth_widget/<int:pk>/<int:widget_pk>', views.follower_growth_widget, name='follower_growth_widget'),
    path('optimal_post_length_widget/<int:pk>/<int:widget_pk>', views.optimal_post_length_widget, name='optimal_post_length_widget'),
    path('top_hashtags_widget/<int:pk>/<int:widget_pk>', views.top_hashtags_widget, name='top_hashtags'),
    path('optimal_number_of_hashtags_widget/<int:pk>/<int:widget_pk>', views.optimal_number_of_hashtags_widget, name='optimal_number_of_hashtags'),
    path('average_engagements_by_day_widget/<int:pk>/<int:widget_pk>', views.average_engagements_by_day_widget, name='average_engagements_by_day'),
    path('optimal_post_time_widget/<int:pk>/<int:widget_pk>', views.optimal_post_time_widget, name='optimal_post_time'),
    path('top_posts_by_engagements_widget/<int:pk>/<int:widget_pk>', views.top_posts_by_engagements_widget, name='top_posts_by_engagements'),
    path('best_times_to_post_widget/<int:pk>/<int:widget_pk>', views.best_times_to_post_widget, name='best_times_to_post'),
    path('mention_timeline_widget/<int:pk>/<int:widget_pk>', views.mention_timeline_widget, name='mention_timeline'),
    path('dimensions_for_each_widgets/<int:project_pk>/<int:widget_pk>', views.dimensions_for_each_widgets, name='dimensions_for_each_widgets'),
    # =======Profile Handle======
    path('list_of_profile_handle', views.list_of_profile_handle, name='list_of_profile_handle'),
    # =======Search========
    path('search_posts/<int:project_pk>', views.search_posts, name='search_posts'),
]

router.register('projects', ProjectsAccountAnalysisViewSet)

urlpatterns += router.urls
