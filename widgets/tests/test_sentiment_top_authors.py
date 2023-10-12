from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SentimentTopAuthorsWidgetTests(APITestCase):
    def test_response_list(self):
        p1 = PostFactory(entry_author='AFP', sentiment='neutral')
        p2 = PostFactory(entry_author='AFP', sentiment='neutral')
        p3 = PostFactory(entry_author='AFP', sentiment='negative')
        p4 = PostFactory(entry_author='AFP', sentiment='negative')
        p5 = PostFactory(entry_author='AFP', sentiment='positive')
        p6 = PostFactory(entry_author='EFE', sentiment='neutral')
        p7 = PostFactory(entry_author='AFP', sentiment='neutral')
        p8 = PostFactory(entry_author='', sentiment='neutral')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4, p5,p6, p7, p8):
            pr.posts.add(post)
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
