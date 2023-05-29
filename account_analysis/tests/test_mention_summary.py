from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
import datetime
import json


class MentionSummaryWidgetTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(type=['original', 'reply', 'retweet'], text = 'First twitter post @First_name', user_name = 'Second_name')
        TweetBinderPostFactory(type=['original', 'reply'], text = 'First twitter post @First_name', user_name = 'Third_name')
        TweetBinderPostFactory(text = 'First twitter post @First_name')
        TweetBinderPostFactory(count_retweets='2', count_favorites='2', type=['original', 'reply', 'retweet'], text = 'First twitter post @First_name')
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.mention_summary_id
        url = reverse('account_analysis:mention_summary', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
                'mention': 4, 
                'language': 1, 
                'countries': 1, 
                'authors': 1, 
                'neutral': 4, 
                'negative': 4, 
                'positive': 4, 
                'potential_rates': 400.0
              }
        self.assertEqual(json.loads(response.content), res)
