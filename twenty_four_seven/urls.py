from twenty_four_seven.views import WorkspaceTwentyFourSevenViewSet
from twenty_four_seven.views import TwentyFourSevenProjectViewSet
from twenty_four_seven.views import RelatedContentViewSet
from twenty_four_seven.views import ItemViewSet
from twenty_four_seven.views import translator
from twenty_four_seven.views import whatsapp
from twenty_four_seven.views import summary
from rest_framework import routers
from rest_framework_nested import routers
from django.urls import path


app_name = 'twenty_four_seven'

urlpatterns = [
    path('translator/', translator, name='translator'),
    path('whatsapp/', whatsapp, name='whatsapp'),
    path('summary/<int:item_pk>/', summary, name='summary'),
]

router = routers.SimpleRouter()
router.register('workspaces', WorkspaceTwentyFourSevenViewSet, basename='tfs_workspaces')
router.register('projects', TwentyFourSevenProjectViewSet, basename='tfs_projects')

items_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
items_router.register(r'items', ItemViewSet, basename='project-items')
router.register('related_content', RelatedContentViewSet, basename='tfs_related_content')

urlpatterns += router.urls
urlpatterns += items_router.urls
