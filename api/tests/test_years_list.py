from rest_framework.test import APITestCase
from rest_framework import status
from project.models import Post, Feedlinks, Speech
from datetime import datetime
from django.urls import reverse
import json

class CountriesTests(APITestCase):
  def create_posts(self):
    flink = Feedlinks.objects.create()
    sp = Speech.objects.create(language='English (United States)')
    post1 = Post.objects.create(feedlink=flink, entry_title='First post title', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37))
    post3 = Post.objects.create(feedlink=flink, entry_title='Second post title', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37))
    post2 = Post.objects.create(feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37))

  def test_countries_list(self):
    self.create_posts()
    url = reverse('years_range')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'year': 2021}, {'year': 2022}, {'year': 2023}])
