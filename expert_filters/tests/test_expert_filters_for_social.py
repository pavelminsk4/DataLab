from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from common.factories.expert_filters.preset import PresetFactory
from common.factories.user import UserFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TestSocialExpertFilters(APITestCase):
    def test_search_with_expert_preset(self):
        TweetBinderPostFactory(text='bird', sentiment='positive')
        TweetBinderPostFactory(text='bird dog', sentiment='negative')
        TweetBinderPostFactory(text='dog cat', sentiment='positive')
        TweetBinderPostFactory(text='bird', user_location='Scotland')
        TweetBinderPostFactory(text='wolf cat bear', user_location='Scotland')
        TweetBinderPostFactory(text='wolf', sentiment='positive')
        TweetBinderPostFactory(text='cat bear cow', user_followers=100)
        TweetBinderPostFactory(text='bear bird wolf cat', user_followers=200)
        TweetBinderPostFactory(text='dog bird wolf', user_followers=200)
        aim = TweetBinderPostFactory(post_id=41111111, user_name='Elon', user_alias='Musk', text='cat fish', sentiment='negative',
                                     date='2022-09-02T06:44:00.000Z', user_location='USA', language='Arabic', count_favorites=11, count_totalretweets=13, count_replies=1994)

        pr = ProjectSocialFactory()
        ps = PresetFactory(query=['cat AND fish'])
        pr.expert_presets.add(ps.id)

        self.client.force_login(UserFactory())
        data = {
            'keywords': ['cat'],
            'exceptions': [],
            'additions': [],
            'country': [],
            'language': [],
            'sentiment': [],
            'date_range': ['2018-09-02T06:44:00Z', '2024-09-30T06:44:00Z'],
            'source': [],
            'author': [],
            'posts_per_page': 20,
            'page_number': 1,
            'author_dimensions': [],
            'language_dimensions': [],
            'country_dimensions': [],
            'source_dimensions': [],
            'sentiment_dimensions': [],
            'query_filter': '',
            'expert_mode': False,
            'project_pk': pr.id,
        }
        url = reverse('project_social:twitter_posts_search')
        response = self.client.post(url, data, format='json')

        res = {
            'num_pages': 1,
            'num_posts': 1,
            'posts':
                [
                    {
                        'id': aim.id,
                        'post_id': '41111111',
                        'user_name': 'Elon',
                        'user_alias': 'Musk',
                        'text': 'cat fish',
                        'sentiment': 'negative',
                        'date': '2022-09-02T06:44:00Z',
                        'user_location': 'USA',
                        'link': 'https://twitter.com/user/status/41111111',
                        'language': 'Arabic',
                        'count_favorites': 11,
                        'count_totalretweets': 13,
                        'count_replies': 1994,
                        'user_picture': None,
                        'images': None
                    }
                ]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), res)
