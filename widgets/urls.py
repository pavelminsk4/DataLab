from django.urls import path

from . import views

app_name = 'widgets'

urlpatterns = [
  path('/summary_widget/<int:pk>', views.sum_widget, name='summary_widget'),
  path('/sentiment_for_period/<int:pk>', views.sntmnt_for_period, name='sentiment_for_period'),
]
