from project.models import Project, Post, Feedlinks, Speech
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class DemographyFeatureTests(APITestCase):
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

  def test_top_sharing_sources(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.top_sharing_sources_id
    url = reverse('widgets:onl_top_sharing_sources', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
        {
          'type': 'Most active site',
          'name': 'third_source',
          'url': 'twitter',
          'value': '3 post',
          'sentiments': {'positive': 1, 'negative': 0, 'neutral': 2},
          'picture': None,
        },
        {
          'type': 'Most influential site',
          'name': 'third_source',
          'url': 'twitter',
          'value': '90210 engagement',
          'sentiments': {'positive': 1, 'negative': 0, 'neutral': 2},
          'picture': None,
        },
    ]
    self.assertEqual(json.loads(response.content), res)
    
  def test_sources_by_country(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.sources_by_country_id
    url = reverse('widgets:onl_sources_by_country', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'feedlink__country': 'England', 'source_count': 2},
            {'feedlink__country': 'USA', 'source_count': 1},
          ]
    self.assertEqual(json.loads(response.content), res)
    
  def test_sources_by_language(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.sources_by_language_id
    url = reverse('widgets:onl_sources_by_language', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'feed_language__language': 'English', 'source_count': 3},
            {'feed_language__language': 'Spanish', 'source_count': 2},
          ]
    self.assertEqual(json.loads(response.content), res)
    
  def test_overall_top_sources(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.overall_top_sources_id
    url = reverse('widgets:onl_overall_top_sources', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {
              'name': 'third_source',
              'url': 'twitter',
              'picture': None,
              'sentiments': {
                'positive': 1,
                'negative': 0,
                'neutral':  2,
              },
              'posts': 3,
              'reach': 0,
              'engagements': 0,
            },
            {
              'name': 'two_source',
              'url': 'youtube',
              'picture': None,
              'sentiments': {
                'positive': 1,
                'negative': 1,
                'neutral':  0,
              },
              'posts': 2,
              'reach': 0,
              'engagements': 0,
            },
            {
              'name': 'one_source',
              'url': 'google',
              'picture': None,
              'sentiments': {
                'positive': 0,
                'negative': 1,
                'neutral':  0,
              },
              'posts': 1,
              'reach': 0,
              'engagements': 0,
            },
          ]
    self.assertEqual(json.loads(response.content), res)
