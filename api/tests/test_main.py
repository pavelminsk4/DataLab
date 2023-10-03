from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.feedlinks import FeedlinksFactory
from common.factories.speech import SpeechFactory
from talkwalker.models import TalkwalkerPost
from common.factories.post import PostFactory
from common.factories.user import UserFactory
from project.models import Speech, Feedlinks
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from countries_plus.models import Country
from accounts.models import department
from rest_framework import status
from django.urls import reverse
from project.models import Post
import json
import copy
import os


DATA = {
      'keywords':[],
      'exceptions':[],
      'additions':[],
      'country':[],
      'language':[],
      'sentiment':[],
      'date_range':[],
      'source':[],
      'author':[],
      'posts_per_page': 20,
      'page_number': 1,
      'sort_posts':[],
      'author_dimensions':[],
      'language_dimensions':[],
      'country_dimensions':[],
      'source_dimensions':[],
      'sentiment_dimensions':[],
      'query_filter': '',
      'department_id':1,
      'expert_mode': False,
      }

global url, ex1, ex2, ex3, ex4
url = reverse('search')
ex1 = {
    'id':1,
    'entry_title':'First post title nikita',
    'entry_published':'2022-09-03T06:37:00Z',
    'entry_summary': 'First post body',
    'entry_media_thumbnail_url': None,
    'entry_media_content_url':None,
    'entry_links_href':None,
    'feed_image_link':None,
    'feed_image_href':None,
    'feed_language__language': 'English (United States)',
    'sentiment': 'neutral',
    'entry_author':'Elon Musk',
    'feedlink__country':'USA',
    'feedlink__source1': 'BBC',
    'feedlink__sourceurl':None,
    'feedlink__alexaglobalrank': 0,
    'category': None
    }
  
ex2 = {
    'id':2,
    'entry_title':'Second post title',
    'entry_published':'2022-10-03T06:37:00Z',
    'entry_summary':'Second post body',
    'entry_media_thumbnail_url':None,
    'entry_media_content_url':None,
    'feed_image_href':None,
    'feed_image_link':None,
    'feed_language__language':'Lithuanian (Lithuania)',
    'sentiment':'neutral',
    'entry_author':'Tim Cook',
    'entry_links_href':None,
    'feedlink__country':'China',
    'feedlink__source1': 'CNN',
    'feedlink__sourceurl':None,
    'feedlink__alexaglobalrank': 0,
    'category': None
    }
ex3 = {
    'id':3,
    'entry_title':'Third post',
    'entry_published':'2022-10-03T06:37:00Z',
    'entry_summary':'Third post body',
    'entry_media_thumbnail_url':None,
    'entry_media_content_url':None,
    'entry_links_href':None,
    'feed_image_href':None,
    'feed_image_link':None,
    'feed_language__language':'Italian (Italy)',
    'sentiment':'neutral',
    'entry_author':'Bill Gates',
    'feedlink__country':'China',
    'feedlink__source1': 'CNN',
    'feedlink__sourceurl':None,
    'feedlink__alexaglobalrank': 0,
    'category': None
    }
ex4 = {
    'id':4,
    'entry_title':'Fourth post',
    'entry_published':'2022-10-03T06:37:00Z',
    'entry_summary':'Fourth post body',
    'entry_media_thumbnail_url':None,
    'entry_media_content_url':None,
    'feed_image_href':None,
    'feed_image_link':None,
    'feed_language__language':'Arabic',
    'entry_author':'Steve Jobs',
    'entry_links_href':None,
    'feedlink__country':'China',
    'feedlink__source1': 'CNN',
    'feedlink__sourceurl':None,
    'feedlink__alexaglobalrank': 0,
    'sentiment':'positive',
    'category': None
    }


class SearchTestsTLW(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'
        self.client.force_login(UserFactory())
        flink1 = TalkwalkerFeedlinksFactory(country='USA', source1='BBC')
        flink2 = TalkwalkerFeedlinksFactory(country='China', source1='CNN')
        sp1 = SpeechFactory(language='English (United States)')
        sp2 = SpeechFactory(language='Lithuanian (Lithuania)')
        sp3 = SpeechFactory(language='Italian (Italy)')
        sp4 = SpeechFactory(language='Arabic')
        TalkwalkerPostFactory(id=1, feedlink=flink1, entry_title='First post title nikita', entry_summary='First post body', feed_language=sp1, entry_author='Elon Musk', entry_published='2022-09-03T06:37:00Z', sentiment='neutral')
        TalkwalkerPostFactory(id=2, feedlink=flink2, entry_title='Second post title', entry_summary='Second post body', feed_language=sp2, entry_author='Tim Cook', entry_published='2022-10-03T06:37:00Z', sentiment='neutral')
        TalkwalkerPostFactory(id=3, feedlink=flink2, entry_title='Third post', entry_summary='Third post body', feed_language=sp3, entry_author='Bill Gates', entry_published='2022-10-03T06:37:00Z', sentiment='neutral')
        TalkwalkerPostFactory(id=4, feedlink=flink2, entry_title='Fourth post', entry_summary='Fourth post body', feed_language=sp4, entry_author='Steve Jobs', entry_published='2022-10-03T06:37:00Z', sentiment='positive')


    def test_search_with_keywords_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['nikita']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]}) 
    
    def test_search_with_exclusion_words_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['exceptions'] = ['First']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':3, 'posts':[ex2,ex3,ex4]})
        self.assertEqual(len(TalkwalkerPost.objects.all()), 4)

    def test_search_with_additional_words_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['additions'] = ['Third']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex3]})
        self.assertEqual(len(TalkwalkerPost.objects.all()), 4)

    def test_serch_with_exclusion_and_additional_words_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['exceptions'] = ['First']
        data['additions'] = ['title']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex2]})
        self.assertEqual(len(TalkwalkerPost.objects.all()), 4)

    def test_search_by_country_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['country'] = 'USA'
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})

    def test_search_by_language_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['language'] = 'Arabic'
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex4]})

    def test_search_filtering_by_sentiment_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['sentiment'] = 'positive'
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex4]})

    def test_serarch_filtering_by_date_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-09-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})

    def test_search_by_source_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        data['source'] = 'CNN'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':3, 'posts':[ex2, ex3, ex4]})

    def test_search_by_author_tlw(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        data['author'] = 'Elon Musk'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})


