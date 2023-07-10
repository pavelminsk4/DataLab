from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json


class MostFrequentPostTypeslineWidgetTests(APITestCase):
  def test_response_list(self):
    TweetBinderPostFactory(type=['original', 'reply', 'retweet'])
    TweetBinderPostFactory(type=['original', 'reply'])
    TweetBinderPostFactory(type=['original'])
    TweetBinderPostFactory(type=['original', 'reply', 'retweet'], user_name='Second_name')
    AccountAnalysisProjectFactory()
    pr = ProjectAccountAnalysis.objects.first()
    widget_pk = pr.account_analysis_widgets_list.most_frequent_post_types_id
    url = reverse('account_analysis:most_frequent_post_types_widget', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {'count_tweets': 4,
           'count_replies': 3,
           'count_retweets': 2}
    self.assertEqual(json.loads(response.content), res)
