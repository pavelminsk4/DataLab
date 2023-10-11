from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SentimentForPeriodWidgetTests(APITestCase):
    def test_response_list(self):
        p1 = PostFactory(entry_published='2021-09-03 00:00:00Z', sentiment='neutral')
        p2 = PostFactory(entry_published='2022-09-03 00:00:00Z', sentiment='neutral')
        p3 = PostFactory(entry_published='2021-10-03 00:00:00Z', sentiment='negative')
        p4 = PostFactory(entry_published='2021-09-03 00:00:00Z', sentiment='negative')
        p5 = PostFactory(entry_published='2022-09-03 00:00:00Z', sentiment='positive')
        p6 = PostFactory(entry_published='2022-10-03 00:00:00Z', sentiment='neutral')
        p7 = PostFactory(entry_published='2023-09-03 00:00:00Z', sentiment='neutral')
        p8 = PostFactory(entry_published='2023-09-03 00:00:00Z', sentiment='neutral')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4, p5, p6, p7, p8):
            pr.posts.add(post)
        widget_pk = pr.widgets_list_2.sentiment_for_period_id
        url = reverse('widgets:onl_sentiment_for_period', kwargs={
                      'pk': pr.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'2021-09-03 00:00:00+00:00': {'negative': 1, 'neutral': 1, 'positive': 0}},
            {'2021-10-03 00:00:00+00:00': {'negative': 1, 'neutral': 0, 'positive': 0}},
            {'2022-09-03 00:00:00+00:00': {'negative': 0, 'neutral': 1, 'positive': 1}},
            {'2022-10-03 00:00:00+00:00': {'negative': 0, 'neutral': 1, 'positive': 0}},
            {'2023-09-03 00:00:00+00:00': {'negative': 0, 'neutral': 2, 'positive': 0}},
        ]
        self.assertEqual(json.loads(response.content), res)
