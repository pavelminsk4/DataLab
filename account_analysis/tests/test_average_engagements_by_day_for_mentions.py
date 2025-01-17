from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class AverageEngagementsByDayForMentionsTests(APITestCase):
    def setUp(self):
        for i in range(10, 18):
            TweetBinderPostFactory(date=f'2020-10-{i}T00:00:00Z', text='First twitter post @First_name')
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.average_engagements_by_day_for_mentions_id
        url = reverse('account_analysis:average_engagements_by_day_for_mentions', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
                'Friday': 2.0,
                'Monday': 2.0,
                'Saturday': 2.0,
                'Sunday': 2.0,
                'Thursday': 2.0,
                'Tuesday': 2.0,
                'Wednesday': 2.0
              }
        self.assertEqual(json.loads(response.content), res)
