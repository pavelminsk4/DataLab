from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class TopKeywordsTests(APITestCase):
  def setUp(self):
    user = User.objects.create(username='Arturo')
    flink1 = Feedlinks.objects.create(country = 'England', source1='Time')
    sp1 = Speech.objects.create(language='English')
    Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp1, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral',
                        entry_summary = 'the keyword uno dos')
    Post.objects.create(feedlink=flink1, entry_title='Second post title', feed_language=sp1, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral',
                        entry_summary = 'the keyword text',)
    Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10),
                                end_search_date=datetime(2023, 10, 16), creator=user, language_dimensions=[], country_dimensions=[], 
                                source_dimensions=[], author_dimensions=[], sentiment_dimensions = [])
  
  def test_top_keywords_api(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.top_keywords_id
    url = reverse('widgets:top_keywords', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'key': 'keyword', 'value': 1.0},
            {'key': 'text', 'value': 0.5},
          ]
    self.assertEqual(json.loads(response.content), res)
    
  def test_sentiment_top_keywords_api(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.sentiment_top_keywords_id
    url = reverse('widgets:sentiment_top_keywords', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {'negative': [],
           'neutral': [{'key': 'keyword', 'value': 1.0}, {'key': 'text', 'value': 0.5}],
           'positive': []}
    self.assertEqual(json.loads(response.content), res)
