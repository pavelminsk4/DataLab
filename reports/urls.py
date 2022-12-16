from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
  path('instantly_report', views.instantly_report, name="instantly_report"),
  ]

router.register('regular_reports', views.RegularReportViewSet, 'regular_reports')

urlpatterns += router.urls
