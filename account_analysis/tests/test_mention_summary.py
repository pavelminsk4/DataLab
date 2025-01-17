from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class MentionSummaryWidgetTests(APITestCase):
    maxDiff = None

    def setUp(self):
        TweetBinderPostFactory(type=['original', 'reply', 'retweet'], text='First twitter post @First_name', user_name='Second_name', user_alias='Second_name')
        TweetBinderPostFactory(type=['original', 'reply'], text='First twitter post @First_name', user_name='Third_name', user_alias='Third_name')
        TweetBinderPostFactory(text='First twitter post @First_name', user_alias='First_name', user_name='First_name')
        TweetBinderPostFactory(count_totalretweets='2', count_favorites='2', type=['original', 'reply', 'retweet'], text='First twitter post @First_name')
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.mention_summary_id
        url = reverse('account_analysis:mention_summary', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'location': 'United States',
            'stats': {
                'authors': 3,
                'countries': 1,
                'language': 1,
                'mention': 4,
                'negative': 0,
                'neutral': 4,
                'positive': 0,
                'potential_rates': 400.0
            },
            'user_alias': 'First_name',
            'user_bio': None,
            'user_name': 'First_name',
            'user_picture': None,
            'user_value': 100.0,
            'verified': False
        }
        self.assertEqual(json.loads(response.content), res)
