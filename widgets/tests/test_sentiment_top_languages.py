from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SentimentTopLanguagessWidgetTests(APITestCase):
    def test_response_list(self):
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Spain')
        PostFactory(feed_language=sp1, sentiment='neutral')
        PostFactory(feed_language=sp1, sentiment='neutral')
        PostFactory(feed_language=sp1, sentiment='negative')
        PostFactory(feed_language=sp2, sentiment='negative')
        PostFactory(feed_language=sp2, sentiment='positive')
        PostFactory(feed_language=sp2, sentiment='neutral')
        PostFactory(feed_language=sp2, sentiment='neutral')
        PostFactory(feed_language=sp2, sentiment='neutral')
        pr = ProjectFactory()

        widget_pk = pr.widgets_list_2.sentiment_top_languages_id
        url = reverse('widgets:onl_sentiment_top_languages', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'English':
            [
                {'sentiment': 'neutral', 'sentiment_count': 2},
                {'sentiment': 'negative', 'sentiment_count': 1},
                {'sentiment': 'positive', 'sentiment_count': 0}
            ],
            'Spain':
            [
                {'sentiment': 'neutral', 'sentiment_count': 3},
                {'sentiment': 'negative', 'sentiment_count': 1},
                {'sentiment': 'positive', 'sentiment_count': 1}
            ],
        }
        self.assertEqual(json.loads(response.content), res)
