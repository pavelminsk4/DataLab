from django.urls import path

from . import views

app_name = 'widgets'

urlpatterns = [
  path('onl_sentiment_top_languages/<int:pk>/<int:widget_pk>', views.onl_sentiment_top_languages, name='onl_sentiment_top_languages'),
  path('onl_sentiment_top_authors/<int:pk>/<int:widget_pk>', views.onl_sentiment_top_authors, name='onl_sentiment_top_authors'),
  path('onl_sentiment_top_countries/<int:pk>/<int:widget_pk>', views.onl_sentiment_top_countries, name='onl_sentiment_top_countries'),
  path('onl_sentiment_top_sources/<int:pk>/<int:widget_pk>', views.onl_sentiment_top_sources, name='onl_sentiment_top_sources'),
  path('onl_content_volume_top_authors/<int:pk>/<int:widget_pk>', views.onl_content_volume_top_authors, name='onl_content_volume_top_authors'),
  path('onl_content_volume_top_countries/<int:pk>/<int:widget_pk>', views.onl_content_volume_top_countries, name='onl_content_volume_top_countries'),
  path('onl_content_volume_top_sources/<int:pk>/<int:widget_pk>', views.onl_content_volume_top_sources, name='onl_content_volume_top_sources'),
  path('onl_top_languages/<int:pk>/<int:widget_pk>', views.onl_top_languages, name='onl_top_languages'),
  path('onl_top_countries/<int:pk>/<int:widget_pk>', views.onl_top_countries, name='onl_top_countries'),
  path('onl_top_brands/<int:pk>/<int:widget_pk>', views.onl_top_brands, name='onl_top_brands'),
  path('onl_summary/<int:pk>/<int:widget_pk>', views.onl_summary, name='onl_summary'),
  path('onl_volume/<int:pk>/<int:widget_pk>', views.onl_volume, name='onl_volume'),
  path('onl_sentiment_for_period/<int:pk>/<int:widget_pk>', views.onl_sentiment_for_period, name='onl_sentiment_for_period'),
  path('onl_clipping_feed_content/<int:pk>/<int:widget_pk>', views.onl_clipping_feed_content, name='onl_clipping_feed_content'),
  path('onl_top_authors/<int:pk>/<int:widget_pk>', views.onl_top_authors, name='onl_top_authors'),
  path('onl_top_keywords/<int:pk>/<int:widget_pk>', views.onl_top_keywords, name='onl_top_keywords'),
  path('onl_sentiment_top_keywords/<int:pk>/<int:widget_pk>', views.onl_sentiment_top_keywords, name='onl_sentiment_top_keywords'),
  path('onl_sentiment_number_of_results/<int:pk>/<int:widget_pk>', views.onl_sentiment_number_of_results, name='onl_sentiment_number_of_results'),
  path('onl_sentiment_diagram/<int:pk>/<int:widget_pk>', views.onl_sentiment_diagram, name='onl_sentiment_diagram'),
  path('onl_authors_by_country/<int:pk>/<int:widget_pk>', views.onl_authors_by_country, name='onl_authors_by_country'),
  path('onl_sources_by_country/<int:pk>/<int:widget_pk>', views.onl_sources_by_country, name='onl_sources_by_country'),
  path('onl_sources_by_language/<int:pk>/<int:widget_pk>', views.onl_sources_by_language, name='onl_sources_by_language'),
  path('onl_top_sharing_sources/<int:pk>/<int:widget_pk>', views.onl_top_sharing_sources, name='onl_top_sharing_sources'),
  path('onl_overall_top_sources/<int:pk>/<int:widget_pk>', views.onl_overall_top_sources, name='onl_overall_top_sources'),
  path('onl_overall_top_authors/<int:pk>/<int:widget_pk>', views.onl_overall_top_authors, name='onl_overall_top_authors'),
  path('onl_authors_by_language/<int:pk>/<int:widget_pk>', views.onl_authors_by_language, name='onl_authors_by_language'),
  path('onl_authors_by_sentiment/<int:pk>/<int:widget_pk>', views.onl_authors_by_sentiment, name='onl_authors_by_sentiment'),
  path('onl_top_keywords_by_country/<int:pk>/<int:widget_pk>', views.onl_top_keywords_by_country, name='onl_top_keywords_by_country'),
  path('onl_languages_by_country/<int:pk>/<int:widget_pk>', views.onl_languages_by_country, name='onl_languages_by_country'),
  path('dimensions_for_each_widgets/<int:project_pk>/<int:widget_pk>', views.dimensions_for_each_widgets, name='dimensions_for_each_widgets'),
  path('interactive_widgets/<int:project_pk>/<int:widget_pk>', views.interactive_data_for_widgets, name='interactive_widgets'),
]
