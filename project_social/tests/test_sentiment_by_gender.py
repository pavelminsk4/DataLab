from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SentimentByGenderWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(sentiment='neutral', user_gender='undefined')
        TweetBinderPostFactory(sentiment='positive', user_gender='male')
        TweetBinderPostFactory(sentiment='negative', user_gender='female')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.sentiment_by_gender_id
        url = reverse('project_social:social_sentiment_by_gender', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'female': [
                {'sentiment_count': 1, 'sentiment': 'negative'},
                {'sentiment': 'neutral', 'sentiment_count': 0},
                {'sentiment': 'positive', 'sentiment_count': 0}
            ],
            'male': [
                {'sentiment_count': 1, 'sentiment': 'positive'},
                {'sentiment': 'negative', 'sentiment_count': 0},
                {'sentiment': 'neutral', 'sentiment_count': 0}
            ],
            'undefined': [
                {'sentiment_count': 1, 'sentiment': 'neutral'},
                {'sentiment': 'negative', 'sentiment_count': 0},
                {'sentiment': 'positive', 'sentiment_count': 0}
            ]
        }
        self.assertEqual(json.loads(response.content), res)
