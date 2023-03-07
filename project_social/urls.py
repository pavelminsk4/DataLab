from rest_framework import routers
from django.urls import path
from project_social import views
from .models import *
from .views import *

app_name = 'project_social'

router = routers.SimpleRouter()

urlpatterns = [
  path("social_workspaces/",views.WorkspaceSocialList.as_view(),name="social_workspaces_list"),
  path("social_workspaces/create/", views.WorkspaceSocialCreate.as_view(),name="social_workspaces_create"),
  path("social_workspaces/update/<int:pk>/",views.WorkspaceSocialUpdate.as_view(),name="social_workspaces_update"),
  path("social_workspaces/delete/<int:pk>/",views.WorkspaceSocialDelete.as_view(),name="social_workspaces_delete"),
  path("twitter_post_search/", views.twitter_posts_search,name="twitter_posts_search"),
]

router.register('projects', ProjectsSotialViewSet)

urlpatterns += router.urls
