from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class SentimentNumberOfResultsTests(APITestCase):
  def setUp(self):
    user = User.objects.create(username='Arturo')
    flink1 = Feedlinks.objects.create(country = 'England', source1='Time')
    sp1 = Speech.objects.create(language='English')
    Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp1, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral', summary_vector=[])
    Post.objects.create(feedlink=flink1, entry_title='Second post title', feed_language=sp1, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', sentiment='positive', summary_vector=[])
    Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10),
                            end_search_date=datetime(2023, 10, 16), creator=user, language_dimensions=[], country_dimensions=[],
                            source_dimensions=[], author_dimensions=[], sentiment_dimensions = [])  

  def test_sentiment_number_of_results(self):
    pr = Project.objects.first()
    res = {'positive': 1, 'negative': 0, 'neutral': 1}
    widget_pk = pr.widgets_list_2.sentiment_number_of_results_id
    url = reverse('widgets:sentiment_number_of_results', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), res)

def test_sentiment_diagram(self):
    pr = Project.objects.first()
    res = {'positive': 1, 'negative': 0, 'neutral': 1}
    widget_pk = pr.widgets_list_2.sentiment_diagram_id
    url = reverse('widgets:sentiment_diagram', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), res)
