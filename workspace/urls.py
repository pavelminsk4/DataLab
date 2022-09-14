from django.urls import path,include

from workspace import views

app_name = 'workspace'

urlpatterns = [
  path('create', views.create, name='create'),
  path('<pk>', views.detail, name='workspace_detail'),
]
