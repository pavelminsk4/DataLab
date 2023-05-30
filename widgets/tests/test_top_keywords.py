from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import json
from project.models import Project
from common.factories.post import PostFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.feedlinks import FeedlinksFactory


class TopKeywordsTests(APITestCase):
    def setUp(self):
        flink = FeedlinksFactory(country='Brasil')
        sp = SpeechFactory()
        PostFactory(entry_summary='the keyword uno dos', feed_language=sp, feedlink=flink)
        PostFactory(entry_summary='the keyword text', feed_language=sp, feedlink=flink)
        ProjectFactory()

    def test_top_keywords_api(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.top_keywords_id
        url = reverse('widgets:onl_top_keywords', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'key': 'keyword', 'value': 1.0},
            {'key': 'text', 'value': 0.5},
        ]
        self.assertEqual(json.loads(response.content), res)

    def test_sentiment_top_keywords_api(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.sentiment_top_keywords_id
        url = reverse('widgets:onl_sentiment_top_keywords',kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {'negative': [],
               'neutral': [{'key': 'keyword', 'value': 1.0}, {'key': 'text', 'value': 0.5}],
               'positive': []}
        self.assertEqual(json.loads(response.content), res)

    def test_top_keywords_by_country_api(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.sentiment_top_keywords_id
        url = reverse('widgets:onl_top_keywords_by_country', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'Brasil': [{'key': 'keyword', 'value': 1.0}, {'key': 'text', 'value': 0.5}]},
        ]
        self.assertEqual(json.loads(response.content), res)
