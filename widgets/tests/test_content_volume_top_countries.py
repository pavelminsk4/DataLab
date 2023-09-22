from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json, os


class ContentVolumeTop5CountriesWidgetTests(APITestCase):

    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'

    def test_response_list(self):
        flink1 = FeedlinksFactory(country='England')
        flink2 = FeedlinksFactory(country='USA')
        PostFactory(feedlink=flink1, entry_published='2021-09-03 00:00:00+00:00', entry_title='1')
        PostFactory(feedlink=flink1, entry_published='2022-09-03 00:00:00+00:00', entry_title='2')
        PostFactory(feedlink=flink2, entry_published='2023-09-03 00:00:00+00:00', entry_title='1')
        PostFactory(feedlink=flink2, entry_published='2023-09-03 00:00:00+00:00', entry_title='2')
        pr1 = ProjectFactory()

        widget_pk = pr1.widgets_list_2.content_volume_top_countries_id
        url = reverse('widgets:onl_content_volume_top_countries',kwargs={'pk': pr1.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'England':
             [{'date': '2021-09-03 00:00:00+00:00', 'post_count': 1},
              {'date': '2022-09-03 00:00:00+00:00', 'post_count': 1},
              {'date': '2023-09-03 00:00:00+00:00', 'post_count': 0}]
             },
            {'USA':
             [{'date': '2021-09-03 00:00:00+00:00', 'post_count': 0},
              {'date': '2022-09-03 00:00:00+00:00', 'post_count': 0},
              {'date': '2023-09-03 00:00:00+00:00', 'post_count': 2}]
             },
        ]
        self.assertEqual(json.loads(response.content), res)


class ContentVolumeTop5CountriesWidgetTestsTLW(APITestCase):

    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'

    def test_response_list_tlw(self):
        flink1 = TalkwalkerFeedlinksFactory(country='England')
        flink2 = TalkwalkerFeedlinksFactory(country='USA')
        TalkwalkerPostFactory(feedlink=flink1, entry_published='2021-09-03 00:00:00+00:00', entry_title='1')
        TalkwalkerPostFactory(feedlink=flink1, entry_published='2022-09-03 00:00:00+00:00', entry_title='2')
        TalkwalkerPostFactory(feedlink=flink2, entry_published='2023-09-03 00:00:00+00:00', entry_title='1')
        TalkwalkerPostFactory(feedlink=flink2, entry_published='2023-09-03 00:00:00+00:00', entry_title='2')
        pr1 = ProjectFactory()

        widget_pk = pr1.widgets_list_2.content_volume_top_countries_id
        url = reverse('widgets:onl_content_volume_top_countries',kwargs={'pk': pr1.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'England':
             [{'date': '2021-09-03 00:00:00+00:00', 'post_count': 1},
              {'date': '2022-09-03 00:00:00+00:00', 'post_count': 1},
              {'date': '2023-09-03 00:00:00+00:00', 'post_count': 0}]
             },
            {'USA':
             [{'date': '2021-09-03 00:00:00+00:00', 'post_count': 0},
              {'date': '2022-09-03 00:00:00+00:00', 'post_count': 0},
              {'date': '2023-09-03 00:00:00+00:00', 'post_count': 2}]
             },
        ]
        self.assertEqual(json.loads(response.content), res)
