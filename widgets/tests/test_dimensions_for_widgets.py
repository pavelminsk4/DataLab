from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import json


class FilterForWidgetsTests(APITestCase):
    def test_response_list(self):
        flink1 = FeedlinksFactory(country='England', source1='Time')
        flink2 = FeedlinksFactory(country='USA', source1='Time')
        flink3 = FeedlinksFactory(country='USA', source1='Time')
        flink4 = FeedlinksFactory(country='Canada', source1='BBC')
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Spain')
        PostFactory(feedlink=flink1, feed_language=sp1, entry_author='AFP', sentiment='neutral')
        PostFactory(feedlink=flink1, feed_language=sp1, entry_author='AFP', sentiment='neutral')
        PostFactory(feedlink=flink2, feed_language=sp1, entry_author='AFP', sentiment='negative')
        PostFactory(feedlink=flink2, feed_language=sp2, entry_author='AFP', sentiment='negative')
        PostFactory(feedlink=flink3, feed_language=sp2, entry_author='AFP', sentiment='positive')
        PostFactory(feedlink=flink3, feed_language=sp2, entry_author='EFE', sentiment='neutral')
        PostFactory(feedlink=flink4, feed_language=sp2, entry_author='AFP', sentiment='neutral')
        PostFactory(feedlink=flink4, feed_language=sp2, entry_author='', sentiment='neutral')
        pr = ProjectFactory(language_dimensions=['English', 'Spain'], country_dimensions=['England', 'USA'], source_dimensions=['Time', 'BBC'], author_dimensions=['AFP'])
        widget_pk = pr.widgets_list_2.sentiment_top_authors_id
        url = reverse('widgets:onl_sentiment_top_authors', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {'AFP': [
            {'sentiment': 'negative', 'sentiment_count': 2},
            {'sentiment': 'neutral', 'sentiment_count': 2},
            {'sentiment': 'positive', 'sentiment_count': 1}
        ]
        }
        self.assertEqual(json.loads(response.content), res)
