from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class ContentVolumeTop5CountriesWidgetTests(APITestCase):
    def test_response_list(self):
        flink1 = FeedlinkFactory(country='England')
        flink2 = FeedlinkFactory(country='USA')
        flink3 = FeedlinkFactory(country='England')
        p1 = PostFactory(feedlink=flink1, entry_published='2023-09-03 00:00:00Z', entry_title='1')
        p2 = PostFactory(feedlink=flink1, entry_published='2023-09-04 00:00:00Z', entry_title='2')
        p3 = PostFactory(feedlink=flink1, entry_published='2023-09-05 00:00:00Z', entry_title='3')
        p4 = PostFactory(feedlink=flink2, entry_published='2023-09-05 00:00:00Z', entry_title='1')
        p5 = PostFactory(feedlink=flink2, entry_published='2023-09-05 00:00:00Z', entry_title='2')
        p6 = PostFactory(feedlink=flink3, entry_published='2023-09-05 00:00:00Z', entry_title='2')
        pr = ProjectFactory(start_search_date='2023-09-03T00:00:00Z', end_search_date='2023-09-05T00:00:00Z')
        for post in (p1, p2, p3, p4, p5, p6):
            pr.posts.add(post)
        widget_pk = pr.widgets_list_2.content_volume_top_countries_id
        url = reverse('widgets:onl_content_volume_top_countries', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'England':
             [{'date': '2023-09-03 00:00:00+00:00', 'post_count': 1},
              {'date': '2023-09-04 00:00:00+00:00', 'post_count': 1},
              {'date': '2023-09-05 00:00:00+00:00', 'post_count': 2}]
             },
            {'USA':
             [{'date': '2023-09-03 00:00:00+00:00', 'post_count': 0},
              {'date': '2023-09-04 00:00:00+00:00', 'post_count': 0},
              {'date': '2023-09-05 00:00:00+00:00', 'post_count': 2}]
             },
        ]
        self.assertEqual(json.loads(response.content), res)
