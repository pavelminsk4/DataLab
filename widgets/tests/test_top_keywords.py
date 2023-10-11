from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from project.models import Project
from rest_framework import status
from django.urls import reverse
import json


class TopKeywordsTests(APITestCase):
    def setUp(self):
        flink = FeedlinksFactory(country='Brasil')
        p1 = PostFactory(entry_summary='the keyword uno dos', feedlink=flink, entry_title='1')
        p2 = PostFactory(entry_summary='the keyword text', feedlink=flink, entry_title='2')
        pr = ProjectFactory()
        for post in (p1, p2):
            pr.posts.add(post)

    def test_top_keywords_api(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.top_keywords_id
        url = reverse('widgets:onl_top_keywords', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = {}
        response = self.client.post(url, data, format='json')
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
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {'negative': [],
               'neutral': [{'key': 'keyword', 'value': 1.0}, {'key': 'text', 'value': 0.5}],
               'positive': []}
        self.assertEqual(json.loads(response.content), res)

    def test_top_keywords_by_country_api(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.top_keywords_by_country_id
        url = reverse('widgets:onl_top_keywords_by_country', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'Brasil': [{'key': 'keyword', 'value': 1.0}, {'key': 'text', 'value': 0.5}]},
        ]
        self.assertEqual(json.loads(response.content), res)
