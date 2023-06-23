from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SentimentAuthorsWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(user_name='First_name', sentiment='neutral')
        TweetBinderPostFactory(user_name='Second_name', sentiment='positive')
        TweetBinderPostFactory(user_name='3_name', sentiment='negative')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.sentiment_authors_id
        url = reverse('project_social:social_sentiment_authors', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            '3_name': [
                {'sentiment_count': 1, 'sentiment': 'negative'},
                {'sentiment_count': 0, 'sentiment': 'neutral'},
                {'sentiment_count': 0, 'sentiment': 'positive'}
            ],
            'First_name': [
                {'sentiment_count': 1, 'sentiment': 'neutral'},
                {'sentiment_count': 0, 'sentiment': 'negative'},
                {'sentiment_count': 0, 'sentiment': 'positive'}
            ],
            'Second_name': [
                {'sentiment_count': 1, 'sentiment': 'positive'},
                {'sentiment_count': 0, 'sentiment': 'negative'},
                {'sentiment_count': 0, 'sentiment': 'neutral'}
            ]
        }
        self.assertEqual(json.loads(response.content), res)
