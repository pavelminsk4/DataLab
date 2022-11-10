from django.urls import path

from . import views

app_name = 'widgets'

urlpatterns = [
  path('summary_widget/<int:pk>', views.sum_widget, name='summary_widget'),
  path('volume_widget/<int:pk>', views.vol_widget, name='volume_widget'),
  #path('/sentiment_for_period/<int:pk>', views.sntmnt_for_period, name='sentiment_for_period'),
  path('clipping_feed_content_widget/<int:pk>', views.clipping_feed_content_widget, name='clipping_feed_content_widget'),
  path('top_10_authors_by_volume/<int:pk>', views.top_10_authors_by_volume, name='top_10_authors_by_volume_widget'),
]
