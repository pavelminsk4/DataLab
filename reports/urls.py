from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('instantly_report/<int:proj_pk>/', views.online_instantly_report, name="instantly_report"),
    path('social_instantly_report/<int:proj_pk>/', views.social_instantly_report, name='social_instantly_report'),

    path('soc_top_locations_screenshot/<int:proj_pk>/', views.social_top_locations_screenshot, name='soc_top_locations_screenshot'),
    path('soc_top_authors_screenshot/<int:proj_pk>/', views.social_top_authors_screenshot, name='soc_top_authors_screenshot'),
    path('soc_top_languages_screenshot/<int:proj_pk>/', views.social_top_languages_screenshot, name='soc_top_languages_screenshot'),
    path('soc_sentiment_diagram_screenshot/<int:proj_pk>/', views.social_sentiment_diagram_screenshot, name='soc_sentiment_diagram_screenshot'),
    path('soc_sentiment_authors_screenshot/<int:proj_pk>/', views.social_sentiment_authors_screenshot, name='soc_sentiment_authors_screenshot'),
    path('soc_sentiment_languages_screenshot/<int:proj_pk>/', views.social_sentiment_languages_screenshot, name='soc_sentiment_languages_screenshot'),
    path('soc_sentiment_locations_screenshot/<int:proj_pk>/', views.social_sentiment_locations_screenshot, name='soc_sentiment_locations_screenshot'),
    path('soc_content_volume_top_authors_screenshot/<int:proj_pk>/', views.social_content_volume_top_authors_screenshot, name='soc_content_volume_top_authors_screenshot'),
    path('soc_content_volume_top_languages_screenshot/<int:proj_pk>/', views.social_content_volume_top_languages_screenshot, name='soc_content_volume_top_languages_screenshot'),
    path('soc_content_volume_top_locations_screenshot/<int:proj_pk>/', views.social_content_volume_top_locations_screenshot, name='soc_content_volume_top_locations_screenshot'),
    path('soc_content_volume_screenshot/<int:proj_pk>/', views.social_content_volume_screenshot, name='soc_content_volume_screenshot'),
]

router.register('regular_reports', views.RegularReportViewSet, 'regular_reports')

urlpatterns += router.urls
