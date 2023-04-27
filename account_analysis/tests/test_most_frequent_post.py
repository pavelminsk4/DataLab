from account_analysis.models import ProjectAccountAnalysis
from tweet_binder.models import TweetBinderPost
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class MostFrequentPostTypeslineWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    TweetBinderPost.objects.create(post_id='1', count_retweets='1', count_favorites='1', count_replies='1', language='En', user_name='First_name', locationString='USA', sentiment='neutral',
                                    text='First twitter post', type=['original', 'reply', 'retweet'], date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='3', count_retweets='1', count_favorites='3', count_replies='1', language='En', user_name='First_name', locationString='USA', sentiment='neutral', 
                                   text='First twitter post', type=['original', 'reply'], date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='4', count_retweets='1', count_favorites='3', count_replies='1', language='En', user_name='First_name', locationString='USA', sentiment='neutral', 
                                   text='First twitter post', type=['original'], date=datetime(2021, 10, 10), creation_date=datetime(2021, 10, 10))
    TweetBinderPost.objects.create(post_id='2', count_retweets='2', count_favorites='2', count_replies='2', language='Sp', user_name='Second_name', locationString='England', sentiment='positive', 
                                   text='Second twitter post', type=['original', 'reply', 'retweet'], date=datetime(2021, 10, 10), creation_date=datetime(2021, 10, 10))

    pr = ProjectAccountAnalysis.objects.create(title='Project', profile_handle='First_name', start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), country_filter=[], author_filter=[], source_filter=[], creator=user)
    widget_pk = pr.account_analysis_widgets_list.most_frequent_post_types_id
    url = reverse('account_analysis:most_frequent_post_types_widget', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {'count_tweets': 3,
           'count_replies': 2,
           'count_retweets': 1}
    self.assertEqual(json.loads(response.content), res)
