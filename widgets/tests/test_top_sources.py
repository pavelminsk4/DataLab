from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopSourcesWidgetTests(APITestCase):
    def test_response_list(self):
        flink1 = FeedlinkFactory(source1='one_source')
        flink2 = FeedlinkFactory(source1='two_source')
        flink3 = FeedlinkFactory(source1='third_source')
        p1 = PostFactory(feedlink=flink1, entry_title='1')
        p2 = PostFactory(feedlink=flink1, entry_title='2')
        p3 = PostFactory(feedlink=flink2, entry_title='1')
        p4 = PostFactory(feedlink=flink2, entry_title='2')
        p5 = PostFactory(feedlink=flink3, entry_title='1')
        p6 = PostFactory(feedlink=flink3, entry_title='2')
        pr = ProjectFactory()

        for post in (p1, p2, p3, p4, p5, p6):
            pr.posts.add(post)

        widget_pk = pr.widgets_list_2.top_sources_id
        url = reverse('widgets:onl_top_sources', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'brand_count': 2, 'feedlink__source1': 'one_source'},
            {'brand_count': 2, 'feedlink__source1': 'third_source'},
            {'brand_count': 2, 'feedlink__source1': 'two_source'}
        ]
        self.assertEqual(json.loads(response.content), res)
