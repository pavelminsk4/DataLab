from common.factories.project_social import ProjectSocialFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from project_social.models import ProjectSocial
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class SentimentNumberOfResultsTests(APITestCase):
  def setUp(self):
    TweetBinderPostFactory(sentiment_vote='neutral')
    TweetBinderPostFactory(sentiment_vote='positive')
    TweetBinderPostFactory(sentiment_vote='negative')
    ProjectSocialFactory()

  def test_sentiment_number_of_results(self):
    pr = ProjectSocial.objects.first()
    res = {'positive': 1, 'negative': 1, 'neutral': 1}
    widget_pk = pr.social_widgets_list.sentiment_number_of_results_id
    url = reverse('project_social:social_sentiment_number_of_results', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), res)

  def test_sentiment_diagram(self):
    pr = ProjectSocial.objects.first()
    res = {'positive': 1, 'negative': 1, 'neutral': 1}
    widget_pk = pr.social_widgets_list.sentiment_diagram_id
    url = reverse('project_social:social_sentiment_diagram', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), res)
