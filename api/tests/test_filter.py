from common.factories.feedlink import FeedlinkFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from selenium.webdriver.common.by import By
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import status
from selenium import webdriver
from datetime import timedelta
import time
import json


class FilterTests(APITestCase):
    def test_author_filter(self):
        [PostFactory(entry_author=f'a{i}', entry_published=now()-timedelta(days=1)) for i in range(30)]

        url = '/api/authors?author=a'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 20)

        url = '/api/authors?author=a2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 11)

    def test_language_filter(self):
        language1 = SpeechFactory(language='Latin')
        language2 = SpeechFactory(language='Latvian')
        PostFactory(feed_language=language1, entry_published=now()-timedelta(days=1))
        PostFactory(feed_language=language2, entry_published=now()-timedelta(days=1))

        url = '/api/speeches?language=L'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 2)

        url = '/api/speeches?language=Latv'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 1)
        self.assertEqual(json.loads(response.content), [{'language': 'Latvian'}])

    def test_country_filter(self):
        country1 = FeedlinkFactory(country='USA')
        country2 = FeedlinkFactory(country='UK')
        PostFactory(feedlink=country1, entry_published=now()-timedelta(days=1))
        PostFactory(feedlink=country2, entry_published=now()-timedelta(days=1))

        url = '/api/countries?country=U'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 2)

        url = '/api/countries?country=UK'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 1)
        self.assertEqual(json.loads(response.content), [{'country': 'UK'}])

    def test_source_filter(self):
        source1 = FeedlinkFactory(source1='BBC')
        source2 = FeedlinkFactory(source1='BLUE')
        PostFactory(feedlink=source1, entry_published=now()-timedelta(days=1))
        PostFactory(feedlink=source2, entry_published=now()-timedelta(days=1))

        url = '/api/sources?source=B'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 2)

        url = '/api/sources?source=BB'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 1)
        self.assertEqual(json.loads(response.content), [{'source1': 'BBC'}])
