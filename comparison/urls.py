from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework.routers import SimpleRouter
from django.urls import path

from comparison.views import WorkspaceComparisonViewSet
from comparison.views import ProjectComparisonViewSet
from comparison.views import ItemComparisonViewSet
from comparison.views import get_influencers_feature
from comparison.views import get_demography_feature
from comparison.views import get_sentiment_feature
from comparison.views import get_summary_feature
from comparison.views import get_projects

app_name = 'comparison'

urlpatterns = [
    path('projects_list', get_projects, name='projects_list'),
    path('projects/<int:pk>/summary', get_summary_feature, name='summary'),
    path('projects/<int:pk>/sentiment', get_sentiment_feature, name='sentiment'),
    path('projects/<int:pk>/demography', get_demography_feature, name='demography'),
    path('projects/<int:pk>/influencers', get_influencers_feature, name='influencers'),
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
