from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SentimentLocationWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(locationString='USA', sentiment='neutral')
        TweetBinderPostFactory(locationString='England', sentiment='positive')
        TweetBinderPostFactory(locationString='England', sentiment='negative')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.sentiment_locations_id
        url = reverse('project_social:social_sentiment_locations', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'England': [
                {'sentiment_count': 1, 'sentiment': 'negative'},
                {'sentiment_count': 1, 'sentiment': 'positive'},
                {'sentiment': 'neutral', 'sentiment_count': 0}
            ],
            'USA': [
                {'sentiment_count': 1, 'sentiment': 'neutral'},
                {'sentiment': 'negative', 'sentiment_count': 0},
                {'sentiment': 'positive', 'sentiment_count': 0}
            ]
        }
        self.assertEqual(json.loads(response.content), res)
