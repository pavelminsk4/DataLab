from rest_framework.test import APITestCase
from rest_framework import status
from project.models import Project
from datetime import datetime
from django.urls import reverse
import json
from django.contrib.auth.models import User

class TestsProjectsAPI(APITestCase):
  def db_seed(self):
    user = User.objects.create_user(id=1, username='user')
    pr1 = Project.objects.create(title='Project1', keywords=['Keyword'], start_search_date=datetime(2022, 10, 10), end_search_date=datetime(2022, 10, 16), creator=user)
    pr2 = Project.objects.create(title='Project2', keywords=['Apple'], start_search_date=datetime(2022, 10, 10), end_search_date=datetime(2022, 10, 16), creator=user)
    pr1.created_at = datetime(2022, 10, 17)
    pr1.save()
    pr2.created_at = datetime(2022, 10, 17)
    pr2.save()

  def test_projects_list_api(self):
    self.db_seed()
    url = reverse('projects_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {
        "id": 1,
        "note": None,
        "title": "Project1",
        "keywords": ['Keyword'],
        "ignore_keywords": None,
        "additional_keywords": None,
        "max_items": None,
        "image": None,
        "arabic_name": None,
        "english_name": None,
        "social": False,
        "online": False,
        "premium": False,
        "source": None,
        "start_search_date": "2022-10-10T00:00:00Z",
        "end_search_date": "2022-10-16T00:00:00Z",
        "creator": 1,
        "workspace": None,
        "members": [],
        "created_at": "2022-10-17T00:00:00Z",
      },
      {
        "id": 2,
        "note": None,
        "title": "Project2",
        "keywords": ['Apple'],
        "ignore_keywords": None,
        "additional_keywords": None,
        "max_items": None,
        "image": None,
        "arabic_name": None,
        "english_name": None,
        "social": False,
        "online": False,
        "premium": False,
        "source": None,
        "start_search_date": "2022-10-10T00:00:00Z",
        "end_search_date": "2022-10-16T00:00:00Z",
        "creator": 1,
        "workspace": None,
        "members": [],
        "created_at": "2022-10-17T00:00:00Z",
      }
    ]
    self.assertEqual(json.loads(response.content), res)
