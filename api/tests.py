from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from project.models import Post
import json

class SearchTests(APITestCase):
  def test_search(self):
    Post.objects.create(entry_title='USA Abama')
    Post.objects.create(entry_title='RUS Putin')
    data = {'keywords': ['Putin', 'abama'] }
    url = reverse('search')
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'entry_media_thumbnail_url': None, 'entry_published': None, 'entry_summary': None, 'entry_title':'RUS Putin', 'feed_language': None}])  
