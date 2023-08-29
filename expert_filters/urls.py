from rest_framework import routers
from rest_framework_nested import routers
from expert_filters.views import GroupsViewSet
from expert_filters.views import PresetsViewSet


app_name = 'expert_filters'

urlpatterns = []

router = routers.SimpleRouter()
router.register(r'groups', GroupsViewSet, basename='expert_filters_groups')

preset_router = routers.NestedDefaultRouter(router, r'groups', lookup='group')
preset_router.register(r'presets', PresetsViewSet, basename='group-presets')

urlpatterns += router.urls
urlpatterns += preset_router.urls
