from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from project.models import Project
from rest_framework import status
from django.urls import reverse
import json, os


class SentimentNumberOfResultsTests(APITestCase):

    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'
        PostFactory(sentiment='neutral')
        PostFactory(sentiment='positive')
        ProjectFactory()

    def test_sentiment_number_of_results(self):
        pr = Project.objects.first()
        res = {'positive': 1, 'negative': 0, 'neutral': 1}
        widget_pk = pr.widgets_list_2.sentiment_number_of_results_id
        url = reverse('widgets:onl_sentiment_number_of_results',kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), res)


    def test_sentiment_diagram(self):
        pr = Project.objects.first()
        res = {'positive': 1, 'negative': 0, 'neutral': 1}
        widget_pk = pr.widgets_list_2.sentiment_diagram_id
        url = reverse('widgets:onl_sentiment_diagram', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), res)


class SentimentNumberOfResultsTestsTLW(APITestCase):

    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'
        TalkwalkerPostFactory(sentiment='neutral')
        TalkwalkerPostFactory(sentiment='positive')
        ProjectFactory()

    def test_sentiment_number_of_results_tlw(self):
        pr = Project.objects.first()
        res = {'positive': 1, 'negative': 0, 'neutral': 1}
        widget_pk = pr.widgets_list_2.sentiment_number_of_results_id
        url = reverse('widgets:onl_sentiment_number_of_results',kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), res)


    def test_sentiment_diagram_tlw(self):
        pr = Project.objects.first()
        res = {'positive': 1, 'negative': 0, 'neutral': 1}
        widget_pk = pr.widgets_list_2.sentiment_diagram_id
        url = reverse('widgets:onl_sentiment_diagram', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), res)
