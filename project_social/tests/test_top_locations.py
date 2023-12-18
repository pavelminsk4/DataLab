from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopLocationWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(country='USA')
        TweetBinderPostFactory(country='England')
        pr = ProjectSocialFactory()
        widget_pk = pr.social_widgets_list.top_locations_id
        url = reverse('project_social:social_top_locations', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'country': 'England', 'locations_count': 1},
            {'country': 'USA', 'locations_count': 1}
        ]
        self.assertEqual(json.loads(response.content), res)
