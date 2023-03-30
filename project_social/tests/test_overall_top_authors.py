from tweet_binder.models import TweetBinderPost
from project_social.models import ProjectSocial
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class OverallTopAuthorsTest(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Varg')
    TweetBinderPost.objects.create(
      post_id='1',count_retweets='1',
      count_favorites='1',count_replies='1',
      language='En',user_name='First_name',
      user_alias='@first',locationString='USA',
      sentiment='neutral',text='First twitter',
      date=datetime(2020, 10, 10),creation_date=datetime(2020, 10, 10),
    )
    TweetBinderPost.objects.create(
      post_id='2',count_retweets='2',
      count_favorites='2',count_replies='2',
      language='Sp',user_name='First_name',
      user_alias='@first',locationString='England',
      sentiment='positive',text='Second twitter post',
      date=datetime(2020, 10, 10),creation_date=datetime(2020, 10, 10),
    )
    TweetBinderPost.objects.create(
      post_id='3',count_retweets='3',
      count_favorites='9',count_replies='2',
      language='Sp',user_name='Second_name',
      user_alias='@second',locationString='England',
      sentiment='positive',text='Third twitter post',
      date=datetime(2020, 10, 10),creation_date=datetime(2020, 10, 10),
    )

    pr = ProjectSocial.objects.create(title='Project', keywords=['twitter'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), country_filter=[], author_filter=[], source_filter=[], creator=user)
    widget_pk = pr.social_widgets_list.top_authors_id
    url = reverse('project_social:social_overall_top_authors', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {
              'name': 'First_name',
              'alias': '@first',
              'picture': None,
              'sentiments': {
                'positive': 1,
                'negative': 0,
                'neutral':  1,
              },
              'posts': 2,
              'media_type': 'Twitter',
              'reach': None,
              'engagements': 6,
            },
            {
              'name': 'Second_name',
              'alias': '@second',
              'picture': None,
              'sentiments': {
                'positive': 1,
                'negative': 0,
                'neutral':  0,
              },
              'posts': 1,
              'media_type': 'Twitter',
              'reach': None,
              'engagements': 12,
            }, 
          ]
    self.assertEqual(json.loads(response.content), res)
