from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SentimentTopAuthorsWidgetTests(APITestCase):
    def test_response_list(self):
        PostFactory(entry_author='AFP', sentiment='neutral')
        PostFactory(entry_author='AFP', sentiment='neutral')
        PostFactory(entry_author='AFP', sentiment='negative')
        PostFactory(entry_author='AFP', sentiment='negative')
        PostFactory(entry_author='AFP', sentiment='positive')
        PostFactory(entry_author='EFE', sentiment='neutral')
        PostFactory(entry_author='AFP', sentiment='neutral')
        PostFactory(entry_author='', sentiment='neutral')
        pr = ProjectFactory()

        widget_pk = pr.widgets_list_2.sentiment_top_authors_id
        url = reverse('widgets:onl_sentiment_top_authors', kwargs={
                      'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {'AFP': [
            {'sentiment': 'neutral', 'sentiment_count': 3},
            {'sentiment': 'negative', 'sentiment_count': 2},
            {'sentiment': 'positive', 'sentiment_count': 1}
        ],
            'EFE': [
            {'sentiment': 'neutral', 'sentiment_count': 1},
            {'sentiment': 'negative', 'sentiment_count': 0},
            {'sentiment': 'positive', 'sentiment_count': 0}
        ],
        }
        self.assertEqual(json.loads(response.content), res)
