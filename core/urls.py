from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home/ar/', views.home_ar, name='home_ar'),
    path('home/contact/', views.contact, name='contact'),
    path('home/contact_ar/', views.contact_ar, name='contact_ar'),
]
