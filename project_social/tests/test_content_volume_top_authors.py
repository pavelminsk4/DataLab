from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from common.factories.user import UserFactory


class ContentVolumeTopAuthorsWidgetTests(APITestCase):
    def test_response_list(self):
        user = UserFactory(username='Pablo Escobar')
        TweetBinderPostFactory(user_name='First',  date='2020-10-10T00:00:00+00:00')
        TweetBinderPostFactory(user_name='Second', date='2020-10-10T00:00:00+00:00')
        TweetBinderPostFactory(user_name='Third',  date='2021-10-10T00:00:00+00:00')
        pr = ProjectSocialFactory(creator=user)
        widget_pk = pr.social_widgets_list.content_volume_top_authors_id
        url = reverse('project_social:social_content_volume_top_authors', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = { 'aggregation_period': 'day' }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'First':  [{'date': '2020-10-10 00:00:00+00:00', 'post_count': 1},
                        {'date': '2021-10-10 00:00:00+00:00', 'post_count': 0},]},
            {'Second': [{'date': '2020-10-10 00:00:00+00:00', 'post_count': 1},
                        {'date': '2021-10-10 00:00:00+00:00', 'post_count': 0},]},
            {'Third':  [{'date': '2020-10-10 00:00:00+00:00', 'post_count': 0},
                        {'date': '2021-10-10 00:00:00+00:00', 'post_count': 1},]},
        ]
        self.assertEqual(json.loads(response.content), res)
