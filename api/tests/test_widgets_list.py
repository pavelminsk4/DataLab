from rest_framework.test import APITestCase
from rest_framework import status
from project.models import Project
from widgets.models import WidgetDescription
from datetime import datetime
from django.urls import reverse
import json
from django.contrib.auth.models import User

class WidgetsListTests(APITestCase):
  def test_widgets_list(self):
    user = User.objects.create_user(username='user')
    project = Project.objects.create(id=1, title='Test', creator=user, start_search_date=datetime(2022, 10, 10), end_search_date=datetime(2022, 10, 16))
    url = reverse('widgets_list', kwargs={'pk': project.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {
      'summary_widget':
        {
          'id': WidgetDescription.objects.all()[0].id,
          'is_active': False,
          'title': 'Summary',
          'description': 'Description',
          'aggregation_period': 'day'
        },
      'volume_widget':
        {
          'id': WidgetDescription.objects.all()[1].id,
          'is_active': False,
          'title': 'Content volume',
          'description': 'Description',
          'aggregation_period': 'day'
        },
      'clipping_feed_content_widget':
        {
          'id': WidgetDescription.objects.all()[2].id,
          'is_active': False,
          'title': 'Clipping feed content',
          'description': 'Description',
          'aggregation_period': 'day'
        },
      'top_10_authors_by_volume_widget':
        {
          'id': WidgetDescription.objects.all()[3].id,
          'is_active': False,
          'title': 'Top 10 authors by volume',
          'description': 'Description',
          'aggregation_period': 'day'
        },
      }
    self.assertEqual(json.loads(response.content), res)
    url2 = reverse('update_widgets_list', kwargs={'pk':project.id})
    data = {
      'summary_widget':
        {
          'id':13,
          "is_active": True,
          "title": "New Title",
          "description": "Description",
          "aggregation_period": "day"
        },
      'volume_widget':
        {
          'id':14,
          'is_active': False,
          'title': 'Content volume',
          'description': 'Description',
          'aggregation_period':'day',
        },
      'clipping_feed_content_widget':
        {
          'id':15,
          'is_active': False,
          'title': 'Clipping feed content',
          'description': 'Description',
          'aggregation_period':'day',
        },
      'top_10_authors_by_volume_widget':
        {
          'id':16,
          'is_active': False,
          'title': 'Top 10 authors by volume',
          'description': 'Description',
          'aggregation_period':'day',
        },
      }
    self.client.put(url2, data, format='json')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {
      'summary_widget':
        {
          'id': 13,
          'is_active': True,
          'title': 'New Title',
          'description': 'Description',
          'aggregation_period': 'day',
        },
      'volume_widget':
        {
          'id': 14,
          'is_active': False,
          'title': 'Content volume',
          'description': 'Description',
          'aggregation_period': 'day',
        },
      'clipping_feed_content_widget':
        {
          'id': 15,
          'is_active': False,
          'title': 'Clipping feed content',
          'description': 'Description',
          'aggregation_period': 'day',
        },
      'top_10_authors_by_volume_widget':
        {
          'id': 16,
          'is_active': False,
          'title': 'Top 10 authors by volume',
          'description': 'Description',
          'aggregation_period': 'day',
        },
      }
    self.assertEqual(json.loads(response.content), res)
