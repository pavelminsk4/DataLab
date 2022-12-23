from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from project.models import Post, Speech, Feedlinks
from accounts.models import department
from countries_plus.models import Country
from django.contrib.auth.models import User
import json
from datetime import datetime

class SearchTests(APITestCase):
  global url, ex1, ex2, ex3, ex4
  url = reverse('search')
  ex1 = {
    'id':1,
    'entry_title':'First post title',
    'entry_published':'2022-09-03T06:37:00Z',
    'entry_summary': 'First post body',
    'entry_media_thumbnail_url': None,
    'entry_media_content_url':None,
    'entry_links_href':None,
    'feed_image_href':None,
    'feed_image_link':None,
    'feed_language__language': 'English (United States)',
    'sentiment': 'neutral',
    'entry_author':'Elon Musk',
    'feedlink__country':'USA',
    'feedlink__source1': 'BBC',
    'feedlink__sourceurl':None,
    'feedlink__alexaglobalrank': 0,
    }
  ex2 = {
    'id':2,
    'entry_title':'Second post title',
    'entry_published':'2022-10-03T06:37:00Z',
    'entry_summary':'Second post body',
    'entry_media_thumbnail_url':None,
    'entry_media_content_url':None,
    'entry_links_href':None,
    'feed_image_href':None,
    'feed_image_link':None,
    'feed_language__language':'Lithuanian (Lithuania)',
    'sentiment':'neutral',
    'entry_author':'Tim Cook',
    'feedlink__country':'China',
    'feedlink__source1': 'CNN',
    'feedlink__sourceurl':None,
    'feedlink__alexaglobalrank': 0,
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
    }
  ex4 = {
    'id':4,
    'entry_title':'Fourth post',
    'entry_published':'2022-10-03T06:37:00Z',
    'entry_summary':'Fourth post body',
    'entry_media_thumbnail_url':None,
    'entry_media_content_url':None,
    'entry_links_href':None,
    'feed_image_href':None,
    'feed_image_link':None,
    'feed_language__language':'Arabic',
    'sentiment':'positive',
    'entry_author':'Steve Jobs',
    'feedlink__country':'China',
    'feedlink__source1': 'CNN',
    'feedlink__sourceurl':None,
    'feedlink__alexaglobalrank': 0,
    }

  def db_seeder(self):
    flink1 = Feedlinks.objects.create(country='USA', source1='BBC')
    flink2 = Feedlinks.objects.create(country='China', source1='CNN')
    sp1 = Speech.objects.create(language='English (United States)')
    sp2 = Speech.objects.create(language='Lithuanian (Lithuania)')
    sp3 = Speech.objects.create(language='Italian (Italy)')
    sp4 = Speech.objects.create(language='Arabic')
    Post.objects.create(id=1, feedlink=flink1, entry_title='First post title', entry_summary='First post body', feed_language=sp1, entry_author='Elon Musk', entry_published=datetime(2022, 9, 3, 6, 37), sentiment='neutral')
    Post.objects.create(id=2, feedlink=flink2, entry_title='Second post title', entry_summary='Second post body', feed_language=sp2, entry_author='Tim Cook', entry_published=datetime(2022, 10, 3, 6, 37), sentiment='neutral')
    Post.objects.create(id=3, feedlink=flink2, entry_title='Third post', entry_summary='Third post body', feed_language=sp3, entry_author='Bill Gates', entry_published=datetime(2022, 10, 3, 6, 37), sentiment='neutral')
    Post.objects.create(id=4, feedlink=flink2, entry_title='Fourth post', entry_summary='Fourth post body', feed_language=sp4, entry_author='Steve Jobs', entry_published=datetime(2022, 10, 3, 6, 37), sentiment='positive')

  def test_search_with_keywords(self):
    self.db_seeder()
    data = {
      'keywords':['First', 'Post'],
      'exceptions':[],
      'additions':[],
      'country':[],
      'language':[],
      'sentiment':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z'],
      'source':[],
      'author':[],
      'posts_per_page':20,
      'page_number':1,
      }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]}) 
 
  def test_search_with_exclusion_words(self):
    self.db_seeder()
    data = {
      'keywords':['post'],
      'exceptions':['First'],
      'additions':[],
      'country':[],
      'language':[],
      'sentiment':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z'],
      'source':[],
      'author':[],
      'posts_per_page':20,
      'page_number':1,
      }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':3, 'posts':[ex2,ex3,ex4]})
    self.assertEqual(len(Post.objects.all()), 4)

  def test_search_with_additional_words(self):
    self.db_seeder()
    data = {
      'keywords':['post'],
      'exceptions':[],
      'additions':['Third'],
      'country':[],
      'language':[],
      'sentiment':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z'],
      'source':[],
      'author':[],
      'posts_per_page':20,
      'page_number':1,
      }
    response = self.client.post(url, data, format='json')
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex3]})
    self.assertEqual(len(Post.objects.all()), 4)

  def test_serch_with_exclusion_and_additional_words(self):
    self.db_seeder()
    data = {
      'keywords':['post'],
      'exceptions':['First'],
      'additions':['title'],
      'country':[],
      'language':[],
      'sentiment':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z'],
      'source':[],
      'author':[],
      'posts_per_page':20,
      'page_number':1,
      }
    response = self.client.post(url, data, format='json')
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex2]})
    self.assertEqual(len(Post.objects.all()), 4)

  def test_search_by_country(self):
    self.db_seeder()
    data = {
      'keywords':['post'],
      'exceptions':[],
      'additions':[],
      'country':'USA',
      'language':[],
      'sentiment':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z'],
      'source':[],
      'author':[],
      'posts_per_page':20,
      'page_number':1,
      }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})

  def test_search_by_language(self):
    self.db_seeder()
    data = {
      'keywords':['post'],
      'exceptions':[],
      'additions':[],
      'country':[],
      'language':'Arabic',
      'sentiment':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z'],
      'source':[],
      'author':[],
      'posts_per_page':20,
      'page_number':1,
      }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex4]})

  def test_search_filtering_by_sentiment(self):
    self.db_seeder()
    data = {
      'keywords':['post'],
      'exceptions':[],
      'additions':[],
      'country':[],
      'language':[],
      'sentiment':'positive',
      'date':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z'],
      'source':[],
      'author':[],
      'posts_per_page':20,
      'page_number':1,
      }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex4]})

  def test_serarch_filtering_by_date(self):
    self.db_seeder()
    data = {
      'keywords':['post'],
      'exceptions':[],
      'additions':[],
      'country':[],
      'language':[],
      'sentiment':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-09-30T06:44:00.000Z'],
      'source':[],
      'author':[],
      'posts_per_page':20,
      'page_number':1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})

  def test_search_by_source(self):
    self.db_seeder()
    data = {
      'keywords':['post'],
      'exceptions':[],
      'additions':[],
      'country':[],
      'language':[],
      'sentiment':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z'],
      'source':'CNN',
      'author':[],
      'posts_per_page':20,
      'page_number':1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':3, 'posts':[ex2, ex3, ex4]})

  def test_search_by_author(self):
    self.db_seeder()
    data = {
      'keywords':['post'],
      'exceptions':[],
      'additions':[],
      'country':[],
      'language':[],
      'sentiment':[],
      'date_range':['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z'],
      'source':[],
      'author':'Elon Musk',
      'posts_per_page':20,
      'page_number':1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})

