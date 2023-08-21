from multilanguage.views import multilanguage
from django.urls import path


app_name = 'multilanguage'

urlpatterns = [
    path('api/multilanguage/', multilanguage, name='multilanguage'),
]
