from twenty_four_seven.serializers import ProjectTwentyFourSevenPostSerializer
from twenty_four_seven.serializers import ProjectTwentyFourSevenSerializer
from twenty_four_seven.serializers import WorkspaceTwentyFourSevenPostSerializer
from twenty_four_seven.serializers import WorkspaceTwentyFourSevenSerializer
from twenty_four_seven.serializers import ItemSerializer
from twenty_four_seven.models import WorkspaceTwentyFourSeven
from twenty_four_seven.models import ProjectTwentyFourSeven
from twenty_four_seven.models import Item
from twenty_four_seven.whatsapp import whatsappp_sender
from ml_components.models import RelatedThreshold
from sentence_transformers import util
from django.http import JsonResponse
from rest_framework import viewsets
import numpy as np
import pandas as pd
import json
from django.db.models import Case, When

from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


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
        defaults = {
            'is_active': True,
            'description': 'threshold',
            'threshold': 0.3,
            'tf_idf_method': True
        }
        threshold_item, _ = RelatedThreshold.objects.get_or_create(is_active=True, defaults=defaults)
        threshold = threshold_item.threshold
        method = threshold_item.tf_idf_method
        return tfidf_top_similar(item_id, threshold) if method else top_similar(item_id, threshold)

    serializer_class = ItemSerializer


def tfidf_top_similar(item_id, threshold):
    try:
        item = Item.objects.get(id=item_id)
        project = ProjectTwentyFourSeven.objects.get(id=item.project.id)
        items = project.tfs_project_items.all()
        vectors = items.values('post__id', 'post__entry_title')
        id_list = np.array([i['post__id'] for i in vectors])
        titles = np.array([i['post__entry_title'] for i in vectors])
        item_title = (item.post.id, item.post.entry_title)
        titles_series = pd.Series(titles)
        index_series = pd.Series([(id_list[i], titles[i]) for i in range(len(titles))])
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(titles)
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        indices = pd.Series(titles_series.index, index=index_series)
        idx = indices[item_title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        result_indices = []
        for i in sim_scores[1:]:
            if i[1] > threshold:
                result_indices.append(i[0])
            else:
                break
        result_id = id_list[result_indices]
        preserved = Case(*[When(post__pk=pk, then=pos) for pos, pk in enumerate(result_id)])
        items = items.filter(post__pk__in=result_id).order_by(preserved)
        return items
    except:
        return Item.objects.none()


def top_similar(item_id, threshold=0.5):
    try:
        item = Item.objects.get(id=item_id)
        project = item.project
        items = project.tfs_project_items.exclude(post__summary_vector=[])
        vectors = items.values('post__id', 'post__summary_vector')
        id_list = np.array([i['post__id'] for i in vectors])
        posts_vector = np.array([i['post__summary_vector'] for i in vectors])
        cosine_scores = util.cos_sim(np.array([item.post.summary_vector[0]]), posts_vector.reshape(len(items), 384))
        cosine_scores = cosine_scores.reshape(1, -1)[0]
        result = cosine_scores.argsort(descending=True)
        items = items.filter(post__pk__in=id_list[result])
        result_cosine = cosine_scores[result]
        result_id = id_list[result[:len(result_cosine[result_cosine > threshold])]]
        if result_id.shape == ():
            return Item.objects.none()
        result_id = result_id[1:]
        preserved = Case(*[When(post__pk=pk, then=pos) for pos, pk in enumerate(result_id)])
        items = items.filter(post__pk__in=result_id).order_by(preserved)
        return items
    except:
        return Item.objects.none()
