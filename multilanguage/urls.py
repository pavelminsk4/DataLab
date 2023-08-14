from multilanguage.views import multilanguage
from django.urls import path


app_name = 'multilanguage'

urlpatterns = [
    path('multilanguage/', multilanguage, name='multilanguage'),
]
