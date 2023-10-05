from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from project.models import Project
from rest_framework import status
from django.urls import reverse
import json, os


class DemographyFeatureTests(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'
        flink1 = FeedlinksFactory(source1='one_source', country='England', sourceurl='google')
        flink2 = FeedlinksFactory(source1='two_source', country='USA', sourceurl='youtube')
        flink3 = FeedlinksFactory(source1='third_source', country='England', sourceurl='twitter')
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Spanish')
        p1 = PostFactory(feedlink=flink1, feed_language=sp1, sentiment='negative')
        p2 = PostFactory(feedlink=flink2, feed_language=sp1, sentiment='positive', entry_title='1')
        p3 = PostFactory(feedlink=flink2, feed_language=sp2, sentiment='negative', entry_title='2')
        p4 = PostFactory(feedlink=flink3, feed_language=sp1, sentiment='neutral', entry_title='1')
        p5 = PostFactory(feedlink=flink3, feed_language=sp2, sentiment='neutral', entry_title='2')
        p6 = PostFactory(feedlink=flink3, feed_language=sp2, sentiment='positive', entry_title='3')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4, p5, p6):
            pr.posts.add(post)

    def test_top_sharing_sources(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.top_sharing_sources_id
        url = reverse('widgets:onl_top_sharing_sources', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {
                'type': 'Most active site',
                'name': 'third_source',
                'url': 'twitter',
                'value': '3 posts',
                'sentiments': {'positive': 1, 'negative': 0, 'neutral': 2},
                'picture': None,
            },
            {
                'type': 'Most influential site',
                'name': 'third_source',
                'url': 'twitter',
                'value': '90210 engagement',
                'sentiments': {'positive': 1, 'negative': 0, 'neutral': 2},
                'picture': None,
            },
        ]
        self.assertEqual(json.loads(response.content), res)

    def test_sources_by_country(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.sources_by_country_id
        url = reverse('widgets:onl_sources_by_country', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'England': [['third_source', 3], ['one_source', 1]]},
            {'USA': [['two_source', 2]]}
        ]
        self.assertEqual(json.loads(response.content), res)

    def test_sources_by_language(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.sources_by_language_id
        url = reverse('widgets:onl_sources_by_language', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'English': [['one_source', 1], ['third_source', 1], ['two_source', 1]]},
            {'Spanish': [['third_source', 2], ['two_source', 1]]}
        ]
        self.assertEqual(json.loads(response.content), res)

    def test_languages_by_country(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.languages_by_country_id
        url = reverse('widgets:onl_languages_by_country', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'England': [{'language': 'English', 'count': 2}, {'language': 'Spanish', 'count': 2}],
            'USA': [{'language': 'English', 'count': 1}, {'language': 'Spanish', 'count': 1}]
        }
        self.assertEqual(json.loads(response.content), res)

    def test_overall_top_sources(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.overall_top_sources_id
        url = reverse('widgets:onl_overall_top_sources', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {
                'name': 'third_source',
                'url': 'twitter',
                'picture': None,
                'sentiments': {
                    'positive': 1,
                    'negative': 0,
                    'neutral':  2,
                },
                'posts': 3,
                'reach': 0,
                'engagements': 0,
            },
            {
                'name': 'two_source',
                'url': 'youtube',
                'picture': None,
                'sentiments': {
                    'positive': 1,
                    'negative': 1,
                    'neutral':  0,
                },
                'posts': 2,
                'reach': 0,
                'engagements': 0,
            },
            {
                'name': 'one_source',
                'url': 'google',
                'picture': None,
                'sentiments': {
                    'positive': 0,
                    'negative': 1,
                    'neutral':  0,
                },
                'posts': 1,
                'reach': 0,
                'engagements': 0,
            },
        ]
        self.assertEqual(json.loads(response.content), res)


class DemographyFeatureTestsTLW(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'
        flink1 = TalkwalkerFeedlinksFactory(source1='one_source', country='England', sourceurl='google')
        flink2 = TalkwalkerFeedlinksFactory(source1='two_source', country='USA', sourceurl='youtube')
        flink3 = TalkwalkerFeedlinksFactory(source1='third_source', country='England', sourceurl='twitter')
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Spanish')
        p1 = TalkwalkerPostFactory(feedlink=flink1, feed_language=sp1, sentiment='negative')
        p2 = TalkwalkerPostFactory(feedlink=flink2, feed_language=sp1, sentiment='positive', entry_title='1')
        p3 = TalkwalkerPostFactory(feedlink=flink2, feed_language=sp2, sentiment='negative', entry_title='2')
        p4 = TalkwalkerPostFactory(feedlink=flink3, feed_language=sp1, sentiment='neutral', entry_title='1')
        p5 = TalkwalkerPostFactory(feedlink=flink3, feed_language=sp2, sentiment='neutral', entry_title='2')
        p6 = TalkwalkerPostFactory(feedlink=flink3, feed_language=sp2, sentiment='positive', entry_title='3')
        pr = ProjectFactory()
        for post in (p1, p2, p3, p4, p5, p6):
            pr.tw_posts.add(post)

    def test_top_sharing_sources_tlw(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.top_sharing_sources_id
        url = reverse('widgets:onl_top_sharing_sources', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {
                'type': 'Most active site',
                'name': 'third_source',
                'url': 'twitter',
                'value': '3 posts',
                'sentiments': {'positive': 1, 'negative': 0, 'neutral': 2},
                'picture': None,
            },
            {
                'type': 'Most influential site',
                'name': 'third_source',
                'url': 'twitter',
                'value': '90210 engagement',
                'sentiments': {'positive': 1, 'negative': 0, 'neutral': 2},
                'picture': None,
            },
        ]
        self.assertEqual(json.loads(response.content), res)

    def test_sources_by_country_tlw(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.sources_by_country_id
        url = reverse('widgets:onl_sources_by_country', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'England': [['third_source', 3], ['one_source', 1]]},
            {'USA': [['two_source', 2]]}
        ]
        self.assertEqual(json.loads(response.content), res)

    def test_sources_by_language_tlw(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.sources_by_language_id
        url = reverse('widgets:onl_sources_by_language', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'English': [['one_source', 1], ['third_source', 1], ['two_source', 1]]},
            {'Spanish': [['third_source', 2], ['two_source', 1]]}
        ]
        self.assertEqual(json.loads(response.content), res)

    def test_languages_by_country_tlw(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.languages_by_country_id
        url = reverse('widgets:onl_languages_by_country', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'England': [{'language': 'English', 'count': 2}, {'language': 'Spanish', 'count': 2}],
            'USA': [{'language': 'English', 'count': 1}, {'language': 'Spanish', 'count': 1}]
        }
        self.assertEqual(json.loads(response.content), res)

    def test_overall_top_sources_tlw(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.overall_top_sources_id
        url = reverse('widgets:onl_overall_top_sources', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {
                'name': 'third_source',
                'url': 'twitter',
                'picture': None,
                'sentiments': {
                    'positive': 1,
                    'negative': 0,
                    'neutral':  2,
                },
                'posts': 3,
                'reach': 0,
                'engagements': 0,
            },
            {
                'name': 'two_source',
                'url': 'youtube',
                'picture': None,
                'sentiments': {
                    'positive': 1,
                    'negative': 1,
                    'neutral':  0,
                },
                'posts': 2,
                'reach': 0,
                'engagements': 0,
            },
            {
                'name': 'one_source',
                'url': 'google',
                'picture': None,
                'sentiments': {
                    'positive': 0,
                    'negative': 1,
                    'neutral':  0,
                },
                'posts': 1,
                'reach': 0,
                'engagements': 0,
            },
        ]
        self.assertEqual(json.loads(response.content), res)
