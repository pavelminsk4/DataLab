from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from twenty_four_seven.serializers import ProjectTwentyFourSevenPostSerializer
from twenty_four_seven.serializers import ProjectTwentyFourSevenSerializer
from twenty_four_seven.serializers import WorkspaceTwentyFourSevenPostSerializer
from twenty_four_seven.serializers import WorkspaceTwentyFourSevenSerializer
from rest_framework.pagination import PageNumberPagination
from twenty_four_seven.serializers import ItemSerializer
from twenty_four_seven.models import WorkspaceTwentyFourSeven
from twenty_four_seven.models import ProjectTwentyFourSeven
from twenty_four_seven.models import Item
from twenty_four_seven.whatsapp import whatsappp_sender
from ml_components.models import RelatedThreshold
from deep_translator import GoogleTranslator
from common.ai_summary import ai_summary
from sentence_transformers import util
from django.http import JsonResponse
from rest_framework import viewsets
import numpy as np
import json
from django.db.models import Case, When


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ItemViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.GET:
            status = self.request.GET.get('status')
            return Item.objects.filter(project__pk=self.kwargs['project_pk'], status=status)
        return Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = StandardResultsSetPagination


class TwentyFourSevenProjectViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return ProjectTwentyFourSeven.objects.filter(members=user)

        return ProjectTwentyFourSeven.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectTwentyFourSevenPostSerializer
        return ProjectTwentyFourSevenSerializer


class WorkspaceTwentyFourSevenViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return WorkspaceTwentyFourSeven.objects.filter(members=user)

        return WorkspaceTwentyFourSeven.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WorkspaceTwentyFourSevenPostSerializer
        return WorkspaceTwentyFourSevenSerializer


def whatsapp(request):
    body = json.loads(request.body)
    phone_number = body['phone_number']
    message_content = body['message_content']
    res = whatsappp_sender(phone_number, message_content)
    return JsonResponse(res, safe=False)


class RelatedContentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        item_id = self.request.GET['item']
        threshold = RelatedThreshold.objects.filter(is_active=True)
        try:
            threshold = list(threshold.values_list('threshold',flat=True))[0]
        except:
            return top_similar(item_id)
        return top_similar(item_id,threshold)

    serializer_class = ItemSerializer


def top_similar(item_id,threshold=0.5):
    try:
        item = Item.objects.get(id=item_id)
        project = item.project
        items = project.tfs_project_items.exclude(online_post__summary_vector=[])
        vectors = items.values('online_post__id', 'online_post__summary_vector')
        id_list = np.array([i['online_post__id'] for i in vectors])
        posts_vector = np.array([i['online_post__summary_vector'] for i in vectors])
        cosine_scores = util.cos_sim(np.array([item.online_post.summary_vector[0]]), posts_vector.reshape(len(items),384))
        cosine_scores = cosine_scores.reshape(1,-1)[0]
        result = cosine_scores.argsort(descending=True)
        items = items.filter(online_post__pk__in=id_list[result])
        result_cosine = cosine_scores[result]
        result_id = id_list[result[:len(result_cosine[result_cosine>threshold])]]
        if result_id.shape == ():
            return Item.objects.none()
        result_id = result_id[1:]
        preserved = Case(*[When(online_post__pk=pk, then=pos) for pos, pk in enumerate(result_id)])
        items = items.filter(online_post__pk__in=result_id).order_by(preserved)
        return items
    except:
        return Item.objects.none()
    

def translator(request):
    data = json.loads(request.body)
    text = data['text']
    target_lang = data['target_lang']
    translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text=text)
    return JsonResponse({'translated_text': translated_text}, safe=False)


def summary(request, item_pk):
    item = Item.objects.get(id=item_pk)
    post = item.online_post
    text = post.full_text or post.entry_summary or post.entry_title
    lang = item.online_post.feed_language.language
    summary = ai_summary(text, lang)
    return JsonResponse({'summary': summary}, safe=False)
