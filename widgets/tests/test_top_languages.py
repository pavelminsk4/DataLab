from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from common.factories.speech import SpeechFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json, os


class TopLanguagesTests(APITestCase):

    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'

    def test_response_list(self):
        flink1 = FeedlinksFactory(country='England')
        flink2 = FeedlinksFactory(country='USA')
        flink3 = FeedlinksFactory(country='Canada')
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Spain')
        PostFactory(feedlink=flink1, feed_language=sp1, entry_title='1')
        PostFactory(feedlink=flink1, feed_language=sp1, entry_title='2')
        PostFactory(feedlink=flink2, feed_language=sp1, entry_title='1')
        PostFactory(feedlink=flink2, feed_language=sp2, entry_title='2')
        PostFactory(feedlink=flink2, feed_language=sp2, entry_title='3')
        PostFactory(feedlink=flink2, feed_language=sp2, entry_title='4')
        PostFactory(feedlink=flink3, feed_language=sp2, entry_title='1')
        PostFactory(feedlink=flink3, feed_language=sp2, entry_title='2')
        pr = ProjectFactory()

        widget_pk = pr.widgets_list_2.top_languages_id
        url = reverse('widgets:onl_top_languages', kwargs={
                      'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'feed_language__language': 'Spain', 'language_count': 5},
            {'feed_language__language': 'English', 'language_count': 3},
        ]
        self.assertEqual(json.loads(response.content), res)


class TopLanguagesTestsTLW(APITestCase):

    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'

    def test_response_list_tlw(self):
        flink1 = TalkwalkerFeedlinksFactory(country='England')
        flink2 = TalkwalkerFeedlinksFactory(country='USA')
        flink3 = TalkwalkerFeedlinksFactory(country='Canada')
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Spain')
        TalkwalkerPostFactory(feedlink=flink1, feed_language=sp1, entry_title='1')
        TalkwalkerPostFactory(feedlink=flink1, feed_language=sp1, entry_title='2')
        TalkwalkerPostFactory(feedlink=flink2, feed_language=sp1, entry_title='1')
        TalkwalkerPostFactory(feedlink=flink2, feed_language=sp2, entry_title='2')
        TalkwalkerPostFactory(feedlink=flink2, feed_language=sp2, entry_title='3')
        TalkwalkerPostFactory(feedlink=flink2, feed_language=sp2, entry_title='4')
        TalkwalkerPostFactory(feedlink=flink3, feed_language=sp2, entry_title='1')
        TalkwalkerPostFactory(feedlink=flink3, feed_language=sp2, entry_title='2')
        pr = ProjectFactory()

        widget_pk = pr.widgets_list_2.top_languages_id
        url = reverse('widgets:onl_top_languages', kwargs={
                      'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'feed_language__language': 'Spain', 'language_count': 5},
            {'feed_language__language': 'English', 'language_count': 3},
        ]
        self.assertEqual(json.loads(response.content), res)
