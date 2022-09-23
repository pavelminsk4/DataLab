from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from project.models import Post
from accounts.models import department
from django.contrib.auth.models import User
import json

class SearchTests(APITestCase):
  global url
  url = reverse('search')

  def db_seeder(self):
    Post.objects.create(entry_title='First post title', entry_summary='First post body')
    Post.objects.create(entry_title='Second post title', entry_summary='Second post body')
    Post.objects.create(entry_title='Third post', entry_summary='Third post body')
    Post.objects.create(entry_title='Fourth post', entry_summary='Fourth post body')

  def test_search(self):
    self.db_seeder()
    data = {'keywords':['First', 'Post'], 'exceptions':[], 'additions':[]}
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), [{'entry_media_thumbnail_url': None, 'entry_published': None, 'entry_summary': 'First post body', 'entry_title':'First post title', 'feed_language': None, 'sentiment': 'neutral'}])  
 
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
    self.assertEqual(json.loads(response.content),  [{'entry_media_thumbnail_url': None, 'entry_published': None, 'entry_summary': 'Third post body', 'entry_title':'Third post', 'feed_language': None, 'sentiment': 'neutral'}] )
    self.assertEqual(len(Post.objects.all()), 4)

  def test_serch_with_exclusion_and_additional_words(self):
     self.db_seeder()
     data = {'keywords':['post'], 'exceptions':['First'], 'additions':['title']}
     response = self.client.post(url, data, format='json')
     self.assertEqual(json.loads(response.content), [{'entry_media_thumbnail_url': None, 'entry_published': None, 'entry_summary': 'Second post body', 'entry_title':'Second post title', 'feed_language': None, 'sentiment': 'neutral'}])
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

