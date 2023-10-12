from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from project.models import Speech
from project.models import Speech
from rest_framework import status
from django.urls import reverse
import json


class ProjectPostTests(APITestCase):
    def test_project_post_endpoint(self):
        user = User.objects.create(username='Fox')
        flink = FeedlinksFactory()
        sp = Speech.objects.create(language='English (United States)')
        pr = ProjectFactory(
          title='Project1',
          keywords=['Keyword'],
          start_search_date="2022-10-10T00:00:00Z",
          end_search_date="2022-10-16T00:00:00Z",
          creator=user
          )
        post1 = PostFactory(feedlink=flink, entry_title='First post title', feed_language=sp, entry_published="2021-09-03T00:00:00Z")
        post3 = PostFactory(feedlink=flink, entry_title='Second post title', feed_language=sp, entry_published="2022-09-03T00:00:00Z")
        post2 = PostFactory(feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published="2023-09-03T00:00:00Z")
        url = reverse('cl_fd_cont_widg_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [])
        data = [
          {'project':pr.id, 'post':post1.id},
          {'project':pr.id, 'post':post2.id},
        ]
