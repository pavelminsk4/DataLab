from multilanguage.models import PhraseTranslations
from django.http import JsonResponse
import json


def multilanguage(request):
    en = json.loads(request.body).get('en', '')
    if en == '':
        return JsonResponse('', safe=False)

    obj, created = PhraseTranslations.objects.get_or_create(en=en)
    res = {'ar': en} if created or obj.ar is None else {'ar': obj.ar}
    return JsonResponse(res, safe=False)
