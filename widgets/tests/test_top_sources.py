from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json, os


class TopSourcesWidgetTests(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'

    def test_response_list(self):
        flink1 = FeedlinksFactory(source1='one_source')
        flink2 = FeedlinksFactory(source1='two_source')
        flink3 = FeedlinksFactory(source1='third_source')
        p1 = PostFactory(feedlink=flink1, entry_title='1')
        p2 = PostFactory(feedlink=flink1, entry_title='2')
        p3 = PostFactory(feedlink=flink2, entry_title='1')
        p4 = PostFactory(feedlink=flink2, entry_title='2')
        p5 = PostFactory(feedlink=flink3, entry_title='1')
        p6 = PostFactory(feedlink=flink3, entry_title='2')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4, p5,p6):
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


class TopSourcesWidgetTestsTLW(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'

    def test_response_list_tlw(self):
        flink1 = TalkwalkerFeedlinksFactory(source1='one_source')
        flink2 = TalkwalkerFeedlinksFactory(source1='two_source')
        flink3 = TalkwalkerFeedlinksFactory(source1='third_source')
        p1 = TalkwalkerPostFactory(feedlink=flink1, entry_title='1')
        p2 = TalkwalkerPostFactory(feedlink=flink1, entry_title='2')
        p3 = TalkwalkerPostFactory(feedlink=flink2, entry_title='1')
        p4 = TalkwalkerPostFactory(feedlink=flink2, entry_title='2')
        p5 = TalkwalkerPostFactory(feedlink=flink3, entry_title='1')
        p6 = TalkwalkerPostFactory(feedlink=flink3, entry_title='2')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4, p5,p6):
            pr.tw_posts.add(post)
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
