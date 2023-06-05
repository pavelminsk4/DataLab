from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class PostsMentionsTests(APITestCase):
  def test_posts_mentions(self):
    tw = TweetBinderPostFactory(text = 'First twitter post @First_name')
    pr = AccountAnalysisProjectFactory()
    url = reverse('account_analysis:search_posts_mentions', kwargs={'project_pk':pr.id})
    response = self.client.post(url, {'posts_per_page': 20, 'page_number': 1}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    post = {
                'count_favorites': 1,
                'count_replies': 1,
                'count_totalretweets': None,
                'date': '2020-10-10T00:00:00Z',
                'engagements': 2,
                'id': tw.id,
                'images': None,
                'inreplyto': None,
                'link': f'https://twitter.com/user/status/{tw.post_id}',
                'post_id': str(tw.post_id),
                'sentiment': 'neutral',
                'text': 'First twitter post @First_name',
                'type': ['origin'],
                'user_picture': None
            }
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts': [post]})
