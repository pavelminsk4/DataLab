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
        PostFactory(feedlink=flink1, entry_title='1')
        PostFactory(feedlink=flink1, entry_title='2')
        PostFactory(feedlink=flink2, entry_title='1')
        PostFactory(feedlink=flink2, entry_title='2')
        PostFactory(feedlink=flink3, entry_title='1')
        PostFactory(feedlink=flink3, entry_title='2')
        pr = ProjectFactory()
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

    def test_response_list(self):
        flink1 = TalkwalkerFeedlinksFactory(source1='one_source')
        flink2 = TalkwalkerFeedlinksFactory(source1='two_source')
        flink3 = TalkwalkerFeedlinksFactory(source1='third_source')
        TalkwalkerPostFactory(feedlink=flink1, entry_title='1')
        TalkwalkerPostFactory(feedlink=flink1, entry_title='2')
        TalkwalkerPostFactory(feedlink=flink2, entry_title='1')
        TalkwalkerPostFactory(feedlink=flink2, entry_title='2')
        TalkwalkerPostFactory(feedlink=flink3, entry_title='1')
        TalkwalkerPostFactory(feedlink=flink3, entry_title='2')
        pr = ProjectFactory()
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
