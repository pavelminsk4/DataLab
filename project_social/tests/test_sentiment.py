from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SentimentWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(sentiment='neutral', date='2020-10-10 00:00:00Z')
        TweetBinderPostFactory(sentiment='positive', date='2020-10-10 00:00:00Z')
        TweetBinderPostFactory(sentiment='negative', date='2021-10-10 00:00:00Z')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.sentiment_id
        url = reverse('project_social:social_sentiment', kwargs={
                      'pk': pr.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        res = [
            {'2020-10-10 00:00:00+00:00': {'negative': 0, 'neutral': 1, 'positive': 1}},
            {'2021-10-10 00:00:00+00:00': {'negative': 1, 'neutral': 0, 'positive': 0}}
        ]
        self.assertEqual(json.loads(response.content), res)
