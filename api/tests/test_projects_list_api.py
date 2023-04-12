from rest_framework.test import APITestCase
from rest_framework import status
from project.models import Project
from datetime import datetime
from django.urls import reverse
import json
from django.contrib.auth.models import User

class TestsProjectsAPI(APITestCase):
  def test_projects_list_api(self):
    user = User.objects.create_user(id=1, username='user')
    pr1 = Project.objects.create(title='Project1', keywords=['Keyword'], start_search_date=datetime(2022, 10, 10), end_search_date=datetime(2022, 10, 16), creator=user)
    pr2 = Project.objects.create(title='Project2', keywords=['Apple'], start_search_date=datetime(2022, 10, 10), end_search_date=datetime(2022, 10, 16), creator=user)
    pr1.created_at = datetime(2022, 10, 17)
    pr1.save()
    pr2.created_at = datetime(2022, 10, 17)
    pr2.save()
    url = reverse('project-list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res1 = {
      "id": pr1.id,
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
      "source": 'Online',
      "start_search_date": "2022-10-10T00:00:00Z",
      "end_search_date": "2022-10-16T00:00:00Z",
      "creator": 1,
      "workspace": None,
      "members": [],
      "created_at": "2022-10-17T00:00:00Z",
      "report_template": None,
      "report_format":'pdf',
      "report_table_content": True,
      "report_widgets": True,
      "report_content": True,
      "report_language": 'English',
      "author_filter": None,
      "language_filter": None,
      "country_filter": None,
      "source_filter": None,
      "sentiment_filter": None,
      "author_dimensions": None,
      "language_dimensions": None,
      "country_dimensions": None,
      "source_dimensions": None,
      "sentiment_dimensions": None,
    }
    res2 = {
      "id": pr2.id,
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
      "source": 'Online',
      "start_search_date": "2022-10-10T00:00:00Z",
      "end_search_date": "2022-10-16T00:00:00Z",
      "creator": 1,
      "workspace": None,
      "members": [],
      "created_at": "2022-10-17T00:00:00Z",
      "report_template": None,
      "report_format":'pdf',
      "report_table_content": True,
      "report_widgets": True,
      "report_content": True,
      "report_language": 'English',
      "author_filter": None,
      "language_filter": None,
      "country_filter": None,
      "source_filter": None,
      "sentiment_filter": None,
      "author_dimensions": None,
      "language_dimensions": None,
      "country_dimensions": None,
      "source_dimensions": None,
      "sentiment_dimensions": None,
    }
    self.assertEqual(json.loads(response.content), [res1, res2])
