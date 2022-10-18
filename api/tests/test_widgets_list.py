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
    project = Project.objects.create(title='Test', creator=user)
    url = reverse('widgets_list', kwargs={'pk': project.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {
      "summary_widget": 
        {"name": "Summary", "is_active": False}, 
      "volume_widget":
        {"name": "Content volume", "is_active": False}
      }
    self.assertEqual(json.loads(response.content), res)
    url2 = reverse('update_widgets_list', kwargs={'pk':project.id})
    data = {"summary_widget": True,"volume_widget": False}
    self.client.put(url2, data, format='json')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {
      "summary_widget": 
        {"name": "Summary", "is_active": True}, 
      "volume_widget":
        {"name": "Content volume", "is_active": False}
      }
    self.assertEqual(json.loads(response.content), res)  
