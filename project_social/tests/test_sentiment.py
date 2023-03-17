from tweet_binder.models import TweetBinderPost
from project_social.models import ProjectSocial
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class SentimentWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    TweetBinderPost.objects.create(post_id='1', count_retweets='1', count_favorites='1', count_replies='1', language='En', user_name='First_name', locationString='USA', sentiment_vote='neutral', text='First twitter post', creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='2', count_retweets='2', count_favorites='2', count_replies='2', language='Sp', user_name='Second_name', locationString='England', sentiment_vote='positive', text='Second twitter post', creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='3', count_retweets='2', count_favorites='2', count_replies='2', language='Sp', user_name='3_name', locationString='England', sentiment_vote='negative', text='Second twitter post', creation_date=datetime(2021, 10, 10))
    
    # test first project with None field
    pr = ProjectSocial.objects.create(title='Project', keywords=['twitter'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), country_filter=[], author_filter=[], source_filter=[], creator=user)
    widget_pk = pr.social_widgets_list.sentiment_id
    url = reverse('project_social:social_sentiment', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'2020-10-10 00:00:00+00:00': {'negative': 0, 'neutral': 1, 'positive': 1}},
            {'2021-10-10 00:00:00+00:00': {'negative': 1, 'neutral': 0, 'positive': 0}}
          ]
    self.assertEqual(json.loads(response.content), res)