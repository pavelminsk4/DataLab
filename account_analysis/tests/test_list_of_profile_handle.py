from tweet_binder.models import TweetBinderPost
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class ListOfProfileHandleTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    TweetBinderPost.objects.create(post_id='1', count_totalretweets='1', count_favorites='1', count_replies='1', language='En', user_alias='First_name', locationString='USA', sentiment='neutral',
                                    text='First twitter post', type=['original', 'reply', 'retweet'], date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='3', count_totalretweets='1', count_favorites='3', count_replies='1', language='En', user_alias='First_name', locationString='USA', sentiment='neutral', 
                                   text='First twitter post', type=['original', 'reply'], date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='4', count_totalretweets='1', count_favorites='3', count_replies='1', language='En', user_alias='First_name', locationString='USA', sentiment='neutral', 
                                   text='First twitter post', type=['original'], date=datetime(2021, 10, 10), creation_date=datetime(2021, 10, 10))
    TweetBinderPost.objects.create(post_id='2', count_totalretweets='2', count_favorites='2', count_replies='2', language='Sp', user_alias='Second_name', locationString='England', sentiment='positive', 
                                   text='Second twitter post', type=['original', 'reply', 'retweet'], date=datetime(2021, 10, 10), creation_date=datetime(2021, 10, 10))
    url = reverse('account_analysis:list_of_profile_handle')
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [{"user_alias": "First_name", "user_picture": None}, 
           {"user_alias": "Second_name","user_picture": None}]
    self.assertEqual(json.loads(response.content), res)
