from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class SearchTests(APITestCase):

  def db_seeder(self):
        TweetBinderPostFactory()
        AccountAnalysisProjectFactory()

  def test_search(self):
    self.db_seeder()
    pr = ProjectAccountAnalysis.objects.first()
    url = reverse('account_analysis:search_posts', kwargs={'project_pk':pr.pk})
    response = self.client.post(url, {'posts_per_page': 20, 'page_number': 1}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    posts = {
                'count_favorites': 1,
                'count_replies': 1,
                'count_totalretweets': None,
                'date': '2020-10-10T00:00:00Z',
                'engagement': 2,
                'id': 1,
                'images': None,
                'inreplyto': None,
                'link': 'https://twitter.com/user/status/0',
                'post_id': '0',
                'sentiment': 'neutral',
                'text': 'First twitter post',
                'type': ['origin'],
                'user_picture': None
            }
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts': [posts]})
