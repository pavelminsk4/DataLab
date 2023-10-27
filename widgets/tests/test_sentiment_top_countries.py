from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SentimentTopCountriesTests(APITestCase):
    def test_response_list(self):
        flink1 = FeedlinkFactory(country='England')
        flink2 = FeedlinkFactory(country='USA')
        flink3 = FeedlinkFactory(country='Canada')
        p1 = PostFactory(feedlink=flink1, sentiment='neutral', entry_title='1')
        p2 = PostFactory(feedlink=flink1, sentiment='neutral', entry_title='2')
        p3 = PostFactory(feedlink=flink2, sentiment='negative', entry_title='1')
        p4 = PostFactory(feedlink=flink2, sentiment='negative', entry_title='2')
        p5 = PostFactory(feedlink=flink3, sentiment='positive', entry_title='1')
        p6 = PostFactory(feedlink=flink3, sentiment='neutral', entry_title='2')
        pr = ProjectFactory()

        for post in (p1, p2, p3, p4, p5, p6):
            pr.posts.add(post)

        widget_pk = pr.widgets_list_2.sentiment_top_countries_id
        url = reverse('widgets:onl_sentiment_top_countries', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'Canada': [
                {'sentiment': 'neutral', 'sentiment_count': 1},
                {'sentiment': 'positive', 'sentiment_count': 1},
                {'sentiment': 'negative', 'sentiment_count': 0},
            ],
            'England': [
                {'sentiment': 'neutral', 'sentiment_count': 2},
                {'sentiment': 'negative', 'sentiment_count': 0},
                {'sentiment': 'positive', 'sentiment_count': 0},
            ],
            'USA': [
                {'sentiment': 'negative', 'sentiment_count': 2},
                {'sentiment': 'neutral', 'sentiment_count': 0},
                {'sentiment': 'positive', 'sentiment_count': 0},
            ],
        }
        self.assertEqual(json.loads(response.content), res)
