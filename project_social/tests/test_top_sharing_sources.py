from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from project_social.models import *
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json


class TopSharingSources(APITestCase):
  def test_sharing_sources_api(self):
    user = User.objects.create(username='Arturo')
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

    pr = ProjectSocial.objects.create(
      title='Project',keywords=['twitter'],
      additional_keywords=[],ignore_keywords=[],
      start_search_date=datetime(2020, 10, 10),
      end_search_date=datetime(2023, 10, 16),
      country_filter=[],author_filter=[],
      source_filter=[],creator=user,
    )
    widget_pk = pr.social_widgets_list.top_keywords_id
    url = reverse(
      'project_social:social_top_sharing_sources',
      kwargs={'pk': pr.pk, 'widget_pk': widget_pk},
    )
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
        {
          'type': 'Most active author',
          'name': 'First_name',
          'alias': '@first',
          'value': '2 post',
          'sentiments': {'positive': 1, 'negative': 0, 'neutral': 1},
          'picture': None,
          'gender': None,
          'source': 'Twitter',
        },
        {
          'type': 'Most influential author',
          'name': 'First_name',
          'alias': '@first',
          'value': '6 engagement',
          'sentiments': {'positive': 1, 'negative': 0, 'neutral': 1},
          'picture': None,
          'gender': None,
          'source': 'Twitter',
        },
    ]
    self.assertEqual(json.loads(response.content), res)
