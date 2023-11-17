from common.factories.expert_filters.preset import PresetFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from api.services.search_service import SearchService
from django.contrib.auth.models import User
from django.test import TestCase
from unittest.mock import Mock
import datetime
import json


class ExpertFilterTests(TestCase):
    def test_project_with_expert_filter(self):
        user = User.objects.create(username='Government')
        self.client.force_login(user)

        ps = PresetFactory(title='First preset', query=['lemon AND salt'], creator=user)
        post1 = PostFactory(entry_title='Fresh lemon')
        post2 = PostFactory(entry_title='A glass of lemon salt water.')
        
        fl = post2.feedlink

        pr = ProjectFactory()
        pr.expert_presets.set([ps])
        pr.posts.set([post1, post2])

        request = Mock()
        body = json.dumps(
            {
                'project_pk': pr.id,
                'date_range': ["2023-11-09T00:00:00", "2023-11-15T10:55:29.806000"],
                'posts_per_page': 10,
                'page_number': 1,
                'sort_posts': '',
                'query_filter': '',
            }
        )
        request.body = body
        request.user.user_profile.department = user.user_profile.department

        res = {
            'num_pages': 1,
            'num_posts': 1,
            'posts': [
                {
                    'id': post2.id,
                    'entry_title': 'A glass of lemon salt water.',
                    'category': None,
                    'entry_author': 'Socrat',
                    'entry_links_href': None,
                    'entry_media_content_url': None,
                    'entry_media_thumbnail_url': None,
                    'entry_published': datetime.datetime(2020, 10, 10, 0, 0, tzinfo=datetime.timezone.utc),
                    'entry_summary': 'post text',
                    'feed_image_href': None,
                    'feed_image_link': None,
                    'feed_language__language': 'English (United States)',
                    'feedlink__alexaglobalrank': fl.alexaglobalrank,
                    'feedlink__country': fl.country,
                    'feedlink__source1': fl.source1,
                    'feedlink__sourceurl': fl.sourceurl,
                    'sentiment': 'neutral',
                }
            ]
        }

        self.assertEqual(SearchService().execute(request), res)
