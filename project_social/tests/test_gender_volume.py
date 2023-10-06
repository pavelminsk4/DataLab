from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class GendeerVolumeWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(date='2020-10-10 00:00:00Z', user_gender='male')
        TweetBinderPostFactory(date='2020-10-10 00:00:00Z', user_gender='female',)
        TweetBinderPostFactory(date='2021-10-10 00:00:00Z', user_gender='undefined')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.gender_volume_id
        url = reverse('project_social:social_gender_volume', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {
                'female': [
                    {'date': '2020-10-10 00:00:00+00:00', 'post_count': 1},
                    {'date': '2021-10-10 00:00:00+00:00', 'post_count': 0}
                ]
            },
            {
                'male': [
                    {'date': '2020-10-10 00:00:00+00:00', 'post_count': 1},
                    {'date': '2021-10-10 00:00:00+00:00', 'post_count': 0}
                ]
            },
            {
                'undefined': [
                    {'date': '2020-10-10 00:00:00+00:00', 'post_count': 0},
                    {'date': '2021-10-10 00:00:00+00:00', 'post_count': 1}
                ]
            }
        ]
        self.assertEqual(json.loads(response.content), res)
