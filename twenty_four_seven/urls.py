from django.urls import path
from rest_framework_nested import routers
from .views import items, translator, others


app_name = 'twenty_four_seven'

urlpatterns = [
    path('translator/', translator.translator, name='translator'),
    path('whatsapp/', others.whatsapp, name='whatsapp'),
    path('summary/<int:item_pk>/', translator.summary, name='summary'),
]

router = routers.SimpleRouter()
router.register('workspaces', others.WorkspaceTwentyFourSevenViewSet, basename='tfs_workspaces')
router.register('projects', others.TwentyFourSevenProjectViewSet, basename='tfs_projects')

items_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
items_router.register(r'items', items.ItemViewSet, basename='project-items')
router.register('related_content', others.RelatedContentViewSet, basename='tfs_related_content')

urlpatterns += router.urls
urlpatterns += items_router.urls
