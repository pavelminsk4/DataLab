from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class ContentVolumeWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(date='2020-10-10T00:00:00+00:00')
        TweetBinderPostFactory(date='2021-10-10T00:00:00+00:00')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.content_volume_id
        url = reverse('project_social:social_content_volume',kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'created_count': 1, 'date': '2020-10-10 00:00:00+00:00'},
            {'created_count': 1, 'date': '2021-10-10 00:00:00+00:00'}
        ]
        self.assertEqual(json.loads(response.content), res)
