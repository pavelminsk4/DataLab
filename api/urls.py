from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

urlpatterns = [
  path('auth/', include('drf_multitokenauth.urls', namespace='multi_token_auth')),
  # User
  path("users/",views.UserList.as_view(),name="users_list"),
  path('logged_in_user', views.LoggedInUserView.as_view(), name='logged_in_user'),
  path("user/create/", views.UserCreate.as_view(),name="user_create"),
  path("user/update/<int:pk>/",views.UserUpdate.as_view(),name="user_update"),
  path("user/delete/<int:pk>/",views.UserDelete.as_view(),name="user_delete"),
  # Widgets List
  path('projects/<int:pk>/widgets_list', views.ProjectWidgetsAPIView.as_view(), name='widgets_list'),
  path('projects/<int:pk>/widgets_list/update', views.UpdateProjectsWidgetsAPIView.as_view(), name='update_widgets_list'),
  # Workspace
  path("workspaces/",views.WorkspaceList.as_view(),name="workspaces_list"),
  path("workspace/create/", views.WorkspaceCreate.as_view(),name="workspace_create"),
  path("workspace/update/<int:pk>/",views.WorkspaceUpdate.as_view(),name="workspace_update"),
  path("workspace/delete/<int:pk>/",views.WorkspaceDelete.as_view(),name="workspace_delete"),
  path("workspace/<int:pk>", views.SingleWorkspace.as_view(), name="single_workspace"),
  # Search
  path("search", views.search, name='search'),
  # Countries
  path('countries/<str:frst_letters>', views.CountriesList.as_view(), name='countries_list'),
  # Speeches
  path('speeches/<str:frst_letters>', views.SpeechesList.as_view(), name='speeches_list'),
  # Sources
  path('sources', views.sources, name='sources_list'),
  # Authors
  path('authors/<str:frst_letters>', views.AuthorList.as_view(), name='authors_list'),
  # Years range
  path('years', views.years, name='years_range'),
  # ClippingFeedContentWidget
  path('clipping_feed_content_widget/create', views.ClippingFeedContentWidgetCreate.as_view(), name='cl_fd_cont_widg_create'),
  path('projects/<int:proj_pk>/clipping_feed_content_widget/delete/<int:post_pk>', views.ClippingFeedContentWidgetDelete.as_view(), name='cl_fd_cont_widg_delete'),
  # Dimensions
  path('projects/<int:pk>/dimensions', views.ProjectDimensionsList.as_view(), name='project_dimensions_list'), # Selected dimensions for certain project
  path('projects/<int:pk>/dimensions_create', views.ProjectDimensionsCreate.as_view(), name='project_dimensions_create'),
  # Data for dimensions on the widget
  path('projects/<int:pk>/dimension_authors', views.dimension_authors ,name='dim_authors'),
  path('projects/<int:pk>/dimension_languages', views.dimension_languages, name='dim_languages'),
  path('projects/<int:pk>/dimension_countries', views.dimension_countries, name='dim_countries'),
  path('projects/<int:pk>/dimension_sources', views.dimension_sources, name='dim_sources'),
  path('projects/<int:pk>/list_authors', views.ListAuthorsInProject.as_view() ,name='list_authors'),

  #path('projects/<int:pk>/dimension_source', views.dimension_source, name='dim_source'),
  path('departments/<int:pk>/alerts', views.DepAlertsViewSet.as_view(), name='dep_alerts'),
  path('register/', RegisterView.as_view(), name='auth_register'),
  path('company_users/<int:pk>/', CompanyUsersView.as_view(), name='company_users'),
  # Profile
  path('profileuser/<str:user__email>/', ProfileViewSet.as_view(), name='profile_users'),
  # ReportWidgetsList
  path('report_widgets_list', views.widgets_map, name='report_widgets_list'),
  path('change_sentiment/<int:pk>/<int:department_pk>/<str:sentiment>',views.change_sentiment,name='change_sent')
  ]

router.register('dimensions', DimensionsViewSet)
router.register('templates', TemplatesViewSet)
router.register('projects', ProjectsViewSet)
router.register('alerts', AlertsViewSet)
router.register('regularreports', RegularReportCreateViewSet)

urlpatterns += router.urls
