from twenty_four_seven.models import Item
from django.http import JsonResponse
from common.translator.translate_long_text import translate
from common.ai_summary import ai_summary
import json


def translator(request):
    data = json.loads(request.body)
    text = data['text']
    lang = data['target_lang']

    return JsonResponse({'translated_text': translate(text, lang)}, safe=False)


def summary(request, item_pk):
    item = Item.objects.get(id=item_pk)
    post = item.post
    text = post.full_text or post.entry_summary or post.entry_title
    lang = item.post.feed_language.language

    summary = ai_summary(text, lang)
    return JsonResponse({'summary': summary, 'summary_ar': translate(summary, 'arabic')}, safe=False)
