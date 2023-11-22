from django.test import TestCase
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from common.factories.feedlink import FeedlinkFactory
from common.factories.speech import SpeechFactory
from project.models import Project
from api.services.collect_service import CollectService
from api.services.rss_search_service import RssSearchService


class RssSearchServiceTests(TestCase):
    def test_rss_search_service_updates_posts(self):
        """RSS Search Service uploads new posts only"""
        flink = FeedlinkFactory()
        lang  = SpeechFactory()

        project = ProjectFactory(
            status=Project.STATUS_ACTIVE,
            start_search_date='2023-10-24T00:00:00Z',
            end_search_date='2023-10-30T00:00:00Z',
            sources=['rss'],
            keywords=['Saudi']
        )

        PostFactory(feedlink=flink, entry_title='Just Initial', feed_language=lang, entry_published='2023-10-30T00:00:00Z')
        PostFactory(feedlink=flink, entry_title='Saudi Initial', feed_language=lang, entry_published='2023-10-30T00:00:00Z')
        PostFactory(feedlink=flink, entry_title='Saudi New', feed_language=lang, entry_published='2023-11-05T00:00:00Z')
        PostFactory(feedlink=flink, entry_title='Just Outside', feed_language=lang, entry_published='2023-11-05T00:00:00Z')
        PostFactory(feedlink=flink, entry_title='Saudi Outside', feed_language=lang, entry_published='2023-09-30T00:00:00Z')

        CollectService().execute(project.id)
        project.refresh_from_db()

        self.assertIsNotNone(project.synched_at)
        self.assertEqual(project.posts.count(), 1)
        self.assertEqual(project.posts.last().entry_title, 'Saudi Initial')

        project.synched_at = '2023-11-02T00:00:00Z'
        project.save()

        RssSearchService().execute(project.id)
        project.refresh_from_db()

        self.assertNotEqual(project.synched_at, '2023-11-02T00:00:00Z')
        self.assertEqual(project.posts.count(), 2)
        self.assertEqual(project.posts.last().entry_title, 'Saudi New')
