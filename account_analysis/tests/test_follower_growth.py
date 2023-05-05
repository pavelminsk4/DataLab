from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from account_analysis.models import ProjectAccountAnalysis
from tweet_binder.models import TweetBinderPost
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json


class FollowerGrowthWidgetTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory()
        TweetBinderPostFactory()
        TweetBinderPostFactory()
        TweetBinderPostFactory(date='2022-10-10T00:00:00+00:00', user_followers='200')
        TweetBinderPostFactory(date='2021-10-10T00:00:00+00:00', user_followers='150')
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.follower_growth_id
        url = reverse('account_analysis:follower_growth_widget', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'aggregation_period': 'day'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [{'2020-10-10 00:00:00+00:00': 100},
               {'2021-10-10 00:00:00+00:00': 150},
               {'2022-10-10 00:00:00+00:00': 200}]
        self.assertEqual(json.loads(response.content), res)
