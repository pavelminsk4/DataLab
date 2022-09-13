from django.urls import path
from . import views

from django.urls import re_path
from core.views import IndexTemplateView

urlpatterns = [
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
]
