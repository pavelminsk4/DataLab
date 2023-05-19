from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class AverageEngagementsByDayTests(APITestCase):
    def setUp(self):
        for day in range(10, 31):
            for hour in range(10, 24):
                TweetBinderPostFactory(date=f'2020-01-{day}T{hour}:00:00+00:00')
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.optimal_post_time_id
        url = reverse('account_analysis:optimal_post_time',
                      kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = [{'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}, 
                {'engagements': 2.0, 'likes': 3, 'retweets': 3, 'tweets': 3}
                ]
        res = {'Saturday': data, 
               'Friday': data, 
               'Thursday': data, 
               'Wednesday': data, 
               'Tuesday': data, 
               'Monday': data, 
               'Sunday': data}
        self.assertEqual(json.loads(response.content), res)
