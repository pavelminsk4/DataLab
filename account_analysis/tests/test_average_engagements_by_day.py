from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class AverageEngagementsByDayTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory()
        TweetBinderPostFactory(date='2020-10-11T00:00:00+00:00')
        TweetBinderPostFactory(date='2020-10-12T00:00:00+00:00')
        TweetBinderPostFactory(date='2020-10-13T00:00:00+00:00')
        TweetBinderPostFactory(date='2020-10-14T00:00:00+00:00')
        TweetBinderPostFactory(date='2020-10-15T00:00:00+00:00')
        TweetBinderPostFactory(date='2020-10-16T00:00:00+00:00')
        TweetBinderPostFactory(date='2020-10-17T00:00:00+00:00')
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.average_engagements_by_day_id
        url = reverse('account_analysis:average_engagements_by_day', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = { 'Friday': 2,
                'Monday': 2,
                'Saturday': 4,
                'Sunday': 2,
                'Thursday': 2,
                'Tuesday': 2,
                'Wednesday': 2}
        self.assertEqual(json.loads(response.content), res)
