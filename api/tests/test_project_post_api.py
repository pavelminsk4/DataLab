from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
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
from datetime import datetime
import json
import os


class ProjectPostTestsTLW(APITestCase):
    
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'

    def test_project_post_endpoint_tlw(self):
        user = User.objects.create(username='Fox')
        flink = TalkwalkerFeedlinksFactory()
        sp = Speech.objects.create(language='English (United States)')
        pr = ProjectFactory(
          title='Project1',
          keywords=['Keyword'],
          start_search_date=datetime(2022, 10, 10),
          end_search_date=datetime(2022, 10, 16),
          creator=user
          )
        post1 = TalkwalkerPostFactory(feedlink=flink, entry_title='First post title', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37))
        post3 = TalkwalkerPostFactory(feedlink=flink, entry_title='Second post title', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37))
        post2 = TalkwalkerPostFactory(feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37))
        url = reverse('cl_fd_cont_widg_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [])
        data = [
          {'project':pr.id, 'post':post1.id},
          {'project':pr.id, 'post':post2.id},
        ]


class ProjectPostTests(APITestCase):
   
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'

    def test_project_post_endpoint(self):
        user = User.objects.create(username='Fox')
        flink = FeedlinksFactory()
        sp = Speech.objects.create(language='English (United States)')
        pr = ProjectFactory(
          title='Project1',
          keywords=['Keyword'],
          start_search_date=datetime(2022, 10, 10),
          end_search_date=datetime(2022, 10, 16),
          creator=user
          )
        post1 = PostFactory(feedlink=flink, entry_title='First post title', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37))
        post3 = PostFactory(feedlink=flink, entry_title='Second post title', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37))
        post2 = PostFactory(feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37))
        url = reverse('cl_fd_cont_widg_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [])
        data = [
          {'project':pr.id, 'post':post1.id},
          {'project':pr.id, 'post':post2.id},
        ]
