from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class InteractiveWidgetsTests(APITestCase):
  def test_top_10_interactive_widgets(self):
    user = User.objects.create(username='Arturo')
    flink1 = Feedlinks.objects.create(country = 'England', source1='Time')
    sp1 = Speech.objects.create(language='English')
    sp2 = Speech.objects.create(language='Georgian')
    post1 = Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp1, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral')
    post2 = Post.objects.create(feedlink=flink1, entry_title='Second post title', feed_language=sp2, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral')
    pr = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10),
                                end_search_date=datetime(2023, 10, 16), creator=user, language_dimensions=['English', 'Georgian'], country_dimensions=['England', 'USA'], 
                                source_dimensions=['Time', 'BBC'], author_dimensions=['AFP'], sentiment_dimensions = ['negative', 'neutral', 'positive'])
    widget_pk = pr.widgets_list_2.top_10_languages_widget_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'language': 'English',
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post1.id)

  def test_sentiment_top_10_interactive_widgets(self):
    user = User.objects.create(username='Arturo')
    flink1 = Feedlinks.objects.create(country = 'England', source1='Time')
    sp1 = Speech.objects.create(language='English')
    sp2 = Speech.objects.create(language='Georgian')
    Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp1, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral')
    Post.objects.create(feedlink=flink1, entry_title='Second post title', feed_language=sp2, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral')
    pr = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10),
                                end_search_date=datetime(2023, 10, 16), creator=user, language_dimensions=['English', 'Georgian'], country_dimensions=['England', 'USA'], 
                                source_dimensions=['Time', 'BBC'], author_dimensions=['AFP'], sentiment_dimensions = ['negative', 'neutral', 'positive'])
    post3 = Post.objects.create(feedlink=flink1, entry_title='3 post title', feed_language=sp2, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', sentiment='negative')
    widget_pk = pr.widgets_list_2.sentiment_top_10_languages_widget_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'language': 'Georgian',
      'sentiment': 'negative',
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(json.loads(response.content)['posts']), 1)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post3.id)
