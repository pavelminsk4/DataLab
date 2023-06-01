from .views import *
from rest_framework import routers
from rest_framework_nested import routers


app_name = 'twenty_four_seven'

urlpatterns = []

router = routers.SimpleRouter()
router.register('workspaces', WorkspaceTwentyFourSevenViewSet, basename='tfs_workspaces')
router.register('projects', TwentyFourSevenProjectViewSet, basename='tfs_projects')

items_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
items_router.register(r'items', ItemViewSet, basename='project-items')
router.register('related_content', RelatedContentViewSet, basename='tfs_related_content')

urlpatterns += router.urls
urlpatterns += items_router.urls
