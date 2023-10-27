from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from common.factories.speech import SpeechFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopLanguagesTests(APITestCase):
    def test_response_list(self):
        flink1 = FeedlinkFactory(country='England')
        flink2 = FeedlinkFactory(country='USA')
        flink3 = FeedlinkFactory(country='Canada')
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Spain')
        p1 = PostFactory(feedlink=flink1, feed_language=sp1, entry_title='1')
        p2 = PostFactory(feedlink=flink1, feed_language=sp1, entry_title='2')
        p3 = PostFactory(feedlink=flink2, feed_language=sp1, entry_title='1')
        p4 = PostFactory(feedlink=flink2, feed_language=sp2, entry_title='2')
        p5 = PostFactory(feedlink=flink2, feed_language=sp2, entry_title='3')
        p6 = PostFactory(feedlink=flink2, feed_language=sp2, entry_title='4')
        p7 = PostFactory(feedlink=flink3, feed_language=sp2, entry_title='1')
        p8 = PostFactory(feedlink=flink3, feed_language=sp2, entry_title='2')
        pr = ProjectFactory()

        for post in (p1, p2, p3, p4, p5, p6, p7, p8):
            pr.posts.add(post)

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
