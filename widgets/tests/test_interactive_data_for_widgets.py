from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class InteractiveWidgetsTests(APITestCase):
  def setUp(self):
    user = User.objects.create(username='Arturo')
    flink1 = Feedlinks.objects.create(country = 'England', source1='Time')
    sp1 = Speech.objects.create(language='English')
    sp2 = Speech.objects.create(language='Georgian')
    Post.objects.create(feedlink=flink1, entry_title='First post title', entry_summary='First', feed_language=sp1, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral', summary_vector=[])
    Post.objects.create(feedlink=flink1, entry_title='Second post title', entry_summary='Second post post title', feed_language=sp2, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', sentiment='negative', summary_vector=[])
    Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10),
                            end_search_date=datetime(2023, 10, 16), creator=user, language_dimensions=['English', 'Georgian'], country_dimensions=['England', 'USA'], 
                            source_dimensions=['Time', 'BBC'], author_dimensions=['AFP'], sentiment_dimensions = ['negative', 'neutral', 'positive'])

  def test_top_10_interactive_widgets(self):
    pr = Project.objects.first()
    widget_pk = pr.widgets_list_2.top_languages_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post1 = Post.objects.all().get(entry_title='First post title').pk
    data = {
      'first_value': ['English'],
      'second_value': [],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post1)

  def test_sentiment_top_10_interactive_widgets(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='Second post title').pk
    widget_pk = pr.widgets_list_2.sentiment_top_languages_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'second_value': ['negative'],
      'first_value': ['Georgian'],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
  
  def test_sentiment(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='Second post title').pk
    widget_pk = pr.widgets_list_2.sentiment_for_period_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'first_value': ['negative'],
      'second_value': [],
      'dates': [datetime(2022, 1, 3, 6, 37), datetime(2022, 10, 3, 6, 37)],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
  
  def test_content_volume(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='Second post title').pk
    widget_pk = pr.widgets_list_2.volume_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'first_value': [],
      'second_value': [],
      'dates': [datetime(2022, 1, 3, 6, 37), datetime(2022, 10, 3, 6, 37)],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
  
  def test_top_keywords(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='Second post title').pk
    widget_pk = pr.widgets_list_2.top_keywords_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'first_value': ['post'],
      'second_value': [],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
  
  def test_sentiment_top_keywords(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='Second post title').pk
    widget_pk = pr.widgets_list_2.sentiment_top_keywords_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'first_value': ['post'],
      'second_value': ['negative'],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
  
  def test_sentiment_diagram(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='Second post title').pk
    widget_pk = pr.widgets_list_2.sentiment_diagram_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'first_value': ['negative'],
      'second_value': [],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

  def test_authors_by_country(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='First post title').pk
    widget_pk = pr.widgets_list_2.authors_by_country_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'first_value': ['England'],
      'second_value': [],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
  
  def test_authors_by_sentiment(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='First post title').pk
    widget_pk = pr.widgets_list_2.authors_by_sentiment_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'first_value': ['neutral'],
      'second_value': [],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
  
  def test_sources_by_country(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='First post title').pk
    widget_pk = pr.widgets_list_2.sources_by_country_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'first_value': ['England'],
      'second_value': [],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

  def test_sources_by_language(self):
    flink1 = Feedlinks.objects.first()
    sp2 = Speech.objects.get(language='Georgian')
    pr = Project.objects.first()
    post_id = Post.objects.all().get(entry_title='First post title').pk
    widget_pk = pr.widgets_list_2.sources_by_language_id
    url = reverse('widgets:interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
      'first_value': ['English'],
      'second_value': [],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
