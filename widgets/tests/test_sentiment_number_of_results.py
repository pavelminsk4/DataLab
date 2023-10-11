from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from project.models import Project
from rest_framework import status
from django.urls import reverse
import json


class SentimentNumberOfResultsTests(APITestCase):
    def setUp(self):
        p1 = PostFactory(sentiment='neutral')
        p2 = PostFactory(sentiment='positive')
        pr = ProjectFactory()
        for post in (p1, p2):
            pr.posts.add(post)

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
