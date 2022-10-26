from rest_framework.test import APITestCase
from rest_framework import status
from project.models import Workspace, Project
from widgets.models import WidgetsList
from datetime import datetime
from django.urls import reverse
import json
from django.contrib.auth.models import User

class WidgetsListTests(APITestCase):
  def test_widgets_list(self):
    user = User.objects.create_user(username='user')
    project = Project.objects.create(title='Test', creator=user, start_search_date=datetime(2022, 10, 10), end_search_date=datetime(2022, 10, 16))
    url = reverse('widgets_list', kwargs={'pk': project.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {
      'summary_widget': 
        {'name': 'Summary', 'is_active': False}, 
      'volume_widget':
        {'name': 'Content volume', 'is_active': False},
      'clipping_feed_content_widget':
        {'name': 'Clipping feed content', 'is_active': False},
      'top_10_authors_by_volume_widget':
        {'name': 'Top 10 authors by volume', 'is_active': False},
      }
    self.assertEqual(json.loads(response.content), res)
    url2 = reverse('update_widgets_list', kwargs={'pk':project.id})
    data = {
      'summary_widget':True,
      'volume_widget':False,
      'clipping_feed_content_widget':True,
      'top_10_authors_by_volume_widget': True,
      }
    self.client.put(url2, data, format='json')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {
      'summary_widget': 
        {'name': 'Summary', 'is_active': True}, 
      'volume_widget':
        {'name': 'Content volume', "is_active": False},
      'clipping_feed_content_widget':
        {'name': 'Clipping feed content', 'is_active': True},
       'top_10_authors_by_volume_widget':
        {'name': 'Top 10 authors by volume', 'is_active': True},
      }
    self.assertEqual(json.loads(response.content), res)  
