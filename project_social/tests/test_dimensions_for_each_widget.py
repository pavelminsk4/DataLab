from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from common.factories.user import UserFactory


class DimensionsForEachWidgetTests(APITestCase):
    def test_response_list(self):
        user = UserFactory(username='Pablo Escobar')
        TweetBinderPostFactory(date='2020-10-10T00:00:00+00:00', language='En')
        TweetBinderPostFactory(date='2020-10-10T00:00:00+00:00', language='Sp')
        TweetBinderPostFactory(date='2021-10-10T00:00:00+00:00', language='En')
        pr = ProjectSocialFactory(creator = user)
        widget_pk = pr.social_widgets_list.content_volume_top_authors_id
        url = reverse('project_social:dimensions_for_each_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'aggregation_period': 'day',
            'author_dim_pivot': [],
            'country_dim_pivot': [],
            'source_dim_pivot': [],
            'language_dim_pivot': ['En'],
            'sentiment_dim_pivot': []
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {})
        url = reverse('project_social:social_content_volume_top_languages', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = { 'aggregation_period': 'day' }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'En': [{'date': '2020-10-10 00:00:00+00:00', 'post_count': 1},
                    {'date': '2021-10-10 00:00:00+00:00', 'post_count': 1}]}
        ]
        self.assertEqual(json.loads(response.content), res)
