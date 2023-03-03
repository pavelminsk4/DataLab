from rest_framework.test import APITestCase
from tweet_binder.models import *
from rest_framework import status
from django.urls import reverse
import json
import copy

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
      'author_dimensions':[],
      'language_dimensions':[],
      'country_dimensions':[],
      'source_dimensions':[],
      'sentiment_dimensions':[]
      }

class SearchTwitterPostsTests(APITestCase):
  global url, ex1, ex2, ex3, ex4
  url = reverse('project_social:twitter_posts_search')
  ex1 = {
    'id': 1,
    'post_id': '11111111',
    'user_name': '11111111',
    'user_alias': '11111111',
    'text': 'first 11111111',
    'sentiment_vote': 'positive',
    'creation_date': '2022-09-02T06:44:00Z',
    'locationString': 'USA',
    'language': 'En',
    'count_favorites': 1,
    'count_retweets':1,
    'count_replies': 2
    }
  ex2 = {
    'id':2,
    'post_id':'21111111',
    'user_name':'11111111',
    'user_alias':'11111111',
    'text':'second 11111111',
    'sentiment_vote':'positive',
    'creation_date': '2022-09-02T06:44:00Z',
    'locationString':'USA',
    'language':'Ru',
    'count_favorites':1,
    'count_retweets':1,
    'count_replies':2,
    }
  ex3 = {
    'id':3,
    'post_id':'31111111',
    'user_name':'11111111',
    'user_alias':'11111111',
    'text':'third 11111111',
    'sentiment_vote':'neutral',
    'creation_date': '2023-09-02T06:44:00Z',
    'locationString':'Canada',
    'language':'En',
    'count_favorites':1,
    'count_retweets':1,
    'count_replies':2,
    }
  ex4 = {
    'id':4,
    'post_id':'41111111',
    'user_name':'41111111',
    'user_alias':'41111111',
    'text':'4',
    'sentiment_vote':'negative',
    'creation_date': '2022-09-02T06:44:00Z',
    'locationString':'USA',
    'language':'Arabic',
    'count_favorites':1,
    'count_retweets':1,
    'count_replies':2,
    }
  def db_seeder(self):
    TweetBinderPost.objects.create(id=1, post_id=11111111, user_name='11111111', user_alias='11111111', text='first 11111111', sentiment_vote='positive', creation_date='2022-09-02T06:44:00.00Z', locationString='USA',language='En', count_favorites=1, count_retweets=1, count_replies=2)
    TweetBinderPost.objects.create(id=2, post_id=21111111, user_name='11111111', user_alias='11111111', text='second 11111111', sentiment_vote='positive', creation_date='2022-09-02T06:44:00.000Z', locationString='USA', language='Ru', count_favorites=1, count_retweets=1, count_replies=2)
    TweetBinderPost.objects.create(id=3, post_id=31111111, user_name='11111111', user_alias='11111111', text='third 11111111', sentiment_vote='neutral', creation_date='2023-09-02T06:44:00.000Z', locationString='Canada', language='En', count_favorites=1, count_retweets=1, count_replies=2)
    TweetBinderPost.objects.create(id=4, post_id=41111111, user_name='41111111', user_alias='41111111', text='4', sentiment_vote='negative', creation_date='2022-09-02T06:44:00.000Z', locationString='USA', language='Arabic', count_favorites=1, count_retweets=1, count_replies=2)

  def test_search_with_keywords(self):
    self.db_seeder()
    data = copy.deepcopy(DATA)
    data['keywords'] = ['second']
    data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex2]}) 
 
  def test_search_by_country(self):
    self.db_seeder()
    data = copy.deepcopy(DATA)
    data['keywords'] = ['first']
    data['country'] = 'USA'
    data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex1]})

  def test_search_by_language(self):
    self.db_seeder()
    data = copy.deepcopy(DATA)
    data['keywords'] = ['4']
    data['language'] = 'Arabic'
    data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex4]})

  def test_search_filtering_by_sentiment(self):
    self.db_seeder()
    data = copy.deepcopy(DATA)
    data['keywords'] = ['4']
    data['sentiment'] = 'negative'
    data['date_range'] = ['2022-09-02T06:44:00.000Z', '2022-11-30T06:44:00.000Z']
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex4]})

  def test_serarch_filtering_by_date(self):
    self.db_seeder()
    data = copy.deepcopy(DATA)
    data['keywords'] = ['third']
    data['date_range'] = ['2023-09-02T06:44:00.000Z', '2023-09-30T06:44:00.000Z']
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages':1, 'num_posts':1, 'posts':[ex3]})

  def test_search_by_author(self):
    self.db_seeder()
    data = copy.deepcopy(DATA)
    data['keywords'] = ['first']
    data['date_range'] = ['2022-09-02T00:00:00.000Z', '2022-11-30T00:44:00.000Z']
    data['author'] = '11111111'
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'num_pages': 1, 'num_posts': 1, 'posts': [ex1]})
