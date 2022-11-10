from django.urls import path
from . import views

urlpatterns = [
  path("instantly_report",views.instantly_report ,name="instantly_report"),  
  ]
