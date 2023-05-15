from .views import *
from twenty_four_seven import views
from rest_framework import routers
from django.urls import path


router = routers.SimpleRouter()

urlpatterns = [
    path('twenty_four_seven_workspaces/',views.WorkspaceTwentyFourSevenlList.as_view(),name="twenty_four_seven_workspaces_list"),
    path('twenty_four_seven_workspaces/create/', views.WorkspaceTwentyFourSevenCreate.as_view(),name="twenty_four_seven_workspaces_create"),
    path('twenty_four_seven_workspaces/update/<int:pk>/',views.WorkspaceTwentyFourSevenUpdate.as_view(),name="twenty_four_seven_workspaces_update"),
    path('twenty_four_seven_workspaces/delete/<int:pk>/',views.WorkspaceTwentyFourSevenDelete.as_view(),name="twenty_four_seven_workspaces_delete"),    
    path('whatsapp/', views.whatsapp, name='whatsapp'),
]

router.register('projects', TwentyFourSevenProjectViewSet)
router.register('items', ItemViewSet)

urlpatterns += router.urls
