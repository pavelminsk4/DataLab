from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class ProfileTimelineWidgetTests(APITestCase):
  def setUp(self):
        TweetBinderPostFactory()
        TweetBinderPostFactory()
        TweetBinderPostFactory()
        TweetBinderPostFactory()
        TweetBinderPostFactory(date='2021-10-10T00:00:00+00:00')
        AccountAnalysisProjectFactory()

  def test_response_list(self):
    pr = ProjectAccountAnalysis.objects.first()
    widget_pk = pr.account_analysis_widgets_list.profile_timeline_id
    url = reverse('account_analysis:profile_timeline_widget', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    data = {
            'aggregation_period': "day"
           }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'created_count': 4,
            'date': '2020-10-10 00:00:00+00:00',
            'engagement': 8,
            'likes': 4,
            'retweets': 4},
            {'created_count': 1,
            'date': '2021-10-10 00:00:00+00:00',
            'engagement': 2,
            'likes': 1,
            'retweets': 1}
          ]
    self.assertEqual(json.loads(response.content), res)
