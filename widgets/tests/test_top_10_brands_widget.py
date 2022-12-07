from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class Top10BrandsWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    flink1 = Feedlinks.objects.create(source1='one_source', country = 'England')
    flink2 = Feedlinks.objects.create(source1='two_source', country = 'USA')
    flink3 = Feedlinks.objects.create(source1='third_source', country = 'USA')
    sp = Speech.objects.create(language='English (United States)')
    post1 = Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP')
    post2 = Post.objects.create(feedlink=flink1, entry_title='Second post title', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP')
    post3 = Post.objects.create(feedlink=flink2, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP')
    post4 = Post.objects.create(feedlink=flink2, entry_title='4 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP')
    post5 = Post.objects.create(feedlink=flink3, entry_title='5 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP')
    post6 = Post.objects.create(feedlink=flink3, entry_title='6 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='EFE')
    pr = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), author_filter = 'AFP', language_filter=sp, country_filter='USA', creator=user)
    url = reverse('widgets:top_10_brands_widget', kwargs={'pk':pr.pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {'feedlink__source1': 'two_source', 'brand_count': 2},
      {'feedlink__source1': 'third_source', 'brand_count': 1},
    ]
    self.assertEqual(json.loads(response.content), res)