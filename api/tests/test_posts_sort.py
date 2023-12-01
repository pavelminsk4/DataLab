from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from common.factories.user import UserFactory
from project.models import Speech, Feedlinks
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from countries_plus.models import Country
from accounts.models import Department
from rest_framework import status
from django.urls import reverse
from project.models import Post
import json
import copy


DATA = {
    'keywords': [],
    'exceptions': [],
    'additions': [],
    'country': [],
    'language': [],
    'sentiment': [],
    'date_range': [],
    'source': [],
    'author': [],
    'posts_per_page': 20,
    'page_number': 1,
    'sort_posts': '',
    'author_dimensions': [],
    'language_dimensions': [],
    'country_dimensions': [],
    'source_dimensions': [],
    'sentiment_dimensions': [],
    'query_filter': '',
    'department_id': 1,
    'expert_mode': False,
}

url = reverse('search')
ex1 = {
    'id': 1,
    'entry_title': 'First post title',
    'entry_published': '2022-09-03T06:37:00Z',
    'entry_summary': 'First post body',
    'entry_media_thumbnail_url': None,
    'entry_media_content_url': None,
    'entry_links_href': None,
    'feed_image_link': None,
    'feed_image_href': None,
    'feed_language__language': 'English (United States)',
    'sentiment': 'neutral',
    'entry_author': 'Elon Musk',
    'feedlink__country': 'USA',
    'feedlink__source1': 'BBC',
    'feedlink__sourceurl': None,
    'feedlink__alexaglobalrank': 2,
    'category': None
}

ex2 = {
    'id': 2,
    'entry_title': 'Second post title',
    'entry_published': '2022-10-03T06:37:00Z',
    'entry_summary': 'Second post body',
    'entry_media_thumbnail_url': None,
    'entry_media_content_url': None,
    'feed_image_href': None,
    'feed_image_link': None,
    'feed_language__language': 'Lithuanian (Lithuania)',
    'sentiment': 'neutral',
    'entry_author': 'Tim Cook',
    'entry_links_href': None,
    'feedlink__country': 'China',
    'feedlink__source1': 'CNN',
    'feedlink__sourceurl': None,
    'feedlink__alexaglobalrank': 3,
    'category': None
}

ex3 = {
    'id': 3,
    'entry_title': 'Third post',
    'entry_published': '2022-11-03T06:37:00Z',
    'entry_summary': 'Third post body',
    'entry_media_thumbnail_url': None,
    'entry_media_content_url': None,
    'entry_links_href': None,
    'feed_image_href': None,
    'feed_image_link': None,
    'feed_language__language': 'Italian (Italy)',
    'sentiment': 'neutral',
    'entry_author': 'Bill Gates',
    'feedlink__country': 'China',
    'feedlink__source1': 'CNN',
    'feedlink__sourceurl': None,
    'feedlink__alexaglobalrank': 3,
    'category': None
}

ex4 = {
    'id': 4,
    'entry_title': 'Fourth post',
    'entry_published': '2022-05-03T06:37:00Z',
    'entry_summary': 'Fourth post body',
    'entry_media_thumbnail_url': None,
    'entry_media_content_url': None,
    'feed_image_href': None,
    'feed_image_link': None,
    'feed_language__language': 'Arabic',
    'entry_author': 'Steve Jobs',
    'entry_links_href': None,
    'feedlink__country': 'China',
    'feedlink__source1': 'CNN',
    'feedlink__sourceurl': None,
    'feedlink__alexaglobalrank': 3,
    'sentiment': 'positive',
    'category': None
}


class SearchSortPostsTests(APITestCase):
    def setUp(self):
        self.client.force_login(UserFactory())
        flink1 = FeedlinkFactory(country='USA', source1='BBC', sourceurl=None, alexaglobalrank=2)
        flink2 = FeedlinkFactory(country='China', source1='CNN', sourceurl=None, alexaglobalrank=3)
        sp1 = SpeechFactory(language='English (United States)')
        sp2 = SpeechFactory(language='Lithuanian (Lithuania)')
        sp3 = SpeechFactory(language='Italian (Italy)')
        sp4 = SpeechFactory(language='Arabic')
        p1 = PostFactory(id=1, feedlink=flink1, entry_title='First post title', entry_summary='First post body', feed_language=sp1, entry_author='Elon Musk', entry_published='2022-09-03T06:37:00Z', sentiment='neutral')
        p2 = PostFactory(id=2, feedlink=flink2, entry_title='Second post title', entry_summary='Second post body', feed_language=sp2, entry_author='Tim Cook', entry_published='2022-10-03T06:37:00Z', sentiment='neutral')
        p3 = PostFactory(id=3, feedlink=flink2, entry_title='Third post', entry_summary='Third post body', feed_language=sp3, entry_author='Bill Gates', entry_published='2022-11-03T06:37:00Z', sentiment='neutral')
        p4 = PostFactory(id=4, feedlink=flink2, entry_title='Fourth post', entry_summary='Fourth post body', feed_language=sp4, entry_author='Steve Jobs', entry_published='2022-05-03T06:37:00Z', sentiment='positive')
        pr = ProjectFactory()
        pr.posts.set([p1, p2, p3, p4])
        DATA['project_pk'] = pr.id

    def test_sort_by_alexaglobalrank_desc(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2021-09-02T06:44:00.000Z', '2023-11-30T06:44:00.000Z']
        data['sort_posts'] = 'potential_reach_desc'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 4, 'posts': [ex4, ex2, ex3, ex1]})
        
    def test_sort_by_alexaglobalrank(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2021-09-02T06:44:00.000Z', '2023-11-30T06:44:00.000Z']
        data['sort_posts'] = 'potential_reach'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 4, 'posts': [ex1, ex4, ex2, ex3]})

    def test_sort_by_date_desc(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2021-09-02T06:44:00.000Z', '2023-11-30T06:44:00.000Z']
        data['sort_posts'] = 'date_desc'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 4, 'posts': [ex3, ex2, ex1, ex4]})
        
    def test_sort_by_date(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2021-09-02T06:44:00.000Z', '2023-11-30T06:44:00.000Z']
        data['sort_posts'] = 'date'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 4, 'posts': [ex4, ex1, ex2, ex3]})
        
    def test_sort_by_source(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2021-09-02T06:44:00.000Z', '2023-11-30T06:44:00.000Z']
        data['sort_posts'] = 'source'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 4, 'posts': [ex1, ex4, ex2, ex3]})

    def test_sort_by_languages(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2021-09-02T06:44:00.000Z', '2023-11-30T06:44:00.000Z']
        data['sort_posts'] = 'language'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 4, 'posts': [ex4, ex1, ex3, ex2]})

    def test_sort_by_country(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2021-09-02T06:44:00.000Z', '2023-11-30T06:44:00.000Z']
        data['sort_posts'] = 'country'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 4, 'posts': [ex4, ex2, ex3, ex1]})
