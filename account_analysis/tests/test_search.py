from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.user import UserFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class SearchTests(APITestCase):

  def test_search(self):
    self.client.force_login(UserFactory())
    tw = TweetBinderPostFactory()
    pr = AccountAnalysisProjectFactory()
    url = reverse('account_analysis:search_posts', kwargs={'project_pk':pr.id})
    response = self.client.post(url, {'posts_per_page': 20, 'page_number': 1}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    posts = {
              'id': tw.pk,
              'post_id': str(tw.post_id),
              'type': ['origin'],
              'inreplyto': None,
              'images': None,
              'user_picture': None,
              'text': 'First twitter post',
              'sentiment': 'neutral',
              'date': '2020-10-10T00:00:00Z',
              'count_totalretweets': 1,
              'count_replies': 1,
              'count_favorites': 1,
              'user_alias': 'First_name',
              'user_name': 'First_name',
              'engagements': 2,
              'link': f'https://twitter.com/user/status/{tw.post_id}'}
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts': [posts]})
