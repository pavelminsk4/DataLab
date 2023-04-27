from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
  path('instantly_report/<int:proj_pk>/', views.online_instantly_report, name="instantly_report"),
  path('social_instantly_report/<int:proj_pk>/', views.social_instantly_report, name='social_instantly_report'),
  
  path('social/summary_screenshot/<int:proj_pk>/', views.social_summary_screenshot, name='social_summary_screenshot'),
  path('social/top_locations_screenshot/<int:proj_pk>/', views.social_top_locations_screenshot, name='top_locations_screenshot'),
  path('social/top_authors_screenshot/<int:proj_pk>/', views.social_top_authors_screenshot, name='top_authors_screenshot'),
  ]

router.register('regular_reports', views.RegularReportViewSet, 'regular_reports')

urlpatterns += router.urls
