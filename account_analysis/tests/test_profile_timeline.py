from account_analysis.models import ProjectAccountAnalysis
from tweet_binder.models import TweetBinderPost
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class ProfileTimelineWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    TweetBinderPost.objects.create(post_id='1', count_retweets='1', count_favorites='1', count_replies='1', language='En', user_name='First_name', locationString='USA', sentiment='neutral', text='First twitter post', date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='3', count_retweets='1', count_favorites='3', count_replies='1', language='En', user_name='First_name', locationString='USA', sentiment='neutral', text='First twitter post', date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='4', count_retweets='1', count_favorites='3', count_replies='1', language='En', user_name='First_name', locationString='USA', sentiment='neutral', text='First twitter post', date=datetime(2021, 10, 10), creation_date=datetime(2021, 10, 10))
    TweetBinderPost.objects.create(post_id='2', count_retweets='2', count_favorites='2', count_replies='2', language='Sp', user_name='Second_name', locationString='England', sentiment='positive', text='Second twitter post', date=datetime(2021, 10, 10), creation_date=datetime(2021, 10, 10))

    pr = ProjectAccountAnalysis.objects.create(title='Project', profile_handle='First_name', start_search_date=datetime(2020, 10, 10),
                                end_search_date=datetime(2023, 10, 16), country_filter=[], author_filter=[], source_filter=[], creator=user)
    widget_pk = pr.account_analysis_widgets_list.profile_timeline_id
    url = reverse('account_analysis:profile_timeline_widget', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    data = {
            'aggregation_period': "day"
           }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {
              'created_count': 2,
              'date': '2020-10-10 00:00:00+00:00',
              'engagement': 6,
              'likes': 4,
              'retweets': 2
            },
            {
              'created_count': 1,
              'date': '2021-10-10 00:00:00+00:00',
              'engagement': 4,
              'likes': 3,
              'retweets': 1
            }
          ]
    self.assertEqual(json.loads(response.content), res)
