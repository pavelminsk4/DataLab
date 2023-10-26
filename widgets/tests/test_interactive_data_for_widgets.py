from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from project.models import Project
from rest_framework import status
from project.models import Post
from django.urls import reverse
import json


class InteractiveWidgetsTests(APITestCase):
    def setUp(self):
        flink = FeedlinksFactory(country='England', source1='Time')
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Georgian')
        p1 = PostFactory(
            feedlink=flink, entry_title='First post title', entry_summary='First', feed_language=sp1,
            entry_published='2021-09-03T00:00:00Z', entry_author='AFP', sentiment='neutral'
        )
        p2 = PostFactory(
            feedlink=flink, entry_title='Second post title', entry_summary='Second post post title', feed_language=sp2,
            entry_published='2022-09-03T00:00:00Z', entry_author='AFP', sentiment='negative'
        )
        p3 = PostFactory(
            feedlink=flink, entry_title='Third post title', entry_summary='Third summary', feed_language=sp1,
            entry_published='2021-09-03T00:00:00Z', entry_author='AFP', sentiment='neutral'
        )
        p4 = PostFactory(
            feedlink=flink, entry_title='Fourth post title', entry_summary='Fourth summary', feed_language=sp1,
            entry_published='2021-09-03T00:00:00Z', entry_author='AFP', sentiment='negative'
        )
        pr = ProjectFactory(keywords=['post'])
        for post in (p1, p2):
            pr.posts.add(post)

    def test_top_10_interactive_widgets(self):
        pr = Project.objects.first()
        widget_pk = pr.widgets_list_2.top_languages_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        post1 = Post.objects.all().get(entry_title='First post title').pk
        data = {
            'first_value': ['English'],
            'second_value': [],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post1)

    def test_sentiment_top_10_interactive_widgets(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='Second post title').pk
        widget_pk = pr.widgets_list_2.sentiment_top_languages_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'second_value': ['negative'],
            'first_value': ['Georgian'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)

    def test_sentiment(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='Second post title').pk
        widget_pk = pr.widgets_list_2.sentiment_for_period_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'first_value': ['negative'],
            'second_value': [],
            'dates': ['2022-01-03T00:00:00Z', '2022-10-03T00:00:00Z'],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)

    def test_content_volume(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='Second post title').pk
        widget_pk = pr.widgets_list_2.volume_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'first_value': [],
            'second_value': [],
            'dates': ['2022-01-03T00:00:00Z', '2022-10-03T00:00:00Z'],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)

    def test_top_keywords(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='Second post title').pk
        widget_pk = pr.widgets_list_2.top_keywords_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'first_value': ['post'],
            'second_value': [],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)

    def test_sentiment_top_keywords(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='Second post title').pk
        widget_pk = pr.widgets_list_2.sentiment_top_keywords_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'first_value': ['post'],
            'second_value': ['negative'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)

    def test_sentiment_diagram(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='Second post title').pk
        widget_pk = pr.widgets_list_2.sentiment_diagram_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'first_value': ['negative'],
            'second_value': [],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)

    def test_authors_by_country(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='First post title').pk
        widget_pk = pr.widgets_list_2.authors_by_country_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'first_value': ['AFP'],
            'second_value': ['England'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)

    def test_authors_by_sentiment(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='First post title').pk
        widget_pk = pr.widgets_list_2.authors_by_sentiment_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'first_value': ['AFP'],
            'second_value': ['neutral'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)

    def test_sources_by_country(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='First post title').pk
        widget_pk = pr.widgets_list_2.sources_by_country_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'first_value': ['Time'],
            'second_value': ['England'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)

    def test_sources_by_language(self):
        pr = Project.objects.first()
        post_id = Post.objects.all().get(entry_title='First post title').pk
        widget_pk = pr.widgets_list_2.sources_by_language_id
        url = reverse('widgets:interactive_widgets', kwargs={
                      'project_pk': pr.pk, 'widget_pk': widget_pk})
        data = {
            'first_value': ['Time'],
            'second_value': ['English'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)
                         ['posts'][0]['id'], post_id)
