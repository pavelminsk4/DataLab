from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json, os


class ContentVolumeTop5AuthorsWidgetTests(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'

    def test_response_list(self):
        p1 = PostFactory(entry_published='2021-09-03 00:00:00+00:00', entry_author='AFP')
        p2 = PostFactory(entry_published='2022-09-03 00:00:00+00:00', entry_author='AFP')
        p3 = PostFactory(entry_published='2023-09-03 00:00:00+00:00', entry_author='EFE')
        p4 = PostFactory(entry_published='2023-09-03 00:00:00+00:00', entry_author='AFP')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4):
            pr.posts.add(post)
        widget_pk = pr.widgets_list_2.content_volume_top_authors_id
        url = reverse('widgets:onl_content_volume_top_authors', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'AFP': [
                {'date': '2021-09-03 00:00:00+00:00', 'post_count': 1},
                {'date': '2022-09-03 00:00:00+00:00', 'post_count': 1},
                {'date': '2023-09-03 00:00:00+00:00', 'post_count': 1}
            ]},
            {'EFE': [
                {'date': '2021-09-03 00:00:00+00:00', 'post_count': 0},
                {'date': '2022-09-03 00:00:00+00:00', 'post_count': 0},
                {'date': '2023-09-03 00:00:00+00:00', 'post_count': 1}
            ]},
        ]
        self.assertEqual(json.loads(response.content), res)


class ContentVolumeTop5AuthorsWidgetTestsTLW(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'

    def test_response_list_tlw(self):
        p1 = TalkwalkerPostFactory(entry_published='2021-09-03 00:00:00+00:00', entry_author='AFP')
        p2 = TalkwalkerPostFactory(entry_published='2022-09-03 00:00:00+00:00', entry_author='AFP')
        p3 = TalkwalkerPostFactory(entry_published='2023-09-03 00:00:00+00:00', entry_author='EFE')
        p4 = TalkwalkerPostFactory(entry_published='2023-09-03 00:00:00+00:00', entry_author='AFP')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4):
            pr.tw_posts.add(post)
        widget_pk = pr.widgets_list_2.content_volume_top_authors_id
        url = reverse('widgets:onl_content_volume_top_authors', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'AFP': [
                {'date': '2021-09-03 00:00:00+00:00', 'post_count': 1},
                {'date': '2022-09-03 00:00:00+00:00', 'post_count': 1},
                {'date': '2023-09-03 00:00:00+00:00', 'post_count': 1}
            ]},
            {'EFE': [
                {'date': '2021-09-03 00:00:00+00:00', 'post_count': 0},
                {'date': '2022-09-03 00:00:00+00:00', 'post_count': 0},
                {'date': '2023-09-03 00:00:00+00:00', 'post_count': 1}
            ]},
        ]
        self.assertEqual(json.loads(response.content), res)
