from django.urls import path
from .views import webhook 

app_name = 'tweet_binder'

urlpatterns = [
    path('webhook/', webhook),
]
