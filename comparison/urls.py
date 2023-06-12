from rest_framework_nested.routers import NestedSimpleRouter
from comparison.views import WorkspaceComparisonViewSet
from comparison.views import ProjectComparisonViewSet
from comparison.views import ItemComparisonViewSet
from rest_framework.routers import SimpleRouter
from comparison.views import get_projects
from django.urls import path

app_name = 'comparison'

urlpatterns = [
    path('projects_list', get_projects, name='projects_list'),
]

router = SimpleRouter()
router.register('workspaces', WorkspaceComparisonViewSet, basename='cmpr_workspaces')

projects_router = NestedSimpleRouter(router, 'workspaces', lookup='workspace')
projects_router.register('projects', ProjectComparisonViewSet, basename='workspace_projects')

items_router = NestedSimpleRouter(projects_router, 'projects', lookup='project')
items_router.register('items', ItemComparisonViewSet, basename='project_items')

urlpatterns += router.urls
urlpatterns += projects_router.urls
urlpatterns += items_router.urls
