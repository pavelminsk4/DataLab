from django.test import TestCase
from common.factories.feedlink import FeedlinkFactory
from common.factories.status import StatusFactory
from common.factories.speech import SpeechFactory
from project.models import Post
from project.tasks.upload_posts import post_creator
import vcr


class PostsUploadTestCase(TestCase):
    def test_post_creator_succeeds(self):
        """Run post_creator and get data uploaded"""
        FeedlinkFactory(url='http://yaledailynews.com/rss/')
        SpeechFactory(language='English (United States)')
        StatusFactory()

        self.assertEquals(Post.objects.all().count(), 0)

        with vcr.use_cassette('fixtures/vcr_cassettes/celery_post_creator_yaledailynews.yaml'):
            post_creator()

        self.assertEqual(Post.objects.all().count(), 10)

    def test_post_creator_skips_blank_urls(self):
        """Run post_creator and skip blank urls"""
        FeedlinkFactory(url=None)
        SpeechFactory(language='English (United States)')
        StatusFactory()

        self.assertEquals(Post.objects.all().count(), 0)

        with vcr.use_cassette('fixtures/vcr_cassettes/celery_post_creator_yaledailynews.yaml'):
            post_creator()

        self.assertEqual(Post.objects.all().count(), 0)
