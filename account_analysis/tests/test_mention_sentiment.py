from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class MentionSentimentWidgetTests(APITestCase):
  def setUp(self):
        TweetBinderPostFactory(text = 'First twitter post @First_name', sentiment = 'positive')
        TweetBinderPostFactory(text = 'First twitter post @First_name', sentiment = 'positive')
        TweetBinderPostFactory(text = 'First twitter post @First_name')
        TweetBinderPostFactory(date='2021-10-10T00:00:00+00:00', text = 'First twitter post @First_name')
        TweetBinderPostFactory(date='2021-10-10T00:00:00+00:00')
        AccountAnalysisProjectFactory()

  def test_response_list(self):
    pr = ProjectAccountAnalysis.objects.first()
    widget_pk = pr.account_analysis_widgets_list.mention_sentiment_id
    url = reverse('account_analysis:mention_sentiment', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {'positive': 2, 'negative': 0, 'neutral': 2}
    self.assertEqual(json.loads(response.content), res)
