from tweet_binder.models import TweetBinderPost
from project_social.models import ProjectSocial
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class TopLocationWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    TweetBinderPost.objects.create(post_id='1', count_retweets='1', count_favorites='1', count_replies='1', language='En', user_name='First_name', locationString='USA', sentiment_vote='neutral', text='First twitter post', creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='2', count_retweets='2', count_favorites='2', count_replies='2', language='Sp', user_name='Second_name', locationString='England', sentiment_vote='positive', text='Second twitter post', creation_date=datetime(2020, 10, 10))

    pr = ProjectSocial.objects.create(title='Project', keywords=['twitter'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), country_filter=[], author_filter=[], source_filter=[], creator=user)
    widget_pk = pr.social_widgets_list.top_authors_id
    url = reverse('project_social:social_top_authors', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    data = {
            'top_counts': 10
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'user_count': 1, 'user_name': 'First_name'},
            {'user_count': 1, 'user_name': 'Second_name'}
          ]
    self.assertEqual(json.loads(response.content), res)
