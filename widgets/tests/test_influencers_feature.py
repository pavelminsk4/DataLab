from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from project.models import Project
from rest_framework import status
from django.urls import reverse
import json

class InfluencersFeatureTests(APITestCase):
  def setUp(self):
    flink1 = FeedlinksFactory(source1='one_source', country='England', sourceurl='google')
    flink2 = FeedlinksFactory(source1='two_source', country='USA', sourceurl='youtube')
    flink3 = FeedlinksFactory(source1='third_source', country='England', sourceurl='twitter')
    sp1 = SpeechFactory(language='English')
    sp2 = SpeechFactory(language='Spanish')
    PostFactory(feedlink=flink1, feed_language=sp1, entry_author='AFP', sentiment='negative')
    PostFactory(feedlink=flink2, feed_language=sp1, entry_author='AFP', sentiment='positive')
    PostFactory(feedlink=flink2, feed_language=sp2, entry_author='AFP', sentiment='negative')
    PostFactory(feedlink=flink3, feed_language=sp1, entry_author='AFP', sentiment='neutral')
    PostFactory(feedlink=flink3, feed_language=sp2, entry_author='AFP', sentiment='neutral')
    PostFactory(feedlink=flink3, feed_language=sp2, entry_author='EFE', sentiment='positive')
    ProjectFactory()

  def test_authors_by_sentiment(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.authors_by_sentiment_id
    url = reverse('widgets:onl_authors_by_sentiment', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {
            'negative': [['AFP', 2]],
            'neutral': [['AFP', 2]],
            'positive': [['AFP', 1], ['EFE', 1]]
          }
    self.assertEqual(json.loads(response.content), res)

  def test_authors_by_language(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.authors_by_language_id
    url = reverse('widgets:onl_authors_by_language', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'Spanish': [['AFP', 2], ['EFE', 1]]}, 
            {'English': [['AFP', 3]]}
          ]
    self.assertEqual(json.loads(response.content), res)

  def test_overall_top_authors(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.overall_top_sources_id
    url = reverse('widgets:onl_overall_top_authors', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {
              'name': 'AFP',
              'url': 'google',
              'picture': None,
              'sentiments': {
                'positive': 1,
                'negative': 2,
                'neutral':  2,
              },
              'posts': 5,
              'reach': 0,
              'engagements': 0,
            },
            {
              'name': 'EFE',
              'url': 'twitter',
              'picture': None,
              'sentiments': {
                'positive': 1,
                'negative': 0,
                'neutral':  0,
              },
              'posts': 1,
              'reach': 0,
              'engagements': 0,
            },
          ]
    self.assertEqual(json.loads(response.content), res)
