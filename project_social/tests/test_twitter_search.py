from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from project_social.models import ProjectSocial
from common.factories.user import UserFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
import copy


class SearchTwitterPostsTests(APITestCase):
    global url, ex1, ex2, ex3, ex4, load
    url = reverse('project_social:twitter_posts_search')
    load = {
        'keywords': [],
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
        'expert_mode': False,
        'query_filter': '',
        'sort_posts': '',
    }
    ex1 = {
        'id': 1,
        'post_id': '11111111',
        'user_name': '11111111',
        'user_alias': '11111111',
        'text': 'first 11111111',
        'sentiment': 'positive',
        'date': '2022-09-02T06:44:00Z',
        'country': 'USA',
        'language': 'En',
        'link': 'https://twitter.com/user/status/11111111',
        'count_favorites': 1,
        'count_totalretweets': 1,
        'count_replies': 2,
        'user_picture': None,
        'images': None,
        'count_tweetvalue': 1
    }
    ex2 = {
        'id': 2,
        'post_id': '21111111',
        'user_name': '11111111',
        'user_alias': '11111111',
        'text': 'second 11111111',
        'sentiment': 'positive',
        'date': '2022-09-02T06:44:00Z',
        'country': 'USA',
        'language': 'Ru',
        'link': 'https://twitter.com/user/status/21111111',
        'count_favorites': 1,
        'count_totalretweets': 1,
        'count_replies': 2,
        'user_picture': None,
        'images': None,
        'count_tweetvalue': 10
    }
    ex3 = {
        'id': 3,
        'post_id': '31111111',
        'user_name': '11111111',
        'user_alias': '11111111',
        'text': 'third 11111111',
        'sentiment': 'neutral',
        'date': '2023-09-02T06:44:00Z',
        'country': 'Canada',
        'language': 'En',
        'link': 'https://twitter.com/user/status/31111111',
        'count_favorites': 1,
        'count_totalretweets': 1,
        'count_replies': 2,
        'user_picture': None,
        'images': None,
        'count_tweetvalue': 5
    }
    ex4 = {
        'id': 4,
        'post_id': '41111111',
        'user_name': '41111111',
        'user_alias': '41111111',
        'text': '4',
        'sentiment': 'negative',
        'date': '2022-09-02T06:44:00Z',
        'country': 'USA',
        'link': 'https://twitter.com/user/status/41111111',
        'language': 'Arabic',
        'count_favorites': 1,
        'count_totalretweets': 1,
        'count_replies': 2,
        'user_picture': None,
        'images': None,
        'count_tweetvalue': 3
    }

    def setUp(self):
        self.client.force_login(UserFactory())

    def db_seeder(self):
        TweetBinderPostFactory(id=1, post_id=11111111, user_name='11111111', user_alias='11111111', text='first 11111111', sentiment='positive',
                               date='2022-09-02T06:44:00.00Z', country='USA', language='En', count_favorites=1, count_totalretweets=1, count_replies=2, count_tweetvalue=1)
        TweetBinderPostFactory(id=2, post_id=21111111, user_name='11111111', user_alias='11111111', text='second 11111111', sentiment='positive',
                               date='2022-09-02T06:44:00.000Z', country='USA', language='Ru', count_favorites=1, count_totalretweets=1, count_replies=2, count_tweetvalue=10)
        TweetBinderPostFactory(id=3, post_id=31111111, user_name='11111111', user_alias='11111111', text='third 11111111', sentiment='neutral',
                               date='2023-09-02T06:44:00.000Z', country='Canada', language='En', count_favorites=1, count_totalretweets=1, count_replies=2, count_tweetvalue=5)
        TweetBinderPostFactory(id=4, post_id=41111111, user_name='41111111', user_alias='41111111', text='4', sentiment='negative',
                               date='2022-09-02T06:44:00.000Z', country='USA', language='Arabic', count_favorites=1, count_totalretweets=1, count_replies=2, count_tweetvalue=3)
        self.project = ProjectSocialFactory()

    def test_search_with_keywords(self):
        self.db_seeder()
        data = copy.deepcopy(load)
        data['project_pk'] = self.project.id
        data['keywords'] = ['second']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex2]})

    def test_search_by_country(self):
        self.db_seeder()
        data = copy.deepcopy(load)
        data['project_pk'] = self.project.id
        data['keywords'] = ['first']
        data['country'] = ['USA']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex1]})

    def test_search_by_language(self):
        self.db_seeder()
        data = copy.deepcopy(load)
        data['project_pk'] = self.project.id
        data['keywords'] = ['4']
        data['language'] = ['Arabic']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex4]})

    def test_search_filtering_by_sentiment(self):
        self.db_seeder()
        data = copy.deepcopy(load)
        data['project_pk'] = self.project.id
        data['keywords'] = ['4']
        data['sentiment'] = ['negative']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex4]})

    def test_serarch_filtering_by_date(self):
        self.db_seeder()
        data = copy.deepcopy(load)
        data['project_pk'] = self.project.id
        data['keywords'] = ['third']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex3]})

    def test_search_by_author(self):
        self.db_seeder()
        data = copy.deepcopy(load)
        data['project_pk'] = self.project.id
        data['keywords'] = ['first']
        data['author'] = ['11111111']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex1]})

    def test_search_with_sort(self):
        self.db_seeder()
        data = copy.deepcopy(load)
        data['project_pk'] = self.project.id
        data['keywords'] = ['first', 'second', 'third', '4']
        data['sort_posts'] = 'potential_reach'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 4, 'posts': [ex2, ex3, ex4, ex1]})
