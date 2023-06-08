from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopLocationWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(language='En')
        TweetBinderPostFactory(language='Sp')
        pr = ProjectSocialFactory()
        widget_pk = pr.social_widgets_list.top_languages_id
        url = reverse('project_social:social_top_languages', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'language': 'En', 'language_count': 1},
            {'language': 'Sp', 'language_count': 1}
        ]
        self.assertEqual(json.loads(response.content), res)
