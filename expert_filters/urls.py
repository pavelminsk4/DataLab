from rest_framework import routers
from rest_framework_nested import routers
from expert_filters.views import GroupsViewSet
from expert_filters.views import PresetsViewSet


app_name = 'expert_filters'

router = routers.SimpleRouter()
router.register('presets', PresetsViewSet, basename='presets')
router.register('groups', GroupsViewSet, basename='groups')

urlpatterns = router.urls
