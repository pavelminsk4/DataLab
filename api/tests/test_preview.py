from common.factories.feedlink import FeedlinkFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from django.utils.timezone import now
from rest_framework import status
from datetime import timedelta
import json


class PreviewTests(APITestCase):
    def setUp(self):
        feedlink = FeedlinkFactory(source1='TIMES', country='USA')
        self.post1 = PostFactory(feedlink=feedlink, entry_title='USA lalalala', sentiment='positive', entry_author='BBC', entry_published=now()-timedelta(days=1))
        self.post2 = PostFactory(entry_title='Canada lalalala', entry_published=now())
        
    def test_preview(self):
        data = {
            'keywords': ['USA', 'CANADA'],
            'exclude': [],
            'additional': [],
            'country': ['USA'],
            'language': [],
            'source': ['TIMES'],
            'author': ['BBC'],
            'sentiment': ['positive']
        }
        
        url = '/api/project/preview'
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post1.id)
