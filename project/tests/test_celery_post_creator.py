from django.test import TestCase
from common.factories.feedlinks import FeedlinksFactory
from common.factories.status import StatusFactory
from project.models import Post
from project.tasks import post_creator
import vcr


class PostsUploadTestCase(TestCase):
    def test_post_creator_succeeds(self):
        """Run post_creator and get data uploaded"""
        FeedlinksFactory(url='http://yaledailynews.com/rss/')
        StatusFactory()

        self.assertEquals(Post.objects.all().count(), 0)
        with vcr.use_cassette('fixtures/vcr_cassettes/celery_post_creator_yaledailynews.yaml'):
            post_creator()

        self.assertEquals(Post.objects.all().count(), 10)
