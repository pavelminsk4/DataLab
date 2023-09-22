from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json, os


class SentimentForPeriodWidgetTests(APITestCase):

    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'

    def test_response_list(self):
        PostFactory(entry_published='2021-09-03 00:00:00+00:00', sentiment='neutral')
        PostFactory(entry_published='2022-09-03 00:00:00+00:00', sentiment='neutral')
        PostFactory(entry_published='2021-10-03 00:00:00+00:00', sentiment='negative')
        PostFactory(entry_published='2021-09-03 00:00:00+00:00', sentiment='negative')
        PostFactory(entry_published='2022-09-03 00:00:00+00:00', sentiment='positive')
        PostFactory(entry_published='2022-10-03 00:00:00+00:00', sentiment='neutral')
        PostFactory(entry_published='2023-09-03 00:00:00+00:00', sentiment='neutral')
        PostFactory(entry_published='2023-09-03 00:00:00+00:00', sentiment='neutral')
        pr = ProjectFactory()

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


class SentimentForPeriodWidgetTestsTLW(APITestCase):

    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'

    def test_response_list_tlw(self):
        TalkwalkerPostFactory(entry_published='2021-09-03 00:00:00+00:00', sentiment='neutral')
        TalkwalkerPostFactory(entry_published='2022-09-03 00:00:00+00:00', sentiment='neutral')
        TalkwalkerPostFactory(entry_published='2021-10-03 00:00:00+00:00', sentiment='negative')
        TalkwalkerPostFactory(entry_published='2021-09-03 00:00:00+00:00', sentiment='negative')
        TalkwalkerPostFactory(entry_published='2022-09-03 00:00:00+00:00', sentiment='positive')
        TalkwalkerPostFactory(entry_published='2022-10-03 00:00:00+00:00', sentiment='neutral')
        TalkwalkerPostFactory(entry_published='2023-09-03 00:00:00+00:00', sentiment='neutral')
        TalkwalkerPostFactory(entry_published='2023-09-03 00:00:00+00:00', sentiment='neutral')
        pr = ProjectFactory()

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
