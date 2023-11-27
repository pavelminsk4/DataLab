from common.factories.feedlink import FeedlinkFactory
from widgets.models import ClippingFeedContentWidget
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class WidgetTests(APITestCase):
    def test_widgett(self):
        flink = FeedlinkFactory(country='Terra', source1='True')
        sp = SpeechFactory(language='English')
        pr1 = ProjectFactory()
        post1 = PostFactory(feedlink=flink, entry_title='First post title', feed_language=sp, entry_published='2021-09-03T06:37:00Z')
        post2 = PostFactory(feedlink=flink, entry_title='Second post title', feed_language=sp, entry_published='2022-09-03T06:37:00Z')
        ClippingFeedContentWidget.objects.create(project=pr1, post=post1)
        ClippingFeedContentWidget.objects.create(project=pr1, post=post2)
        widget_pk = pr1.widgets_list_2.clipping_feed_content_id
        url = reverse('widgets:onl_clipping_feed_content', kwargs={'pk': pr1.id, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 2)
