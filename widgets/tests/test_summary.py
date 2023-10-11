from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SummaryTests(APITestCase):
    def test_response_list(self):
        p1 = PostFactory.create_batch(4, entry_author='AFP')
        p2 = PostFactory.create_batch(2, entry_author='EFE')
        pr = ProjectFactory()
        for p in p1:
            pr.posts.add(p)
        for p in p2:
            pr.posts.add(p)
        widget_pk = pr.widgets_list_2.summary_id
        url = reverse('widgets:onl_summary', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {'posts': 6, 'sources': 1, 'authors': 1, 'countries': 1, 'languages': 1, 'positive': 0, 'negative': 0, 'neutral': 6, 'reach': 0}
        self.assertEqual(json.loads(response.content), res)
