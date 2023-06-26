from common.factories.feedlinks import FeedlinksFactory
from common.factories.post import PostFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from widgets.models import ClippingFeedContentWidget
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class WidgetTests(APITestCase):
    def test_widgett(self):
        flink = FeedlinksFactory(country='Terra', source1='True')
        sp = SpeechFactory(language='English')
        pr1 = ProjectFactory()
        post1 = PostFactory(id=1, feedlink=flink, entry_title='First post title', feed_language=sp, entry_published='2021-09-03T06:37:00Z')
        post2 = PostFactory(id=2, feedlink=flink, entry_title='Second post title', feed_language=sp, entry_published='2022-09-03T06:37:00Z')
        ClippingFeedContentWidget.objects.create(project=pr1, post=post1)
        ClippingFeedContentWidget.objects.create(project=pr1, post=post2)
        widget_pk = pr1.widgets_list_2.clipping_feed_content_id
        url = reverse('widgets:onl_clipping_feed_content', kwargs={'pk': pr1.id, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pst1 = {
            'post__id': 2,
            'post__entry_title': 'Second post title',
            'post__entry_published': '2022-09-03T06:37:00Z',
            'post__entry_summary': 'post text',
            'post__entry_author': 'Socrat',
            'post__entry_links_href': None,
            'post__entry_media_thumbnail_url': None,
            'post__entry_media_content_url': None,
            'post__feed_image_href': None,
            'post__feed_image_link': None,
            'post__feed_language__language': 'English',
            'post__feedlink__country': 'Terra',
            'post__feedlink__source1': 'True',
            'post__feedlink__sourceurl': None,
            'post__sentiment': 'neutral',
            'post__feedlink__alexaglobalrank': 0,
        }
        pst2 = {
            'post__id': 1,
            'post__entry_title': 'First post title',
            'post__entry_published': '2021-09-03T06:37:00Z',
            'post__entry_summary': 'post text',
            'post__entry_author': 'Socrat',
            'post__feed_image_href': None,
            'post__entry_media_thumbnail_url': None,
            'post__entry_media_content_url': None,
            'post__entry_links_href': None,
            'post__feed_image_link': None,
            'post__feed_language__language': 'English',
            'post__feedlink__country': 'Terra',
            'post__feedlink__source1': 'True',
            'post__feedlink__sourceurl': None,
            'post__sentiment': 'neutral',
            'post__feedlink__alexaglobalrank': 0,
        }
        self.assertEqual(json.loads(response.content), [pst2, pst1])
