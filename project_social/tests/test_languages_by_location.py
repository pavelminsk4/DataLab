from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class LanguagesByLocationTests(APITestCase):
    maxDiff = None

    def test_response_list(self):
        TweetBinderPostFactory(language='En', country='USA')
        TweetBinderPostFactory(language='Sp', country='Spain')
        TweetBinderPostFactory(language='Pl', country='England')
        TweetBinderPostFactory(language='En', country='England')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.languages_by_location_id
        url = reverse('project_social:social_languages_by_location', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'England': [{'language': 'En', 'count': 1}, {'language': 'Pl', 'count': 1}],
            'Spain': [{'language': 'Sp', 'count': 1}],
            'USA': [{'language': 'En', 'count': 1}]
        }
        self.assertEqual(json.loads(response.content), res)
