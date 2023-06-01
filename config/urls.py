from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="List of Anova API endpoints",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('dashboard', include('core.urls')),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('projects/', include('project.urls')),
    path('api/', include('api.urls')),
    path('api/widgets/', include('widgets.urls', namespace='widgets')),
    path('api/social/', include('project_social.urls')),
    path('api/account_analysis/', include('account_analysis.urls')),
    path('api/twenty_four_seven/', include('twenty_four_seven.urls')),
    path('api/comparison/', include('comparison.urls')),
    path('workspace/', include('workspace.urls', namespace='workspace')),
    path('api/reports/<int:dep_pk>/', include('reports.urls')),
    path('', include('tweet_binder.urls')),
    re_path('^.*$', TemplateView.as_view(template_name="index.html")),
]
