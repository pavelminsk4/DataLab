from rest_framework import routers
from django.urls import path
from project_social import views
from .models import *
from .views import *

app_name = 'project_social'

router = routers.SimpleRouter()

urlpatterns = [
  #========Workspaces and Progects=========  
  path("social_workspaces/",views.WorkspaceSocialList.as_view(),name="social_workspaces_list"),
  path("social_workspaces/create/", views.WorkspaceSocialCreate.as_view(),name="social_workspaces_create"),
  path("social_workspaces/update/<int:pk>/",views.WorkspaceSocialUpdate.as_view(),name="social_workspaces_update"),
  path("social_workspaces/delete/<int:pk>/",views.WorkspaceSocialDelete.as_view(),name="social_workspaces_delete"),
  path("twitter_post_search/", views.twitter_posts_search,name="twitter_posts_search"),
  #========Widgets========
  path('social_summary_widget/<int:pk>/<int:widget_pk>', views.social_summary_widget, name='social_summary_widget'),
  #========Widgets List========
  path('projects/<int:pk>/widgets_list', views.ProjectSocialWidgetsAPIView.as_view(), name='social_widgets_list'),
  path('projects/<int:pk>/widgets_list/update', views.UpdateSocialProjectsWidgetsAPIView.as_view(), name='update_social_widgets_list'),
]

router.register('projects', ProjectsSotialViewSet)

urlpatterns += router.urls
