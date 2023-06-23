from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class ContentVolumeTopLanguagesWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(language='En', date='2020-10-10T00:00:00+00:00')
        TweetBinderPostFactory(language='Sp', date='2020-10-10T00:00:00+00:00')
        TweetBinderPostFactory(language='En', date='2021-10-10T00:00:00+00:00')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.content_volume_top_languages_id
        url = reverse('project_social:social_content_volume_top_languages', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'En': [{'date': '2020-10-10 00:00:00+00:00', 'post_count': 1},
                    {'date': '2021-10-10 00:00:00+00:00', 'post_count': 1}]},
            {'Sp': [{'date': '2020-10-10 00:00:00+00:00', 'post_count': 1},
                    {'date': '2021-10-10 00:00:00+00:00', 'post_count': 0}]}
        ]
        self.assertEqual(json.loads(response.content), res)
