from django.urls import path

from . import views

app_name = 'widgets'

urlpatterns = [
  path('sentiment_top_10_languages_widget/<int:pk>/<int:widget_pk>', views.sentiment_top_10_languages_widget, name='sentiment_top_10_languages_widget'),
  path('sentiment_top_10_authors_widget/<int:pk>/<int:widget_pk>', views.sentiment_top_10_authors_widget, name='sentiment_top_10_authors_widget'),
  path('sentiment_top_10_countries_widget/<int:pk>/<int:widget_pk>', views.sentiment_top_10_countries_widget, name='sentiment_top_10_countries_widget'),
  path('sentiment_top_10_sources_widget/<int:pk>/<int:widget_pk>', views.sentiment_top_10_sources_widget, name='sentiment_top_10_sources_widget'),
  path('content_volume_top_5_authors_widget/<int:pk>/<int:widget_pk>', views.content_volume_top_5_authors_widget, name='content_volume_top_5_authors_widget'),
  path('content_volume_top_5_countries_widget/<int:pk>/<int:widget_pk>', views.content_volume_top_5_countries_widget, name='content_volume_top_5_countries_widget'),
  path('content_volume_top_5_source_widget/<int:pk>/<int:widget_pk>', views.content_volume_top_5_source_widget, name='content_volume_top_5_source_widget'),
  path('top_10_languages_widget/<int:pk>/<int:widget_pk>', views.top_10_languages_widget, name='top_10_languages_widget'),
  path('top_10_countries_widget/<int:pk>/<int:widget_pk>', views.top_10_countries_widget, name='top_10_countries_widget'),
  path('top_10_brands_widget/<int:pk>/<int:widget_pk>', views.top_10_brands_widget, name='top_10_brands_widget'),
  path('summary_widget/<int:pk>/<int:widget_pk>', views.sum_widget, name='summary_widget'),
  path('volume_widget/<int:pk>/<int:widget_pk>', views.vol_widget, name='volume_widget'),
  path('sentiment_for_period_widget/<int:pk>/<int:widget_pk>', views.sentiment_for_period_widget, name='sentiment_for_period_widget'),
  path('clipping_feed_content_widget/<int:pk>/<int:widget_pk>', views.clipping_feed_content_widget, name='clipping_feed_content_widget'),
  path('top_10_authors_by_volume/<int:pk>/<int:widget_pk>', views.top_10_authors_by_volume, name='top_10_authors_by_volume_widget'),
  path('top_keywords/<int:pk>/<int:widget_pk>', views.top_keywords_widget, name='top_keywords'),
  path('sentiment_top_keywords/<int:pk>/<int:widget_pk>', views.sentiment_top_keywords_widget, name='sentiment_top_keywords'),
  path('sentiment_number_of_results/<int:pk>/<int:widget_pk>', views.sentiment_number_of_results, name='sentiment_number_of_results'),
  path('sentiment_diagram/<int:pk>/<int:widget_pk>', views.sentiment_diagram, name='sentiment_diagram'),
  path('authors_by_country/<int:pk>/<int:widget_pk>', views.authors_by_country, name='authors_by_country'),
  path('dimensions_for_each_widgets/<int:project_pk>/<int:widget_pk>', views.dimensions_for_each_widgets, name='dimensions_for_each_widgets'),
  path('interactive_widgets/<int:project_pk>/<int:widget_pk>', views.interactive_data_for_widgets, name='interactive_widgets'),
]
