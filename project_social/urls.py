from django.urls import path
from . import views
from rest_framework import routers
from .views import *

app_name = 'project_social'

urlpatterns = [
  path("social_workspaces/",views.WorkspaceSocialList.as_view(),name="social_workspaces_list"),
  path("social_workspaces/create/", views.WorkspaceSocialCreate.as_view(),name="social_workspaces_create"),
  path("social_workspaces/update/<int:pk>/",views.WorkspaceSocialUpdate.as_view(),name="social_workspaces_update"),
  path("social_workspaces/delete/<int:pk>/",views.WorkspaceSocialDelete.as_view(),name="social_workspaces_delete"),
]
