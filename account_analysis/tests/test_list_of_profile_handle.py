from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class ListOfProfileHandleTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(count_totalretweets='1', count_favorites='1', count_replies='1', language='En', user_alias='First_name', user_location='USA', sentiment='neutral',
                               text='First twitter post', type=['original', 'reply', 'retweet'], date="2022-10-10T00:00:00Z", creation_date="2022-10-10T00:00:00Z")
        TweetBinderPostFactory(count_totalretweets='1', count_favorites='3', count_replies='1', language='En', user_alias='First_name', user_location='USA', sentiment='neutral', 
                              text='First twitter post', type=['original', 'reply'], date="2020-10-10T00:00:00Z", creation_date="2020-10-10T00:00:00Z")
        TweetBinderPostFactory(count_totalretweets='1', count_favorites='3', count_replies='1', language='En', user_alias='First_name', user_location='USA', sentiment='neutral', 
                               text='First twitter post', type=['original'], date="2021-10-10T00:00:00Z", creation_date="2021-10-10T00:00:00Z")
        TweetBinderPostFactory(count_totalretweets='2', count_favorites='2', count_replies='2', language='Sp', user_alias='Second_name', user_location='England', sentiment='positive', 
                               text='Second twitter post', type=['original', 'reply', 'retweet'], date="2021-10-10T00:00:00Z", creation_date="2021-10-10T00:00:00Z")
        AccountAnalysisProjectFactory()
        url = reverse('account_analysis:list_of_profile_handle')
        data = {
                'page_number':1,
                'profile_per_page':20,
                'profiles_query':""
                }
        response = self.client.post(url, format='json', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = {
                    'num_pages': 1,
                    'num_profiles': 2,
                    'profiles': [{'user_alias': 'First_name', 'user_picture': None},
                                {'user_alias': 'Second_name', 'user_picture': None}],
                    'profiles_query': ''
                  }
        self.assertEqual(json.loads(response.content), results)
