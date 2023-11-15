from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class FilterForWidgetsTests(APITestCase):
    def test_response_list(self):
        flink1 = FeedlinkFactory(country='England')
        flink2 = FeedlinkFactory(country='USA')
        flink3 = FeedlinkFactory(country='USA', source1='Time')
        flink4 = FeedlinkFactory(country='Canada', source1='BBC')
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Spain')
        p1 = PostFactory(feedlink=flink1, entry_title='First post title', feed_language=sp1, entry_author='AFP', sentiment='neutral')
        p2 = PostFactory(feedlink=flink1, entry_title='Second post title', feed_language=sp1, entry_author='AFP', sentiment='neutral')
        p3 = PostFactory(feedlink=flink2, entry_title='Third post title', feed_language=sp1, entry_author='AFP', sentiment='negative')
        p4 = PostFactory(feedlink=flink2, entry_title='Fourth title', feed_language=sp2, entry_author='AFP', sentiment='negative')
        p5 = PostFactory(feedlink=flink3, entry_title='Fiveth post title', feed_language=sp2, entry_author='AFP', sentiment='positive')
        p6 = PostFactory(feedlink=flink3, entry_title='Sixth title', feed_language=sp2, entry_author='EFE', sentiment='neutral')
        p7 = PostFactory(feedlink=flink4, entry_title='Seventh title', feed_language=sp2, entry_author='AFP', sentiment='neutral')
        pr = ProjectFactory(additional_keywords=['Third'], ignore_keywords=['First'], author_filter=['AFP'], language_filter=['English'], sentiment_filter=['negative'])
        for post in (p1, p2, p3, p4, p5, p6, p7):
            pr.posts.add(post)
        widget_pk = pr.widgets_list_2.sentiment_top_authors_id
        url = reverse('widgets:onl_sentiment_top_authors', kwargs={
                      'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'AFP': [
                {'sentiment': 'negative', 'sentiment_count': 1},
                {'sentiment': 'neutral', 'sentiment_count': 0},
                {'sentiment': 'positive', 'sentiment_count': 0},
            ]
        }
        self.assertDictEqual(json.loads(response.content), res)
