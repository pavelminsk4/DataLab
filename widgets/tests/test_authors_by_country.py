from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
import os


class AuthorsByCountryTestsTWL(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'
        
    def test_authors_by_country_tlw(self):
        flink1 = TalkwalkerFeedlinksFactory(country='England')
        flink2 = TalkwalkerFeedlinksFactory(country='USA')
        flink3 = TalkwalkerFeedlinksFactory(country='Greece')
        TalkwalkerPostFactory(feedlink=flink1, entry_author='AFP')
        TalkwalkerPostFactory(feedlink=flink2, entry_author='EFP', entry_title='1')
        TalkwalkerPostFactory(feedlink=flink2, entry_author='EFP', entry_title='2')
        TalkwalkerPostFactory(feedlink=flink3, entry_author='CFP', entry_title='1')
        TalkwalkerPostFactory(feedlink=flink3, entry_author='CFP', entry_title='2')
        TalkwalkerPostFactory(feedlink=flink3, entry_author='CFE')

        pr = ProjectFactory()
        widget_pk = pr.widgets_list_2.authors_by_country_id
        url = reverse('widgets:onl_authors_by_country', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
                {'Greece': [['CFP', 2], ['CFE', 1]]},
                {'England': [['AFP', 1]]},
                {'USA': [['EFP', 2]]}
              ]

        self.assertEqual(json.loads(response.content), res)

class AuthorsByCountryTests(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'
        
    def test_authors_by_country(self):
        flink1 = FeedlinksFactory(country='England')
        flink2 = FeedlinksFactory(country='USA')
        flink3 = FeedlinksFactory(country='Greece')
        PostFactory(feedlink=flink1, entry_author='AFP')
        PostFactory(feedlink=flink2, entry_author='EFP', entry_title='1')
        PostFactory(feedlink=flink2, entry_author='EFP', entry_title='2')
        PostFactory(feedlink=flink3, entry_author='CFP', entry_title='1')
        PostFactory(feedlink=flink3, entry_author='CFP', entry_title='2')
        PostFactory(feedlink=flink3, entry_author='CFE')

        pr = ProjectFactory()
        widget_pk = pr.widgets_list_2.authors_by_country_id
        url = reverse('widgets:onl_authors_by_country', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
                {'Greece': [['CFP', 2], ['CFE', 1]]},
                {'England': [['AFP', 1]]},
                {'USA': [['EFP', 2]]}
              ]

        self.assertEqual(json.loads(response.content), res)
