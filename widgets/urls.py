from django.urls import path

from . import views

app_name = 'widgets'

urlpatterns = [
  path('sentiment_top_10_languages_widget/<int:pk>', views.sentiment_top_10_languages_widget, name='sentiment_top_10_languages_widget'),
  path('sentiment_top_10_authors_widget/<int:pk>', views.sentiment_top_10_authors_widget, name='sentiment_top_10_authors_widget'),
  path('sentiment_top_10_countries_widget/<int:pk>', views.sentiment_top_10_countries_widget, name='sentiment_top_10_countries_widget'),
  path('sentiment_top_10_sources_widget/<int:pk>', views.sentiment_top_10_sources_widget, name='sentiment_top_10_sources_widget'),
  path('content_volume_top_5_authors_widget/<int:pk>', views.content_volume_top_5_authors_widget, name='content_volume_top_5_authors_widget'),
  path('content_volume_top_5_countries_widget/<int:pk>', views.content_volume_top_5_countries_widget, name='content_volume_top_5_countries_widget'),
  path('content_volume_top_5_source_widget/<int:pk>', views.content_volume_top_5_source_widget, name='content_volume_top_5_source_widget'),
  path('top_10_languages_widget/<int:pk>', views.top_10_languages_widget, name='top_10_languages_widget'),
  path('top_10_countries_widget/<int:pk>', views.top_10_countries_widget, name='top_10_countries_widget'),
  path('top_10_brands_widget/<int:pk>', views.top_10_brands_widget, name='top_10_brands_widget'),
  path('summary_widget/<int:pk>', views.sum_widget, name='summary_widget'),
  path('volume_widget/<int:pk>', views.vol_widget, name='volume_widget'),
  path('sentiment_for_period_widget/<int:pk>', views.sentiment_for_period_widget, name='sentiment_for_period_widget'),
  path('clipping_feed_content_widget/<int:pk>', views.clipping_feed_content_widget, name='clipping_feed_content_widget'),
  path('top_10_authors_by_volume/<int:pk>', views.top_10_authors_by_volume, name='top_10_authors_by_volume_widget'),
  path('clipping_widget/<int:pk>', views.clipping_widget, name='clipping_widget'),
]
