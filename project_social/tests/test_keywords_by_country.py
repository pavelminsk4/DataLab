from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from project_social.models import ProjectSocial
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopKeywordsByCountryTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(text='First twitter', locationString='USA')
        TweetBinderPostFactory(text='Second twitter post', locationString='USA')
        TweetBinderPostFactory(text='First twitter', locationString='England')
        ProjectSocialFactory(keywords=['twitter'])

    def test_top_keywords_by_country(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.keywords_by_country_id
        url = reverse('project_social:social_keywords_by_country',kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
                {'USA': [{'key': 'twitter', 'value': 1.0}, {'key': 'post', 'value': 0.5}]},
                {'England': [{'key': 'twitter', 'value': 1.0}]}
              ]
        self.assertEqual(json.loads(response.content), res)
