from widgets.models import WidgetDescription
from django.http import JsonResponse
from widgets.models import WidgetDescription
from project.models import Project
from django.db.models import Q
from functools import reduce
import json

def dimensions_for_each(request, project_pk, widget_pk):
    project = Project.objects.get(id=project_pk)
    posts = post_agregator_with_dimensions(project)
    widget = WidgetDescription.objects.get(id=widget_pk)
    body = json.loads(request.body)
    smpl_freq = body['smpl_freq']
    widget.author_dim_pivot = body['author_dim_pivot']
    widget.country_dim_pivot = body['country_dim_pivot']
    widget.source_dim_pivot = body['source_dim_pivot']
    widget.language_dim_pivot = body['language_dim_pivot']
    widget.sentiment_dim_pivot = body['sentiment_dim_pivot']
    widget.save()