class CurrentUserTests(APITestCase):
  def test_logged_in_user(self):
    user = User.objects.create(username='John')
    user2 = User.objects.create(username='Pablo')
    company = department.objects.create(departmentname='Anadea')
    user.user_profile.department = company
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
    Feedlinks.objects.bulk_create([Feedlinks(source1='BBC'), Feedlinks(source1='TNT')])
    url = reverse('sources_list')
    response = self.client.post(url, 'B', format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'source1': 'BBC'}])

class SpeechesTests(APITestCase):
  def test_speeches_list(self):
    user = User.objects.create(username='John')
    self.client.force_authenticate(user=user)
    Speech.objects.bulk_create([Speech(language='Italy'), Speech(language='Albanian')])
    url = '/api/speeches/speeches?search=Alb'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'language': 'Albanian'}])

class CountriesTests(APITestCase):
  def create_country(self):
    Country.objects.create(iso='AF', iso3='AFG', name='Afghanistan', iso_numeric=4, fips='AF', capital='Kabul', area=1, population=1, continent='AS', tld='.af', currency_code='AFN', currency_name='Afghani', phone=93, languages='fa-AF,ps,uz-AF,tk', geonameid=1149361, neighbours='TM,CN,IR,TJ,PK,UZ')

  def test_countries_list(self):
    user = User.objects.create(username='Fox')
    self.client.force_authenticate(user=user)
    self.create_country()
    url = '/api/countries/countries?search=A'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'name': 'Afghanistan'}])

class AuthorsTests(APITestCase):
  def test_authors_list(self):
    flink = Feedlinks.objects.create(country='China', source1='CNN')
    sp = Speech.objects.create(language='English (United States)')
    Post.objects.create(feedlink=flink, entry_title='First post title', entry_summary='First post body', feed_language=sp, entry_author='Elon Musk', entry_published=datetime(2022, 9, 3, 6, 37), sentiment='neutral')
    Post.objects.create(feedlink=flink, entry_title='Second post title', entry_summary='Second post body', feed_language=sp, entry_author='Tim Cook', entry_published=datetime(2022, 10, 3, 6, 37), sentiment='neutral')
    url = '/api/authors/authors?search=E'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'entry_author': 'Elon Musk'}])
