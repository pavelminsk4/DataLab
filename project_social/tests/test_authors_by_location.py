from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class AuthorsByLocationTests(APITestCase):
    maxDiff = None

    def test_response_list(self):
        TweetBinderPostFactory(user_alias='@first', country='USA')
        TweetBinderPostFactory(user_alias='@second', country='England')
        TweetBinderPostFactory(user_alias='@second', country='England')
        TweetBinderPostFactory(user_alias='@new', country='England')

        pr = ProjectSocialFactory()
        widget_pk = pr.social_widgets_list.authors_by_location_id
        url = reverse('project_social:social_authors_by_location', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'England': [['@second', 2], ['@new', 1]]},
            {'USA': [['@first', 1]]}
        ]
        self.assertEqual(json.loads(response.content), res)
