from common.factories.tweet_binder_post import TweetBinderPostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class ListLocationsTests(APITestCase):
    def test_top_keywords_api(self):
        location_list = ['a'+f'{n}' for n in range(51)]
        [TweetBinderPostFactory(user_location=location) for location in location_list]
        url = reverse('project_social:social_locations_list')
        response = self.client.get(url + '?' + 'search=a')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)['results']), 50)
        self.assertEqual(json.loads(response.content)['results'][0], {'user_location': 'a0'})