class SearchTests(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'
        self.client.force_login(UserFactory())
        flink1 = FeedlinksFactory(country='USA', source1='BBC')
        flink2 = FeedlinksFactory(country='China', source1='CNN')
        sp1 = SpeechFactory(language='English (United States)')
        sp2 = SpeechFactory(language='Lithuanian (Lithuania)')
        sp3 = SpeechFactory(language='Italian (Italy)')
        sp4 = SpeechFactory(language='Arabic')
        PostFactory(id=1, feedlink=flink1, entry_title='First post title nikita', entry_summary='First post body', feed_language=sp1, entry_author='Elon Musk', entry_published='2022-09-03T06:37:00Z', sentiment='neutral')
        PostFactory(id=2, feedlink=flink2, entry_title='Second post title', entry_summary='Second post body', feed_language=sp2, entry_author='Tim Cook', entry_published='2022-10-03T06:37:00Z', sentiment='neutral')
        PostFactory(id=3, feedlink=flink2, entry_title='Third post', entry_summary='Third post body', feed_language=sp3, entry_author='Bill Gates', entry_published='2022-10-03T06:37:00Z', sentiment='neutral')
        PostFactory(id=4, feedlink=flink2, entry_title='Fourth post', entry_summary='Fourth post body', feed_language=sp4, entry_author='Steve Jobs', entry_published='2022-10-03T06:37:00Z', sentiment='positive')


    def test_search_with_keywords(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['nikita']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]}) 
    
    def test_search_with_exclusion_words(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['exceptions'] = ['First']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':3, 'posts':[ex2,ex3,ex4]})
        self.assertEqual(len(Post.objects.all()), 4)

    def test_search_with_additional_words(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['additions'] = ['Third']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex3]})
        self.assertEqual(len(Post.objects.all()), 4)

    def test_serch_with_exclusion_and_additional_words(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['exceptions'] = ['First']
        data['additions'] = ['title']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex2]})
        self.assertEqual(len(Post.objects.all()), 4)

    def test_search_by_country(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['country'] = 'USA'
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})

    def test_search_by_language(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['language'] = 'Arabic'
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex4]})

    def test_search_filtering_by_sentiment(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['sentiment'] = 'positive'
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex4]})

    def test_serarch_filtering_by_date(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-09-30T06:44:00.000Z']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})

    def test_search_by_source(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        data['source'] = 'CNN'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':3, 'posts':[ex2, ex3, ex4]})

    def test_search_by_author(self):
        data = copy.deepcopy(DATA)
        data['keywords'] = ['post']
        data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
        data['author'] = 'Elon Musk'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})


class CurrentUserTests(APITestCase):
    
    def test_logged_in_user(self):
        user = User.objects.create(username='John')
        user2 = User.objects.create(username='Pablo')
        user.user_profile.department = department.objects.create(departmentname='Anadea')
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
        url = '/api/sources/sources?search=B'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [{'source1': 'BBC'}])


class SpeechesTests(APITestCase):
    
    def test_speeches_list(self):
        self.client.force_authenticate(user=UserFactory())
        Speech.objects.bulk_create([Speech(language='Italy'), Speech(language='Albanian')])
        url = '/api/speeches/speeches?search=Alb'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [{'language': 'Albanian'}])


class CountriesTests(APITestCase):
    
    def create_country(self):
        Country.objects.create(iso='AF', iso3='AFG', name='Afghanistan', iso_numeric=4, fips='AF', capital='Kabul', area=1, population=1, continent='AS', tld='.af', currency_code='AFN', currency_name='Afghani', phone=93, languages='fa-AF,ps,uz-AF,tk', geonameid=1149361, neighbours='TM,CN,IR,TJ,PK,UZ')

    def test_countries_list(self):
        self.client.force_authenticate(user=UserFactory())
        self.create_country()
        url = '/api/countries/countries?search=A'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [{'name': 'Afghanistan'}])


class AuthorsTestsTLW(APITestCase):
    
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'
  
    def test_authors_list_tlw(self):
        self.client.force_login(UserFactory())
        flink1 = TalkwalkerFeedlinksFactory(country='USA', source1='BBC')
        sp1 = SpeechFactory(language='English (United States)')
        TalkwalkerPostFactory(id=1, feedlink=flink1, entry_title='First post title nikita', entry_summary='First post body', feed_language=sp1, entry_author='Elon Musk', entry_published='2022-09-03T06:37:00Z', sentiment='neutral')
        url = '/api/authors/authors?search=E'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [{'entry_author': 'Elon Musk'}])
