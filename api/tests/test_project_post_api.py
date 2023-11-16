from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from common.factories.user import UserFactory
from common.factories.workspace import WorkspaceFactory
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from project.models import Speech, Project
from django.urls import reverse
import json

from unittest.mock import patch


class ProjectPostTests(APITestCase):

    @patch('api.services.collect_service.CollectService.rss')
    @patch('api.services.collect_service.CollectService.talkwalker')
    def test_project_created(self, talkwalker, rss):
        """Project is created and runs a Celary task"""
        self.client.force_login(UserFactory())

        params = {
            'title': 'Project 1',
            'keywords': ['nothing', 'special'],
            'note': 'nope',
            'start_search_date': '2023-10-31T00:00:00Z',
            'end_search_date': '2023-10-31T00:00:00Z',
            'creator': UserFactory().id,
            'workspace': WorkspaceFactory().id,
            'sources': ['rss'],
        }

        response = self.client.post('/api/projects/', params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        rss.assert_called()
        talkwalker.assert_not_called()

        content = json.loads(response.content)
        self.assertEqual(content['title'], 'Project 1')
        self.assertEqual(content['keywords'], ['nothing', 'special'])
        self.assertEqual(content['start_date'], '2023-10-31T00:00:00Z')
        self.assertEqual(content['sources'], ['rss'])

    def test_rss_project_created(self):
        """Project is created with source RSS and data is collected"""
        flink = FeedlinkFactory()
        lang  = Speech.objects.create(language='English (United States)')

        PostFactory(feedlink=flink, entry_title='Trump', feed_language=lang, entry_published='2023-10-30T00:00:00Z')
        PostFactory(feedlink=flink, entry_title='Biden', feed_language=lang, entry_published='2023-10-30T00:00:00Z')

        self.client.force_login(UserFactory())

        params = {
            'title': 'Project 1',
            'keywords': ['trump'],
            'note': 'nope',
            'start_search_date': '2023-10-24T00:00:00Z',
            'end_search_date': '2023-10-31T00:00:00Z',
            'creator': UserFactory().id,
            'workspace': WorkspaceFactory().id,
            'sources': ['rss'],
        }

        response = self.client.post('/api/projects/', params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        project = Project.objects.all().first()
        self.assertEqual(project.status, Project.STATUS_ACTIVE)
        self.assertEqual(project.posts.count(), 1)
        self.assertEqual(project.posts.first().entry_title, 'Trump')

    def test_clipping_feed_widget_created(self):
        user  = User.objects.create(username='Fox')
        flink = FeedlinkFactory()
        lang  = Speech.objects.create(language='English (United States)')

        ProjectFactory(
            title='Project1',
            keywords=['Keyword'],
            start_search_date='2022-10-10T00:00:00Z',
            end_search_date='2022-10-16T00:00:00Z',
            creator=user
        )

        PostFactory(feedlink=flink, entry_title='First post title', feed_language=lang, entry_published='2021-09-03T00:00:00Z')
        PostFactory(feedlink=flink, entry_title='Third post title', feed_language=lang, entry_published='2023-09-03T00:00:00Z')
        PostFactory(feedlink=flink, entry_title='Second post title', feed_language=lang, entry_published='2022-09-03T00:00:00Z')

        url = reverse('cl_fd_cont_widg_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [])
