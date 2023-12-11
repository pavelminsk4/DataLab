from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class LanguagesByLocationTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(language='En', user_location='USA')
        TweetBinderPostFactory(language='Sp', user_location='Spain')
        TweetBinderPostFactory(language='Pl', user_location='England')
        TweetBinderPostFactory(language='En', user_location='England')
        TweetBinderPostFactory(language='En', user_location=None)
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
