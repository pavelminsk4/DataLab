from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
import datetime
import json


class TopMentionsByEngagementsWidgetTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(type=['original', 'reply', 'retweet'], text = 'First twitter post @First_name', user_name = 'Second_name')
        TweetBinderPostFactory(type=['original', 'reply'], text = 'First twitter post @First_name', user_name = 'Third_name')
        TweetBinderPostFactory(text = 'First twitter post @First_name')
        TweetBinderPostFactory(count_retweets='2', count_favorites='2', type=['original', 'reply', 'retweet'], text = 'First twitter post @First_name')
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.top_mentions_by_engagements_id
        url = reverse('account_analysis:top_mentions_by_engagements', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
                {'name': 'First_name', 'text': 'First twitter post @First_name', 'sentiment': 'neutral', 'engagement': 4, 'likes': 2, 'retweets': 2, 'date': 'Oct 10, 2020 12:00 AM'}, 
                {'name': 'Second_name', 'text': 'First twitter post @First_name', 'sentiment': 'neutral', 'engagement': 2, 'likes': 1, 'retweets': 1, 'date': 'Oct 10, 2020 12:00 AM'}, 
                {'name': 'Third_name', 'text': 'First twitter post @First_name', 'sentiment': 'neutral', 'engagement': 2, 'likes': 1, 'retweets': 1, 'date': 'Oct 10, 2020 12:00 AM'}, 
                {'name': 'First_name', 'text': 'First twitter post @First_name', 'sentiment': 'neutral', 'engagement': 2, 'likes': 1, 'retweets': 1, 'date': 'Oct 10, 2020 12:00 AM'}
              ]
        self.assertEqual(json.loads(response.content), res)
