from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from common.factories.user import UserFactory
from project.models import Speech, Feedlinks
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from accounts.models import Department
from project.models import Project
from rest_framework import status
from django.urls import reverse
import json
import copy


DATA = {
    'posts_per_page': 20,
    'page_number': 1,
    'sort_posts': []
}

global url, ex1, ex2, ex3, ex4
url = reverse('search')
ex1 = {
    'id': 1,
    'entry_title': 'First post title nikita',
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
    'feedlink__alexaglobalrank': 0,
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
    'feedlink__alexaglobalrank': 0,
    'category': None
}

ex3 = {
    'id': 3,
    'entry_title': 'Third post',
    'entry_published': '2022-10-03T06:37:00Z',
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
    'feedlink__alexaglobalrank': 0,
    'category': None
}

ex4 = {
    'id': 4,
    'entry_title': 'Fourth post',
    'entry_published': '2022-10-03T06:37:00Z',
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
    'feedlink__alexaglobalrank': 0,
    'sentiment': 'positive',
    'category': None
}


class SearchTests(APITestCase):
    maxDiff = None

    def setUp(self):
        self.client.force_login(UserFactory())
        flink1 = FeedlinkFactory(country='USA', source1='BBC', sourceurl=None)
        flink2 = FeedlinkFactory(country='China', source1='CNN', sourceurl=None)
        sp1 = SpeechFactory(language='English (United States)')
        sp2 = SpeechFactory(language='Lithuanian (Lithuania)')
        sp3 = SpeechFactory(language='Italian (Italy)')
        sp4 = SpeechFactory(language='Arabic')
        p1 = PostFactory(id=1, feedlink=flink1, entry_title='First post title nikita', entry_summary='First post body', feed_language=sp1, entry_author='Elon Musk', entry_published='2022-09-03T06:37:00Z', sentiment='neutral')
        p2 = PostFactory(id=2, feedlink=flink2, entry_title='Second post title', entry_summary='Second post body', feed_language=sp2, entry_author='Tim Cook', entry_published='2022-10-03T06:37:00Z', sentiment='neutral')
        p3 = PostFactory(id=3, feedlink=flink2, entry_title='Third post', entry_summary='Third post body', feed_language=sp3, entry_author='Bill Gates', entry_published='2022-10-03T06:37:00Z', sentiment='neutral')
        p4 = PostFactory(id=4, feedlink=flink2, entry_title='Fourth post', entry_summary='Fourth post body', feed_language=sp4, entry_author='Steve Jobs', entry_published='2022-10-03T06:37:00Z', sentiment='positive')
        pr = ProjectFactory(start_search_date='2022-09-02T06:44:00.000Z', end_search_date='2022-11-30T06:44:00.000Z')
        pr.posts.set([p1, p2, p3, p4])
        DATA['project_pk'] = pr.id

    def test_search_by_country(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.country_filter = ['USA']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex1]})

    def test_search_by_language(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.language_filter = ['Arabic']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex4]})

    def test_search_filtering_by_sentiment(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.sentiment_filter = ['positive']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex4]})

    def test_search_filtering_by_date(self):
        data = copy.deepcopy(DATA)
        data['date_range'] = ['2022-09-02T06:00:00.000Z', '2022-09-30T06:00:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex1]})

    def test_search_by_source(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.source_filter = ['CNN']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 3, 'posts': [ex2, ex3, ex4]})

    def test_search_by_author(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.author_filter = ['Elon Musk']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex1]})

    def test_search_by_country_dimensions(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.country_dimensions = ['USA']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex1]})

    def test_search_by_language_dimensions(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.language_dimensions = ['Arabic']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex4]})

    def test_search_filtering_by_sentiment_dimensions(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.sentiment_dimensions = ['positive']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex4]})

    def test_search_by_source_dimensions(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.source_dimensions = ['CNN']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 3, 'posts': [ex2, ex3, ex4]})

    def test_search_by_author_dimensions(self):
        data = copy.deepcopy(DATA)
        pr = Project.objects.get(id=DATA['project_pk'])
        pr.author_dimensions = ['Elon Musk']
        pr.save()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex1]})


class CurrentUserTests(APITestCase):
    def test_logged_in_user(self):
        user = User.objects.create(username='John')
        User.objects.create(username='Pablo')
        user.user_profile.department = Department.objects.create(departmentname='Anadea')
        user.user_profile.jobtitle = 'Boss'
        user.user_profile.phone = '+966-12345678'
        self.client.force_authenticate(user=user)
        url = reverse('logged_in_user')
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content)['username'], 'John')
        self.assertEqual(json.loads(response.content)['user_profile']['department']['departmentname'], 'Anadea')
        self.assertEqual(json.loads(response.content)['user_profile']['jobtitle'], 'Boss')
        self.assertEqual(json.loads(response.content)['user_profile']['phone'], '+966-12345678')


class SourcesTests(APITestCase):
    def test_sources_list(self):
        self.client.force_authenticate(user=UserFactory())
        Feedlinks.objects.bulk_create([Feedlinks(source1='BBC'), Feedlinks(source1='TNT')])
        url = '/api/sources/sources?limit=20&search=B'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['results'], [{'source1': 'BBC'}])


class SpeechesTests(APITestCase):
    def test_speeches_list(self):
        self.client.force_authenticate(user=UserFactory())
        Speech.objects.bulk_create([Speech(language='Italy'), Speech(language='Albanian')])
        url = '/api/speeches/speeches?limit=20&search=Alb'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['results'], [{'language': 'Albanian'}])


class CountriesTests(APITestCase):
    def test_countries_list(self):
        self.client.force_authenticate(user=UserFactory())
        Feedlinks.objects.bulk_create([Feedlinks(country='Belarus'), Feedlinks(country='USA')])
        url = '/api/countries/countries?limit=20&search=U'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['results'], [{'country': 'USA'}])
