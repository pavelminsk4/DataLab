from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from project.models import Post, Speech, Feedlinks
from accounts.models import department
from countries_plus.models import Country
from django.contrib.auth.models import User
import json

class SearchTests(APITestCase):
  global url
  url = reverse('search')

  def db_seeder(self):
    Speech.objects.create(id=1, language='English (United States)')
    Speech.objects.create(id=2, language='Lithuanian (Lithuania)')
    Speech.objects.create(id=3, language='Italian (Italy)')
    Speech.objects.create(id=4, language='Arabic')
    Post.objects.create(entry_title='First post title', entry_summary='First post body', feed_language_id=1)
    Post.objects.create(entry_title='Second post title', entry_summary='Second post body', feed_language_id=2)
    Post.objects.create(entry_title='Third post', entry_summary='Third post body', feed_language_id=3)
    Post.objects.create(entry_title='Fourth post', entry_summary='Fourth post body', feed_language_id=4)

  def test_search(self):
    self.db_seeder()
    data = {'keywords':['First', 'Post'], 'exceptions':[], 'additions':[]}
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'entry_media_thumbnail_url': None, 'entry_published': None, 'entry_summary': 'First post body', 'entry_title':'First post title', 'sentiment': 'neutral', 'feed_language__language': 'English (United States)'}])  
 
  def test_search_with_exclusion_words(self):
    self.db_seeder()
    data = {'keywords':['post'], 'exceptions':['First'], 'additions':[]}
    response = self.client.post(url, data, format='json')
    self.assertEqual(len(json.loads(response.content)), 3)
    self.assertEqual(len(Post.objects.all()), 4)

  def test_search_with_additional_words(self):
    self.db_seeder()
    data = {'keywords':['post'], 'exceptions':[], 'additions':['Third']}
    response = self.client.post(url, data, format='json')
    self.assertEqual(json.loads(response.content),  [{'entry_media_thumbnail_url': None, 'entry_published': None, 'entry_summary': 'Third post body', 'entry_title':'Third post', 'sentiment': 'neutral', 'feed_language__language': 'Italian (Italy)'}] )
    self.assertEqual(len(Post.objects.all()), 4)

  def test_serch_with_exclusion_and_additional_words(self):
     self.db_seeder()
     data = {'keywords':['post'], 'exceptions':['First'], 'additions':['title']}
     response = self.client.post(url, data, format='json')
     self.assertEqual(json.loads(response.content), [{'entry_media_thumbnail_url': None, 'entry_published': None, 'entry_summary': 'Second post body', 'entry_title':'Second post title', 'sentiment': 'neutral', 'feed_language__language': 'Lithuanian (Lithuania)'}])
     self.assertEqual(len(Post.objects.all()), 4)

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
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'source1': 'TNT'}, {'source1': 'BBC'}])

class SpeechesTests(APITestCase):
  def test_speeches_list(self):
    user = User.objects.create(username='John')
    self.client.force_authenticate(user=user)
    Speech.objects.bulk_create([Speech(language='Italy'), Speech(language='Albanian')])
    url = reverse('speeches_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'language': 'Albanian'}, {'language': 'Italy'}])

class CountriesTests(APITestCase):
  def create_country(self):
    Country.objects.create(iso='AF', iso3='AFG', name='Afghanistan', iso_numeric=4, fips='AF', capital='Kabul', area=1, population=1, continent='AS', tld='.af', currency_code='AFN', currency_name='Afghani', phone=93, languages='fa-AF,ps,uz-AF,tk', geonameid=1149361, neighbours='TM,CN,IR,TJ,PK,UZ')

  def test_countries_list(self):
    user = User.objects.create(username='Fox')
    self.client.force_authenticate(user=user)
    self.create_country()
    url = reverse('countries_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'name': 'Afghanistan'}])
