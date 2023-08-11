from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('instantly_report/<int:proj_pk>/', views.online_instantly_report, name="instantly_report"),
    path('social_instantly_report/<int:proj_pk>/', views.social_instantly_report, name='social_instantly_report'),

    path('soc_summary_screenshot/<int:proj_pk>/', views.social_summary_screenshot, name='soc_summary_screenshot'),
    path('soc_sentiment_screenshot/<int:proj_pk>/', views.social_sentiment_screenshot, name='soc_sentiment_screenshot'),
    path('soc_top_locations_screenshot/<int:proj_pk>/', views.social_top_locations_screenshot, name='soc_top_locations_screenshot'),
    path('soc_top_authors_screenshot/<int:proj_pk>/', views.social_top_authors_screenshot, name='soc_top_authors_screenshot'),
    path('soc_top_languages_screenshot/<int:proj_pk>/', views.social_top_languages_screenshot, name='soc_top_languages_screenshot'),
    path('soc_sentiment_diagram_screenshot/<int:proj_pk>/', views.social_sentiment_diagram_screenshot, name='soc_sentiment_diagram_screenshot'),
    path('soc_sentiment_number_of_results_screenshot/<int:proj_pk>/', views.social_sentiment_number_of_results_screenshot, name='soc_sentiment_number_of_results_screenshot'),
    path('soc_sentiment_authors_screenshot/<int:proj_pk>/', views.social_sentiment_authors_screenshot, name='soc_sentiment_authors_screenshot'),
    path('soc_sentiment_languages_screenshot/<int:proj_pk>/', views.social_sentiment_languages_screenshot, name='soc_sentiment_languages_screenshot'),
    path('soc_sentiment_by_gender_screenshot/<int:proj_pk>/', views.social_sentiment_gender_screenshot, name='soc_sentiment_by_gender_screenshot'),
    path('soc_sentiment_locations_screenshot/<int:proj_pk>/', views.social_sentiment_locations_screenshot, name='soc_sentiment_locations_screenshot'),
    path('soc_content_volume_top_authors_screenshot/<int:proj_pk>/', views.social_content_volume_top_authors_screenshot, name='soc_content_volume_top_authors_screenshot'),
    path('soc_content_volume_top_languages_screenshot/<int:proj_pk>/', views.social_content_volume_top_languages_screenshot, name='soc_content_volume_top_languages_screenshot'),
    path('soc_content_volume_top_locations_screenshot/<int:proj_pk>/', views.social_content_volume_top_locations_screenshot, name='soc_content_volume_top_locations_screenshot'),
    path('soc_content_volume_screenshot/<int:proj_pk>/', views.social_content_volume_screenshot, name='soc_content_volume_screenshot'),
    path('soc_top_keywords_screenshot/<int:proj_pk>/', views.social_top_keywords_screenshot, name='soc_top_keywords_screenshot'),
    path('soc_top_authors_by_gender_screenshot/<int:proj_pk>/', views.social_top_authors_by_gender_screenshot, name='soc_top_authors_by_gender_screenshot'),
    path('soc_authors_by_gender_screenshot/<int:proj_pk>/', views.social_authors_by_gender_screenshot, name='soc_authors_by_gender_screenshot'),
    path('soc_authors_by_language_screenshot/<int:proj_pk>/', views.social_authors_by_language_screenshot, name='soc_authors_by_language_screenshot'),
    path('soc_authors_by_location_screenshot/<int:proj_pk>/', views.social_authors_by_location_screenshot, name='soc_authors_by_location_screenshot'),
    path('soc_gender_by_location_screenshot/<int:proj_pk>/', views.social_gender_by_location_screenshot_screenshot, name='soc_gender_by_location_screenshot'),
    path('soc_keywords_by_location_screenshot/<int:proj_pk>/', views.social_keywords_by_location_screenshot, name='soc_keywords_by_location_screenshot'),
    path('soc_languages_by_location_screenshot/<int:proj_pk>/', views.social_languages_by_location_screenshot, name='soc_languages_by_location_screenshot'),
    path('soc_top_sharing_sources_screenshot/<int:proj_pk>/', views.social_top_sharing_sources_screenshot, name='soc_top_sharing_sources_screenshot'),
    path('soc_gender_volume_screenshot/<int:proj_pk>/', views.social_gender_volume_screenshot, name='soc_gender_volume_screenshot'),
    path('soc_sentiment_top_keywords_screenshot/<int:proj_pk>/', views.social_sentiment_top_keywords_screenshot, name='soc_sentiment_top_keywords_screenshot'),
    path('soc_authors_by_sentiment_screenshot/<int:proj_pk>/', views.social_authors_by_sentiment_screenshot, name='soc_authors_by_sentiment_screenshot'),
    
    path('onl_summary_screenshot/<int:proj_pk>/', views.online_summary_screenshot, name='onl_summary_screenshot'),   
]

router.register('regular_reports', views.RegularReportViewSet, 'regular_reports')

urlpatterns += router.urls
