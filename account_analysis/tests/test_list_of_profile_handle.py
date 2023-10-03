from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class ListOfProfileHandleTests(APITestCase):
  def test_response_list(self):

      tw_1 = TweetBinderPostFactory(count_totalretweets='1', count_favorites='1', count_replies='1', language='En', user_alias='First_name', locationString='USA', sentiment='neutral',
                                    text='First twitter post', type=['original', 'reply', 'retweet'], date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
      tw_2 = TweetBinderPostFactory(count_totalretweets='1', count_favorites='3', count_replies='1', language='En', user_alias='First_name', locationString='USA', sentiment='neutral', 
                                   text='First twitter post', type=['original', 'reply'], date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
      tw_3 = TweetBinderPostFactory( count_totalretweets='1', count_favorites='3', count_replies='1', language='En', user_alias='First_name', locationString='USA', sentiment='neutral', 
                                   text='First twitter post', type=['original'], date=datetime(2021, 10, 10), creation_date=datetime(2021, 10, 10))
      tw_4 = TweetBinderPostFactory(count_totalretweets='2', count_favorites='2', count_replies='2', language='Sp', user_alias='Second_name', locationString='England', sentiment='positive', 
                                   text='Second twitter post', type=['original', 'reply', 'retweet'], date=datetime(2021, 10, 10), creation_date=datetime(2021, 10, 10))
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
