from django.urls import path,include

from . import views

app_name = 'project'

urlpatterns = [
  path('', views.index, name='index'),
  path('create', views.create, name='create'),
  path('<pk>/delete', views.delete, name='delete'),
  path('<pk>', views.detail.as_view(), name='project_detail'),
]
