from rest_framework.test import APITestCase
from rest_framework import status
from project.models import Post, Feedlinks, Speech, Project
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
import json

class ProjectPostTests(APITestCase):
  def test_project_post_endpoint(self):
    user = User.objects.create(username='Fox')
    flink = Feedlinks.objects.create()
    sp = Speech.objects.create(language='English (United States)')
    pr = Project.objects.create(title='Project1', keywords=['Keyword'], start_search_date=datetime(2022, 10, 10), end_search_date=datetime(2022, 10, 16), creator=user)
    post1 = Post.objects.create(feedlink=flink, entry_title='First post title', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37))
    post3 = Post.objects.create(feedlink=flink, entry_title='Second post title', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37))
    post2 = Post.objects.create(feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37))
    url = reverse('cl_fd_cont_widg_create')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [])
    data = [
      {'project':pr.id, 'post':post1.id},
      {'project':pr.id, 'post':post2.id},
    ]
    self.client.post(url, data, format='json')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {'id': 1, 'project': pr.id, 'post': post1.id},
      {'id': 2, 'project': pr.id, 'post': post2.id},
    ]
    self.assertEqual(json.loads(response.content), res)
