from .views import *
from twenty_four_seven import views
from rest_framework import routers
from django.urls import path


router = routers.SimpleRouter()

urlpatterns = []

router.register('workspaces', WorkspaceTwentyFourSevenViewSet, basename='tfs_workspaces')
router.register('projects', TwentyFourSevenProjectViewSet, basename='tfs_projects')
router.register('items', ItemViewSet, basename='tfs_items')

urlpatterns += router.urls
