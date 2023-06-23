from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class LanguagesByLocationTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(language='En', locationString='USA')
        TweetBinderPostFactory(language='Sp', locationString='Spain')
        TweetBinderPostFactory(language='Pl', locationString='England')
        TweetBinderPostFactory(language='En', locationString='England')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.languages_by_location_id
        url = reverse('project_social:social_languages_by_location', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'England': [['En', 1], ['Pl', 1]]},
            {'Spain': [['Sp', 1]]},
            {'USA': [['En', 1]]}
        ]
        self.assertEqual(json.loads(response.content), res)
