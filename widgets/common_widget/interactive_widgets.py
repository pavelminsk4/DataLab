from widgets.services.interactive_data_service import InteractiveDataService
from django.http import JsonResponse


def interactive_widgets(request, project_pk, widget_pk):
    res = InteractiveDataService().execute(request, project_pk, widget_pk)
    return JsonResponse(res, safe = False)
