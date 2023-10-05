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
        p1 = TalkwalkerPostFactory(feedlink=flink1, entry_author='AFP')
        p2 = TalkwalkerPostFactory(feedlink=flink2, entry_author='EFP', entry_title='1')
        p3 = TalkwalkerPostFactory(feedlink=flink2, entry_author='EFP', entry_title='2')
        p4 = TalkwalkerPostFactory(feedlink=flink3, entry_author='CFP', entry_title='1')
        p5 = TalkwalkerPostFactory(feedlink=flink3, entry_author='CFP', entry_title='2')
        p6 = TalkwalkerPostFactory(feedlink=flink3, entry_author='CFE')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4, p5, p6):
            pr.tw_posts.add(post)
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
        p1 = PostFactory(feedlink=flink1, entry_author='AFP')
        p2 = PostFactory(feedlink=flink2, entry_author='EFP', entry_title='1')
        p3 = PostFactory(feedlink=flink2, entry_author='EFP', entry_title='2')
        p4 = PostFactory(feedlink=flink3, entry_author='CFP', entry_title='1')
        p5 = PostFactory(feedlink=flink3, entry_author='CFP', entry_title='2')
        p6 = PostFactory(feedlink=flink3, entry_author='CFE')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4, p5, p6):
            pr.posts.add(post)
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
