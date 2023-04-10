from project.models import Project, Post, Feedlinks, Speech
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class InfluencersFeatureTests(APITestCase):
  def setUp(self):
    user = User.objects.create(username='Vikernes')
    flink1 = Feedlinks.objects.create(source1='one_source', country='England', sourceurl='google')
    flink2 = Feedlinks.objects.create(source1='two_source', country='USA', sourceurl='youtube')
    flink3 = Feedlinks.objects.create(source1='third_source', country='England', sourceurl='twitter')
    sp1 = Speech.objects.create(language='English')
    sp2 = Speech.objects.create(language='Spanish')
    Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp1, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', summary_vector=[], sentiment='negative')
    Post.objects.create(feedlink=flink2, entry_title='Second post title', feed_language=sp1, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', summary_vector=[], sentiment='positive')
    Post.objects.create(feedlink=flink2, entry_title='Third post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[], sentiment='negative')
    Post.objects.create(feedlink=flink3, entry_title='4 post title', feed_language=sp1, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[], sentiment='neutral')
    Post.objects.create(feedlink=flink3, entry_title='5 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[], sentiment='neutral')
    Post.objects.create(feedlink=flink3, entry_title='6 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='EFE', summary_vector=[], sentiment='positive')

    Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10),
                                end_search_date=datetime(2023, 10, 16), language_filter='', author_filter='', source_filter='', creator=user)

  def test_authors_by_sentiment(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.authors_by_sentiment_id
    url = reverse('widgets:authors_by_sentiment', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'author_count': 2, 'sentiment': 'positive'},
            {'author_count': 1, 'sentiment': 'negative'},
            {'author_count': 1, 'sentiment': 'neutral'},
          ]
    self.assertEqual(json.loads(response.content), res)

  def test_authors_by_language(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.authors_by_language_id
    url = reverse('widgets:authors_by_language', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'feed_language__language': 'Spanish', 'author_count': 2},
            {'feed_language__language': 'English', 'author_count': 1},
          ]
    self.assertEqual(json.loads(response.content), res)

  def test_overall_top_authors(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.overall_top_sources_id
    url = reverse('widgets:overall_top_authors', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
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
