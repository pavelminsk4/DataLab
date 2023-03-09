from django.http import JsonResponse

def clipping_feed(pk, widget_pk):
 res = []
 return JsonResponse(res, safe=False)
