from django.urls import path, include
from rest_framework import routers
from .views import project_statuses, users, projects, workspaces, widgets

router = routers.SimpleRouter()

urlpatterns = [
    path('auth/', include('drf_multitokenauth.urls', namespace='multi_token_auth')),
    # User
    path('users/', users.UserList.as_view(), name='users_list'),
    path('logged_in_user', users.LoggedInUserView.as_view(), name='logged_in_user'),
    path('user/create/', users.UserCreate.as_view(), name='user_create'),
    path('user/update/<int:pk>/', users.UserUpdate.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', users.UserDelete.as_view(), name='user_delete'),
    # Widgets List
    path('projects/<int:pk>/widgets_list', users.ProjectWidgetsAPIView.as_view(), name='widgets_list'),
    path('projects/<int:pk>/widgets_list/update', users.UpdateProjectsWidgetsAPIView.as_view(), name='update_widgets_list'),
    # Workspace
    path('workspaces/', workspaces.WorkspaceList.as_view(), name='workspaces_list'),
    path('workspace/create/', workspaces.WorkspaceCreate.as_view(), name='workspace_create'),
    path('workspace/update/<int:pk>/', workspaces.WorkspaceUpdate.as_view(), name='workspace_update'),
    path('workspace/delete/<int:pk>/', workspaces.WorkspaceDelete.as_view(), name='workspace_delete'),
    path('workspace/<int:pk>', workspaces.SingleWorkspace.as_view(), name='single_workspace'),
    # Search
    path('search', users.search, name='search'),
    path('projects/<int:pk>/posts', users.project_posts, name='project_posts'),
    # Countries
    path('countries/<str:frst_letters>', users.CountriesList.as_view(), name='countries_list'),
    # Speeches
    path('speeches/<str:frst_letters>', users.SpeechesList.as_view(), name='speeches_list'),
    # Sources
    path('sources/<str:frst_letters>', users.SourceList.as_view(), name='sources_list'),
    # Authors
    path('authors/<str:frst_letters>', users.AuthorList.as_view(), name='authors_list'),
    # ClippingFeedContentWidget
    path('clipping_feed_content_widget/create', users.ClippingFeedContentWidgetCreate.as_view(), name='cl_fd_cont_widg_create'),
    path('projects/<int:proj_pk>/clipping_feed_content_widget/delete/<int:post_pk>', users.ClippingFeedContentWidgetDelete.as_view(), name='cl_fd_cont_widg_delete'),
    # Dimensions
    path('projects/<int:pk>/dimensions', users.ProjectDimensionsList.as_view(), name='project_dimensions_list'),
    path('projects/<int:pk>/dimensions_create', users.ProjectDimensionsCreate.as_view(), name='project_dimensions_create'),
    # Data for dimensions on the widget
    path('projects/<int:pk>/dimension_authors', users.dimension_authors, name='dim_authors'),
    path('projects/<int:pk>/dimension_languages', users.dimension_languages, name='dim_languages'),
    path('projects/<int:pk>/dimension_countries', users.dimension_countries, name='dim_countries'),
    path('projects/<int:pk>/dimension_sources', users.dimension_sources, name='dim_sources'),
    path('projects/<int:pk>/list_authors', users.ListAuthorsInProject.as_view(), name='list_authors'),

    path('departments/<int:pk>/alerts', users.DepAlertsViewSet.as_view(), name='dep_alerts'),
    path('register/', users.RegisterView.as_view(), name='auth_register'),
    path('company_users/<int:pk>/', users.CompanyUsersView.as_view(), name='company_users'),
    # Profile
    path('profileuser/<str:user__email>/', users.ProfileViewSet.as_view(), name='profile_users'),
    # ReportWidgetsList
    path('report_widgets_list', users.widgets_map, name='report_widgets_list'),
    path('change_online_sentiment/<int:pk>/<int:department_pk>/<str:sentiment>', users.change_online_sentiment, name='change_sent'),
    path('project_statuses/<int:pk>/', project_statuses.ProjectStatusesViewSet.as_view({'patch': 'partial_update'}), name='project_statuses-detail'),

    path('online/<int:project_pk>/<int:widget_pk>/download', widgets.get_csv_online, name='csv_online'),
    path('social/<int:project_pk>/<int:widget_pk>/download', widgets.get_csv_social, name='csv_social'),
    path('accountanalysis/<int:project_pk>/<int:widget_pk>/download', widgets.get_csv_acc_analysis, name='csv_acc_analysis'),
    # Delete post from project.posts
    path('project/<int:project_id>/<int:post_id>/delete', users.delete_post, name='delete_post'),
    #Preview posts
    path('project/preview', users.preview, name='preview_post'),
]

router.register('dimensions', users.DimensionsViewSet)
router.register('templates', users.TemplatesViewSet)
router.register('projects', projects.ProjectsViewSet)
router.register('alerts', users.AlertsViewSet)
router.register('regularreports', users.RegularReportCreateViewSet)
router.register('profiles', users.ProfilesViewSet)

urlpatterns += router.urls
