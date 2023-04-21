from account_analysis.models import AccountAnalysisWidgetDescription
from django.http import JsonResponse
from django.db.models import Q
from functools import reduce
import json

def dimensions_for_each(request, widget_pk):
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    body = json.loads(request.body)
    widget.author_dimensions = body['author_dim_pivot']
    widget.country_dimensions = body['country_dim_pivot']
    widget.source_dimensions = body['source_dim_pivot']
    widget.language_dimensions = body['language_dim_pivot']
    widget.sentiment_dimensions = body['sentiment_dim_pivot']
    widget.save()
    return JsonResponse({}, safe = False)
