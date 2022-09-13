from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.views.generic.base import TemplateView


class IndexTemplateView(TemplateView):
    def get_template_names(self):
        template_name = "index.html"
        return template_name
