from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class Top10AuthorsByWolumeWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    flink = Feedlinks.objects.create()
    sp = Speech.objects.create(language='English (United States)')
    post1 = Post.objects.create(feedlink=flink, entry_title='First post title', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post2 = Post.objects.create(feedlink=flink, entry_title='Second post title', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post3 = Post.objects.create(feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post4 = Post.objects.create(feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post5 = Post.objects.create(feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='EFE', summary_vector=[])
    post6 = Post.objects.create(feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='EFE', summary_vector=[])
    pr = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), end_search_date=datetime(2023, 10, 16), creator=user)
    widget_pk = pr.widgets_list_2.top_authors_id
    url = reverse('widgets:onl_top_authors', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {'entry_author': 'AFP', "author_posts_count": 4},
      {'entry_author': 'EFE', "author_posts_count": 2},
    ]
    self.assertEqual(json.loads(response.content), res)