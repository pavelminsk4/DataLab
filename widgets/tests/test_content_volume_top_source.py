from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class ContentVolumeTopSourcesWidgetTests(APITestCase):
    def test_response_list(self):
        flink1 = FeedlinksFactory(source1='BBC')
        flink2 = FeedlinksFactory(source1='Time')
        PostFactory(feedlink=flink1, entry_published='2021-09-03 00:00:00+00:00')
        PostFactory(feedlink=flink1, entry_published='2022-09-03 00:00:00+00:00')
        PostFactory(feedlink=flink2, entry_published='2023-09-03 00:00:00+00:00')
        PostFactory(feedlink=flink2, entry_published='2023-09-03 00:00:00+00:00')
        pr1 = ProjectFactory()

        widget_pk = pr1.widgets_list_2.content_volume_top_sources_id
        url = reverse('widgets:onl_content_volume_top_sources', kwargs={'pk': pr1.pk, 'widget_pk': widget_pk})
        data = {'aggregation_period': 'day'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res1 = [
            {'BBC': [{'date': '2021-09-03 00:00:00+00:00', 'post_count': 1},
                     {'date': '2022-09-03 00:00:00+00:00', 'post_count': 1},
                     {'date': '2023-09-03 00:00:00+00:00', 'post_count': 0}
                     ]},
            {'Time': [{'date': '2021-09-03 00:00:00+00:00', 'post_count': 0},
                      {'date': '2022-09-03 00:00:00+00:00', 'post_count': 0},
                      {'date': '2023-09-03 00:00:00+00:00', 'post_count': 2}
                      ]},
        ]
        self.assertEqual(json.loads(response.content), res1)
