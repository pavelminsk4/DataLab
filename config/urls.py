from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', include('core.urls')),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('projects/', include('project.urls')),
    path('api/', include('api.urls')),
    path('api/widgets', include('widgets.urls', namespace='widgets')),
    path('workspace/', include('workspace.urls', namespace='workspace')),
    path('projects/<int:pk>/reports/', include('reports.urls')),
    re_path('^.*$', TemplateView.as_view(template_name="index.html")),
]
